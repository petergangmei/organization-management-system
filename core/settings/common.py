
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1v7i3x%0fw)&qdo2&s9pcfc-+$op4njzuu)mg^#ta9l*qv2&a+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG= True
ALLOWED_HOSTS = ["*"]

BASE_URL = 'https://organization-management-system-ten.vercel.app/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baseapp',
    'event_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mdb',                      
#         'USER': 'muser',
#         'PASSWORD': '12345',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / '../db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

JWT_SECRET_KEY = config('JWT_SECRET_KEY')



LANGUAGE_CODE = 'en-us'
USE_TZ = True
TIME_ZONE = 'Asia/Kolkata'


STATIC_URL = '/static/'

STATICFILES_DIRS =[
    os.path.join(BASE_DIR, '../static')
]
STATIC_ROOT = os.path.join(BASE_DIR, '../assets')

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ---- (aws - SES setting ) ----
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('AWS_SES_REGION_ENDPOINT')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_SSL = config("EMAIL_USE_SSL")
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# ---- (aws - s3 bucket setting) ----
AWS_S3_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = config("AWS_REGION_NAME")
AWS_QUERYSTRING_EXPIRE = 300
AWS_QUERYSTRING_AUTH = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
