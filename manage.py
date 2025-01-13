import os
import sys
from django.core.management import execute_from_command_line

# This is the part that makes it compatible with Vercel.
from django.core.wsgi import get_wsgi_application

def handler(request, context):
    application = get_wsgi_application()
    return application(request, context)

# Normal Django management tasks.
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chasko_coffee_stop.settings")
    execute_from_command_line(sys.argv)
