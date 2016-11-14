from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from sports.models import Participant


def index(request):
    return render_to_response('home/index.html')


class MenuView(TemplateView):
    template_name = "home/menu.html"
