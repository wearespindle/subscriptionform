from django.views.generic import ListView
from .models import Participant


class ParticipantList(ListView):
    model = Participant
