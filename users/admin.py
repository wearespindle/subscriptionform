from django.contrib import admin
from .models import MyUser, Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'club', 'is_main_contact',)
    list_filter = ('club', 'is_main_contact',)
