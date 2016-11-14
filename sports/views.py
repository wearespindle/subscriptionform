from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import ParticipantForm
from .models import Participant


class ParticipantList(ListView):
    model = Participant


class ParticipantDetail(DetailView):
    model = Participant


class ParticipantCreate(CreateView):
    model = Participant
    form_class = ParticipantForm


class ParticipantUpdate(UpdateView):
    model = Participant
    form_class = ParticipantForm


class ParticipantDelete(DeleteView):
    model = Participant
    success_url = reverse_lazy('participants')
