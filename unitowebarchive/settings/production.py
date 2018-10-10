# settings/production.py

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = []

INTERNAL_IPS = []
# Application definition



# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': get_env_variable("POSTGRES_HOST"),
        'NAME': get_env_variable("POSTGRES_DB"),
        'USER': get_env_variable("POSTGRES_USER"),
        'PASSWORD': get_env_variable("POSTGRES_PASSWORD"),
        'PORT': 5432,
    }
}
