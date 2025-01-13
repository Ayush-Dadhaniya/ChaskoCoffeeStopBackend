from django.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chasko_coffee_stop.settings')
app = get_asgi_application()