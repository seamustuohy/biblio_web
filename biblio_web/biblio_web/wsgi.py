"""
WSGI config for biblio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblio_web.settings')
#os.environ.setdefault('BiblioDBPath', '/home/recoll/bibliography.db')
#os.environ.setdefault('BiblioArchiveDir', '/var/lib/archive')

application = get_wsgi_application()
