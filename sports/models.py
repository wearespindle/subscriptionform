from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import Person


class Participant(Person):
    date_of_birth = models.DateField(_('date of birth'))
    wheelchair_bound = models.BooleanField(_('wheelchair bound'), default=False)
    sport = models.ForeignKey('Sport')
    sport_details = models.ManyToManyField('SportDetail')
    team = models.ManyToManyField('Team')
    # TODO: Come up with a way to automatically assign participants to a club/coach.

    class Meta:
        verbose_name = _('Participant')


class Sport(models.Model):
    pass


class SportDetail(models.Model):
    """Sport details belong to a sport and participant and can, for example,
    be a time, weight class, personal record etc."""
    pass


class Team(models.Model):
    pass
