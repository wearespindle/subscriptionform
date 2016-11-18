from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext as _

from club.models import ClubMixin, Club


class MyUser(ClubMixin, PermissionsMixin, AbstractBaseUser):
    """
    Custom User model that allows logging in with email as username.
    """
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    username = models.CharField(_('username'), max_length=30)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Deselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(_('superuser'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', ]

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


class Person(ClubMixin):
    food_preferences = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True
