import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tiktactoe.settings")
django.setup()
applcation = get_default_application()