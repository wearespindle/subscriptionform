from django.db import models
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField

from .middleware import get_current_user


class ClubManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        """
        Manipulate the returned queryset by adding a filter for club using the club linked
        to the current logged in user (received via custom middleware).
        """
        user = get_current_user()
        if user and user.is_authenticated():
            return super(ClubManager, self).get_queryset().filter(club=user.club)
        else:
            return super(ClubManager, self).get_queryset()


class Club(models.Model):
    """
    Represents a Club (sports organization) that participates in the event.
    """
    name = models.CharField(_('name'), max_length=128)
    street = models.CharField(_('street'), max_length=128)
    number = models.CharField(_('number'), max_length=10, blank=True)
    zipcode = models.CharField(_('zipcode'), max_length=6)
    city = models.CharField(_('city'), max_length=30)
    phone_number = PhoneNumberField(_('phonenumber'), default='+31')
    email = models.EmailField(_('email address'), max_length=254)

    def __str__(self):
        return self.name


class ClubMixin(models.Model):
    # Automatically filter any queryset by club if logged in.
    objects = ClubManager()
    club = models.ForeignKey(Club, null=True)

    def save(self, *args, **kwargs):
        user = get_current_user()

        if user and user.is_authenticated() and not self.club_id:
            self.club = user.club

        return super(ClubMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
