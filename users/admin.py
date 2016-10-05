from django.contrib import admin
from .models import MyUser, Coach, Club


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'club', 'is_main_contact',)
    list_filter = ('club', 'is_main_contact',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city')
