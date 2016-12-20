from django.contrib import admin
from .models import Coach, Participant, Sport, Team, Discipline, Performance


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'club',)
    list_filter = ('disciplines', 'club', 'wheelchair_bound',)


@admin.register(Coach)
class MyCoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'club')


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'club',)


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name_of_discipline', 'eventcode', 'sport',)


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'participant', 'qualification',)
