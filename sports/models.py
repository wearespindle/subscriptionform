from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import Person, Club


class Participant(Person):
    """
    A model representing Participants of the sports event. It gathers some personal information
    by extending the Person class and assigns them to a sport and sport detail.
    """
    date_of_birth = models.DateField(_('date of birth'))
    wheelchair_bound = models.BooleanField(_('wheelchair bound'), default=False)
    photo_choice = models.BooleanField(_('Photography allowed'), default=True)
    sport = models.ForeignKey('Sport')
    sport_details = models.ManyToManyField('SportDetail')
    # TODO: Come up with a way to automatically assign participants to a club/coach.

    class Meta:
        verbose_name = _('Participant')

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()


class Sport(models.Model):
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
    """SportDetail is an intermediate model between the Sport and Detail models.
    It can be a time, weight class, personal record etc."""
    sport = models.ForeignKey(Sport)
    detail = models.ForeignKey(Detail)
    value = models.CharField(_('value'), max_length=20)


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    club = models.ForeignKey(Club)
    team_members = models.ManyToManyField(Participant)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = _('Team')
