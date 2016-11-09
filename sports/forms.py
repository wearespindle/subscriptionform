from django import forms

from .models import Participant


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'food_preferences', 'date_of_birth',
                  'wheelchair_bound', 'photo_choice', 'sport', 'sport_details',)
