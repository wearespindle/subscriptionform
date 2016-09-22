from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, password_reset

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^password_reset/$', password_reset, name='password_reset'),
]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
