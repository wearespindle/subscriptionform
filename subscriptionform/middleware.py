from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from re import compile


EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):
    """
    This LoginRequiredMixin ensures that a user needs to be authenticated
    for all views, except those listed in settings.LOGIN_EXEMPT_URLS and the
    LOGIN_URL.
    Requires authentication middleware and template context processors.
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), "Make sure the Login Required Middleware is installed.\
         Edit your MIDDLEWARE_CLASSES setting to insert\
         'django.contrib.auth.middleware.AuthenticationMiddleware'."
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)
