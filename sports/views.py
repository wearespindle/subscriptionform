from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CoachForm, ParticipantForm, PerformanceForm, TeamForm
from .models import Coach, Participant, Performance, Team


class ParticipantList(ListView):
    model = Participant


class ParticipantDetail(DetailView):
    model = Participant


class ParticipantCreate(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'multiple_add_forms.html'
    success_url = reverse_lazy('participants')
    performance_formset = modelformset_factory(Performance, form=PerformanceForm, extra=0)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        participant_form = self.get_form()
        participant_form.title = _('Participant')
        performance_form = self.performance_formset()
        performance_form.title = _('Performance')
        forms = [participant_form, performance_form, ]
        return self.render_to_response(
            self.get_context_data(forms=forms)
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        participant_form = self.get_form()
        if participant_form.is_valid():
            return self.form_valid(participant_form)
        else:
            return self.form_invalid(participant_form)

    def form_valid(self, participant_form):
        # Populates the form with the POST data
        performance_form = self.performance_formset(self.request.POST)
        if performance_form.is_valid():
            self.object = participant_form.save()
            # First remembers the performance record
            for form in performance_form:
                performance = form.save(commit=False)
                # Then adds the participant
                performance.participant = self.object
                # Finally saves to the database
                performance.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(participant_form)


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


class PerformanceCreate(CreateView):
    model = Performance
    form_class = PerformanceForm
    template_name = 'add_form.html'
