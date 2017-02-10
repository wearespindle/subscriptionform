from subscriptionform.settings.base import *  # noqa

DEBUG = boolean(os.environ.get('DEBUG', 0))
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# HTTPS and Security Settings
SECURE_HSTS_SECONDS = 31536000 # Future requests for the next year should use HTTPS only
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
