from django.contrib import admin
from .models import MyUser, Coach, Club


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'date_of_birth',)
        }),
        ('More Options', {
            'classes': ('collapse',),
            'fields': ('is_staff', 'is_active',)
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_active',)


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'club', 'is_main_contact',)
    list_filter = ('club', 'is_main_contact',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city')
