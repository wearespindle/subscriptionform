"""
Django settings for project_name project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url

# Turn 0 or 1 into False/True respectively
boolean = lambda value: bool(int(value))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '5up$4$tbc-_ba*5unq@89wlp642_qobv_f%&m7p@royty2-u&7')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
    'home',
    'sports',
    'users',
    'club',

    # Django Extensions is a collection of custom extensions for the Django
    # Framework.
    # https://github.com/django-extensions/django-extensions
    'django_extensions',
    # Phonenumber_field is used to validate phonenumbers and use a PhoneNumberField
    # in a model. See: https://github.com/stefanfoulis/django-phonenumber-field
    'phonenumber_field',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'subscriptionform.middleware.LoginRequiredMiddleware',
    'club.middleware.ClubMiddleware',
)

ROOT_URLCONF = 'subscriptionform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'subscriptionform.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGES = [('en', 'English'),
             ('nl', 'Dutch'), ]

LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, os.pardir, 'subscriptionform', os.pardir, 'locale'),
)

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LOGIN_EXEMPT_URLS = (
    r'^$',
    r'^password_reset',
    r'^password_reset_done',
    r'^reset',
    r'^admin',
    r'^static',
)

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'Info <info@example.com>'
SERVER_EMAIL = 'Alerts <alerts@example.com>'

ADMINS = (
    ('Admin', 'admin@example.com'),
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s  [%(name)s:%(lineno)s]  %(levelname)s - %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        # Silence SuspiciousOperation.DisallowedHost exception ('Invalid
        # HTTP_HOST' header messages). Set the handler to 'null' so we don't
        # get those annoying emails.
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console', ],
            'level': 'INFO',
        }
    }
}

AUTH_USER_MODEL = 'users.MyUser'

PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'
