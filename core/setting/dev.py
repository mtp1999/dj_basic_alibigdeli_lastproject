from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n4hz7k9$z^)=w$z10t7v6dke_4nyq&hvye4qgs@zt4wn1@7uz!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


INTERNAL_IPS = [
    "127.0.0.1",
]

# sites
SITE_ID = 2

# using this in development mode
# we use smtp service in production mode
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


COMPRESS_ROOT = BASE_DIR / 'compress_static'
COMPRESS_ENABLED = True
