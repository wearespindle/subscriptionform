from django.conf.urls import url

from .views import MyUserUpdate

urlpatterns = [

    url('^users/update/$', MyUserUpdate.as_view(), name='user_update'),

]
