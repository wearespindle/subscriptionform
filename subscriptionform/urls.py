from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from home.views import index, MenuView


urlpatterns = [

    url(r'^$', index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url('^', include('sports.urls')),
    url('^', include('users.urls')),
    url(r'^menu/$', MenuView.as_view(), name='menu')

]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
