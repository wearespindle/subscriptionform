from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField


class MyUser(PermissionsMixin, AbstractBaseUser):
    """
    Custom User model that allows logging in with email as username.
    """
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(_('staff status'), default=True,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Deselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(_('superuser'), default=False,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        # The user is identified by his/her email address
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')


class Person(models.Model):
    food_preferences = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class Coach(Person, MyUser):
    """
    Coaches are the main contact person for a club
    and manage the registration of participants (i.e. participants
    don't register themselves).
    """
    club = models.ForeignKey('Club', null=True)
    phone_number = PhoneNumberField(_('phonenumber'), default='+31')


class Club(models.Model):
    name = models.CharField(_('name'), max_length=128)
    street = models.CharField(_('street'), max_length=128)
    number = models.CharField(_('number'), max_length=10, blank=True)
    zipcode = models.CharField(_('zipcode'), max_length=6)
    city = models.CharField(_('city'), max_length=30)
    phone_number = PhoneNumberField(_('phonenumber'), default='+31')
    email = models.EmailField(_('email address'), max_length=254)
