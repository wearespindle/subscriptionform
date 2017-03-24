from django.contrib import admin
from .models import Coach, Participant, Sport, Team, Discipline, Performance

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ParticipantResource(resources.ModelResource):
    """
    Class used for the export of a list of registered participants.
    """
    class Meta:
        model = Participant
        # The fields that are used for the export.
        fields = ('first_name', 'prefix', 'last_name', 'date_of_birth', 'gender', 'food_preferences',
                  'club__name', 'disciplines', 'disciplines__performance',)
        

class CoachResource(resources.ModelResource):
    """
    Class used for the export of a list of registered coaches.
    """
    class Meta:
        model = Coach
        # The fields that are used for the export.
        fields = ('club__name', 'first_name', 'prefix', 'last_name', 'gender',
                  'phone_number', 'email', 'food_preferences', )


class TeamResource(resources.ModelResource):
    """
    Class used for the export of teams.
    """
    class Meta:
        model = Team
        # The fields that are used for the export.
        fields = ('club__name', 'team_name', 'team_members')


@admin.register(Participant)
class ParticipantAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'prefix', 'last_name', 'club',)
    list_filter = ('disciplines', 'club', 'wheelchair_bound',)
    resource_class = ParticipantResource


@admin.register(Coach)
class MyCoachAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'club')


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('team_name', 'club',)


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name_of_discipline', 'eventcode', 'sport',)


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'participant', 'qualification',)
