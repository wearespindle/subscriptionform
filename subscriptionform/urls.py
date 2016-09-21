from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', include(admin.site.urls )),
    # url('^', include('django.contrib.auth.urls')), This is the standard django url that handles all authorization
    url(r'^login/$', login, {'template_name': 'login.html'}),
]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
