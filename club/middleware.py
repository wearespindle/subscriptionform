from django.core.urlresolvers import reverse

from threading import local


_thread_locals = local()


def get_current_user():
    """
    Get the current user for club filtering
    """
    return getattr(_thread_locals, 'user', None)


class ClubMiddleware(object):
    """
    Make the user that makes the request retrievable from anywhere.
    """
    def process_request(self, request):
        """
        Save a reference to the user in local threading. When in Django admin,
        make sure to 'None' it to prevent the Middleware from filtering the QuerySets
        to the user's club.
        """
        if request.path.startswith(reverse('admin:index')):
            _thread_locals.user = None
        else:
            _thread_locals.user = getattr(request, 'user', None)
