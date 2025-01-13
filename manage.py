import os
import sys
from django.core.wsgi import get_wsgi_application

# Vercel requires an app or handler function
def handler(request, context):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chasko_coffee_stop.settings")
    application = get_wsgi_application()
    return application(request, context)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chasko_coffee_stop.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
