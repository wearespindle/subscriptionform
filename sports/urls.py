from django.conf.urls import url

from .views import ParticipantCreate, ParticipantDelete, ParticipantDetail, ParticipantList, ParticipantUpdate
from .views import TeamCreate, TeamDelete, TeamDetail, TeamList, TeamUpdate
from .views import CoachCreate, CoachDelete, CoachDetail, CoachList, CoachUpdate
from .views import PerformanceCreate

urlpatterns = [

    url('^participants/$', ParticipantList.as_view(), name='participants'),
    url(r'^participants/(?P<pk>\d+)/$', ParticipantDetail.as_view(), name='participant_detail'),
    url(r'participants/add/$', ParticipantCreate.as_view(), name='participant_add'),
    url(r'participants/(?P<pk>\d+)/update/$', ParticipantUpdate.as_view(), name='participant_update'),
    url(r'participants/(?P<pk>[0-9]+)/delete/$', ParticipantDelete.as_view(), name='participant_delete'),
    url(r'participants/(?P<pk>[0-9]+)/delete/confirm/$', ParticipantDelete.as_view(), name='participant_delete_confirm'),
    url(r'teams/$', TeamList.as_view(), name='teams'),
    url(r'teams/add/$', TeamCreate.as_view(), name='team_add'),
    url(r'teams/(?P<pk>\d+)/$', TeamDetail.as_view(), name='team_detail'),
    url(r'teams/(?P<pk>\d+)/update/$', TeamUpdate.as_view(), name='team_update'),
    url(r'teams/(?P<pk>[0-9]+)/delete/$', TeamDelete.as_view(), name='team_delete'),
    url(r'teams/(?P<pk>[0-9]+)/delete/confirm/$', TeamDelete.as_view(), name='team_delete_confirm'),
    url(r'performance/add/$', PerformanceCreate.as_view(), name='performance_add'),    
    url(r'coaches/$', CoachList.as_view(), name='coaches'),
    url(r'coaches/add/$', CoachCreate.as_view(), name='coach_add'),
    url(r'coaches/(?P<pk>\d+)/$', CoachDetail.as_view(), name='coach_detail'),
    url(r'coaches/(?P<pk>\d+)/update/$', CoachUpdate.as_view(), name='coach_update'),
    url(r'coaches/(?P<pk>\d+)/delete/$', CoachDelete.as_view(), name='coach_delete'),
    url(r'coaches/(?P<pk>\d+)/delete/confirm/$', CoachDelete.as_view(), name='coach_delete_confirm'),

]
