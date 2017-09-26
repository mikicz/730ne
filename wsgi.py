import os
import sys
from pathlib import Path

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.insert(0, str((Path(__file__).resolve().parent / 'wsgi' / 'openshift').resolve()))

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
