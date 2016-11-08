from django.views.generic import DetailView, ListView
from .models import Participant


class ParticipantList(ListView):
    model = Participant


class ParticipantDetail(DetailView):
    model = Participant

