from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Participant, Team


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'food_preferences', 'date_of_birth',
                  'wheelchair_bound', 'photo_choice', 'sport', 'sport_details',)


class TeamForm(forms.ModelForm):
    """
    Form for creating and editing Teams, with a custom filter to
    only display the participants belonging to the club of the logged in
    user.
    """
    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['team_members'].queryset = Participant.objects.all()

    class Meta:
        model = Team
        fields = ('team_name', 'team_members',)
        help_texts = {
            'team_members': _('Keep "control" or "command" on a Mac pressed to select multiple participants.')
        }
