from django.conf.urls import url
from .views import ParticipantCreate, ParticipantDelete, ParticipantDetail, ParticipantList, ParticipantUpdate

urlpatterns = [

    url('^participants/$', ParticipantList.as_view(), name='participants'),
    url(r'^participants/(?P<pk>\d+)/$', ParticipantDetail.as_view(), name='participant_detail'),
    url(r'participants/add/$', ParticipantCreate.as_view(), name='participant_add'),
    url(r'participants/(?P<pk>\d+)/update/$', ParticipantUpdate.as_view(), name='participant_update'),
    url(r'participants/(?P<pk>[0-9]+)/delete/$', ParticipantDelete.as_view(), name='participant_delete'),
    url(r'participants/(?P<pk>[0-9]+)/delete/confirm/$', ParticipantDelete.as_view(), name='participant_delete_confirm'),

]
