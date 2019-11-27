"""
WSGI config for mojedijeteinfo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from mojedijeteinfo.wsgi import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mojedijeteinfo.settings')

application = application(application)
