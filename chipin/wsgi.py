"""
WSGI config for chipin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
import warnings

warnings.filterwarnings("ignore", message="No directory at", module="whitenoise.base" )


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chipin.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='/path/to/static/files')
application.add_files('/path/to/more/static/files', prefix='more-files/')