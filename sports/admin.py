from django.contrib import admin
from .models import Participant, Sport, SportDetail, Detail


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sport')
    list_filter = ('sport', 'wheelchair_bound',)


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SportDetail)
class SportDetailAdmin(admin.ModelAdmin):
    list_display = ('detail', 'sport',)


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('name_of_detail',)
