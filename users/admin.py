from django.contrib import admin
from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('email',
                       'password',
                       'first_name',
                       'last_name',
                       'date_of_birth',
                       'club',
                       'groups',
                       )
        }),
        ('More Options', {
            'classes': ('collapse',),
            'fields': ('is_staff',
                       'is_active',
                       )
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'club', 'is_active',)
    list_filter = ('is_staff', 'is_superuser', 'club', 'is_active',)

    def save_model(self, request, obj, form, change):
        """
        Override saving model in Django Admin to use password encryption.
        """

        if change:
            # Updating existing user.
            orig_obj = MyUser.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            # Creating new user.
            obj.set_password(obj.password)

        obj.save()
