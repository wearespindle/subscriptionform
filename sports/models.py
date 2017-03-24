from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from club.models import Club, ClubMixin
from users.models import Person


class Participant(Person):
    """
    A model representing Participants of the sports event. It gathers some personal information
    by extending the Person class and assigns them to a sport and sport detail. Participants are
    automatically assigned to the Club to which the User that registered them belongs.
    """
    wheelchair_bound = models.BooleanField(_('wheelchair bound'), default=False)
    photo_choice = models.BooleanField(_('Photography allowed'), default=True)
    disciplines = models.ManyToManyField('Discipline', through='Performance')

    class Meta:
        verbose_name = _('Participant')

    def get_full_name(self):
        return self.first_name + " " + self.prefix + " " + self.last_name

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


class Discipline(models.Model):
    """
    A discipline is well, a discipline of a Sport that will be played during
    the event, for example the '50m sprint'.
    """
    name_of_discipline = models.CharField(_('discipline'), max_length=30)
    sport = models.ForeignKey(Sport)
    eventcode = models.CharField(max_length=12)

    class Meta:
        verbose_name = _('Discipline')

    def __str__(self):
        return self.name_of_discipline


class Performance(models.Model):
    """
    Intermediary model between a Participant and a Discipline, used to register a score, time,
    or other qualification.
    """
    discipline = models.ForeignKey(Discipline)
    participant = models.ForeignKey(Participant)
    qualification = models.CharField(_('qualification'), max_length=10, null=True)

    class Meta:
        # Makes sure a participant can only partake in a certain discipline once
        unique_together = ('discipline', 'participant',)

    def __str__(self):
        return str(self.qualification)

    def get_absolute_url(self):
        return reverse('participant_detail', kwargs={'pk':self.pk})


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
