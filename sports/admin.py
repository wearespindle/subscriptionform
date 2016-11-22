from django.contrib import admin
from .models import Participant, Sport, SportDetail, Detail, Team


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'club', 'sport')
    list_filter = ('sport', 'club', 'wheelchair_bound',)


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SportDetail)
class SportDetailAdmin(admin.ModelAdmin):
    list_display = ('detail', 'sport',)


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('name_of_detail',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'club',)
