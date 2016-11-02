from django import forms

from sports.models import Participant


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'food_preferences', 'date_of_birth',
                  'wheelchair_bound', 'sport', 'sport_details', )
