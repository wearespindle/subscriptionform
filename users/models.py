from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField


class MyUser(AbstractUser):
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        # The user is identified by his/her email address
        return self.email

    def get_short_name(self):
        # The user is identified by his/her email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name = _('User')


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    food_preferences = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class Coach(Person):
    """
    Coaches are the main contact person for a club
    and manage the registration of participants (i.e. participants
    don't register themselves).
    """
    club = models.ForeignKey('Club', null=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=255)
    is_main_contact = models.BooleanField(default=False)


class Club(models.Model):
    name = models.CharField(_('name'), max_length=128)
    street = models.CharField(_('street'), max_length=128)
    number = models.CharField(_('number'), max_length=10, blank=True)
    zipcode = models.CharField(_('zipcode'), max_length=6)
    city = models.CharField(_('city'), max_length=30)
    phone_number = PhoneNumberField(_('phonenumber'))
    email = models.EmailField(_('email address'), max_length=254)
