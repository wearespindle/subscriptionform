from django.contrib import admin
from .models import Participant, Sport


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sport')
    list_filter = ('sport', 'wheelchair_bound',)


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)
