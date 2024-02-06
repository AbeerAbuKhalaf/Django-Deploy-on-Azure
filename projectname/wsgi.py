import os

# Check for the PRODUCTION environment variable to see if we are running in Azure App Service
# If so, then load the settings from production.py
settings_module = 'projectname.production' if 'PRODUCTION' in os.environ else 'projectname.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
