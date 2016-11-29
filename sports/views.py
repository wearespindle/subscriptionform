from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import CoachForm, ParticipantForm, TeamForm
from .models import Coach, Participant, Team


class ParticipantList(ListView):
    model = Participant


class ParticipantDetail(DetailView):
    model = Participant


class ParticipantCreate(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'add_form.html'


class ParticipantUpdate(UpdateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'add_form.html'


class ParticipantDelete(DeleteView):
    model = Participant
    success_url = reverse_lazy('participants')
    template_name = 'confirm_delete.html'


class TeamList(ListView):
    model = Team


class TeamDetail(DetailView):
    model = Team


class TeamCreate(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'add_form.html'


class TeamUpdate(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'add_form.html'


class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('teams')
    template_name = 'confirm_delete.html'


class CoachList(ListView):
    model = Coach


class CoachDetail(DetailView):
    model = Coach


class CoachCreate(CreateView):
    model = Coach
    form_class = CoachForm
    template_name = 'add_form.html'


class CoachUpdate(UpdateView):
    model = Coach
    form_class = CoachForm
    template_name = 'add_form.html'


class CoachDelete(DeleteView):
    model = Coach
    success_url = reverse_lazy('coaches')
    template_name = 'confirm_delete.html'
