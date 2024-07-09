from core.settings.common import *

DEBUG = True
TEMPLATES_DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_URL = 'http://127.0.0.1:8000/'

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / '../db.sqlite3',
    }
}


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'