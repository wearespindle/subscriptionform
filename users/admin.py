from django.contrib import admin
from .models import MyUser


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
