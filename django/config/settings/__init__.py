import os

SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')

if SETTINGS_MODULE == 'config.settings.production':
    from .production import *
elif SETTINGS_MODULE == 'config.settings.test':
    from .test import *
else:
    from .local import *
