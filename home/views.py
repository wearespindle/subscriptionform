from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .forms import ParticipantForm


def index(request):
    return render_to_response('home/index.html')


@login_required
def add_participant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            participant.save()
    else:
        form = ParticipantForm()
    return render(request, 'home/add_participant.html', {'form': form})
