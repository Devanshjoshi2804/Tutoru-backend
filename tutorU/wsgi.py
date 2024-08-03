import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings
BASE_DIR = settings.BASE_DIR


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorU.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
