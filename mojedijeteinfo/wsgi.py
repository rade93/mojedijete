"""
WSGI config for mojedijeteinfo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from django.contrib.staticfiles.handlers import StaticFilesHandler
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mojedijeteinfo.settings')

application = StaticFilesHandler(get_wsgi_application())
