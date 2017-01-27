from django import forms

from .models import MyUser


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'date_of_birth',)
