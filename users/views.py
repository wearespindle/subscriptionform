from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

from .models import MyUser
from .forms import UserUpdateForm


class MyUserUpdate(SuccessMessageMixin, UpdateView):
    model = MyUser
    form_class = UserUpdateForm
    success_url = reverse_lazy('menu')
    success_message = _('Your details were updated successfully.')

    def get_object(self):
        return get_object_or_404(MyUser, pk=self.request.user.id)
