from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from club.models import Club, ClubMixin
from users.models import MyUser, Person


class Participant(Person):
    """
    A model representing Participants of the sports event. It gathers some personal information
    by extending the Person class and assigns them to a sport and sport detail. Participants are
    automatically assigned to the Club to which the User that registered them belongs.
    """
    wheelchair_bound = models.BooleanField(_('wheelchair bound'), default=False)
    photo_choice = models.BooleanField(_('Photography allowed'), default=True)
    sport = models.ForeignKey('Sport')
    sport_details = models.ManyToManyField('SportDetail', blank=True)

    class Meta:
        verbose_name = _('Participant')

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def _full_name(self):
        return '%s %s %s' % (self.first_name, self.prefix, self.last_name)
    full_name = property(_full_name)

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('participant_detail', kwargs={'pk': self.pk})


class Coach(Person):
    phone_number = PhoneNumberField(_('phonenumber'), default='+31')
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _('Coach')
        verbose_name_plural = _('Coaches')

    def get_full_name(self):
        return self.first_name + " " + self.prefix + " " + self.last_name

    def _full_name(self):
        return '%s %s %s' % (self.first_name, self.prefix, self.last_name)
    full_name = property(_full_name)

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('coach_detail', kwargs={'pk': self.pk})


class Sport(models.Model):
    """
    The sport model represents a sport that will be played during the event.
    """
    name = models.CharField(_('sport'), max_length=30)
    description = models.CharField(_('description'), max_length=150, blank=True)

    class Meta:
        verbose_name = _('Sport')

    def __str__(self):
        return self.name


class Detail(models.Model):
    """
    Detail is a model for the individual details.
    """
    name_of_detail = models.CharField(_('detail_name'), max_length=30)
    sport = models.ManyToManyField(Sport, through='SportDetail')

    class Meta:
        verbose_name = _('Detail')

    def __str__(self):
        return self.name_of_detail


class SportDetail(models.Model):
    """
    SportDetail is an intermediate model between the Sport and Detail models.
    It can be a time, weight class, personal record etc.
    """
    sport = models.ForeignKey(Sport)
    detail = models.ForeignKey(Detail, blank=True)
    value = models.CharField(_('value'), max_length=20)

    def __str__(self):
        return str(self.detail)


class Team(ClubMixin):
    """
    A team is a collection of Participants that is linked to a Club.
    """
    team_name = models.CharField(max_length=50)
    club = models.ForeignKey(Club)
    team_members = models.ManyToManyField(Participant, related_name='team_members')

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('Team')
