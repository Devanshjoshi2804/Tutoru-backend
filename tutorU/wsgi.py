import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorU.settings')

application = get_wsgi_application()

# Vercel expects a variable named "app" or "handler"
<<<<<<< HEAD
app = application
=======
app = application
>>>>>>> origin/main
