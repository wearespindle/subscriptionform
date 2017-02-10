from subscriptionform.settings.base import *  # noqa

DEBUG = boolean(os.environ.get('DEBUG', 1))
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = []

#############################################
#     DJANGO DEBUG TOOLBAR CONFIGURATION    #
#############################################

if DEBUG:

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    INTERNAL_IPS = ('127.0.0.1', '172.17.42.1',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TEMPLATE_CONTEXT': True,
    }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
