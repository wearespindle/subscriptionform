from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, password_reset, password_change_done

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'login.html'},
        name='login'),
    # TODO: The password_reset.html template still needs to be created.
    url(r'^password_reset/$', password_reset, {'template_name': 'password_reset.html'},
        name='password_reset'),
    # TODO: The password_change_done template still needs to be created.
    url(r'^change_password_done/$', password_change_done, {'template_name': 'password_change_done.html'},
        name="password_change_done"),

]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
