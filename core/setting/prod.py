from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n4hz7k9$z^)=w$z10t7v6dke_4nyq&hvye4qgs@zt4wn1@7uz!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.testhostmtp.com', 'testhostmtp.com', '127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'NAME': '',
# 		'USER': '',
# 		'PASSWORD': '',
# 		'HOST':'localhost',
# 		'PORT':'3306',
# 	}
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = ''

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

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = ''
EMAIL_HOST_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ""

COMPRESS_ROOT = ''
COMPRESS_ENABLED = True
