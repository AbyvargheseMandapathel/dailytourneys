"""
Django settings for classifiedads project.

Generated by 'django-admin startproject' using Django 2.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+$#4m3n(oz_n#ip-3bpl5g5ew7)v$gq66rwhgz(dune&0(2!)g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dailytourneys-1.abyvarghese2000.repl.co']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My apps
    'pages',
    'ads',
    'profiles',
    'taggit',
    'django_social_share',
    'authentication.apps.AuthenticationConfig',
    # Packages
    'ckeditor',
    'debug_toolbar',
    'embed_video',
    'phonenumber_field',
    'phonenumbers'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'classifiedads.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.footer_recent_ads',
            ],
        },
    },
]

WSGI_APPLICATION = 'classifiedads.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

"""PostgreSQL DB"""
# DATABASES = {
#     'default': {
#         'NAME': 'ClassifiedAdsDB',
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'USER': 'postgres',
#         'PASSWORD': 'admin123',
#         'HOST': 'localhost',
#     }
# }

"""SQLite DB"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Path to find static assets.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# Location of project wide static assets.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Location that holds user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# URL that handles the media files served from MEDIA_ROOT. 
MEDIA_URL = '/images/'

# DJ_DEBUG_TOOLBAR
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# CKEDITOR Configs
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'height': 'auto',
        'width': 'auto',
    }
}

#django_heroku.settings(locals())

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False 
#MAILJET_API_KEY = env('MAILJET_API_KEY')
#MAILJET_API_SECRET = env('MAILJET_API_SECRET')
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  
EMAIL_HOST_PASSWORD = env('pass')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

