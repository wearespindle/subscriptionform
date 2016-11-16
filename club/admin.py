from django.contrib import admin
from .models import Club


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city')
