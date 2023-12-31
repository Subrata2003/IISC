"""
Django settings for iisc project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from iisc import SAMPLE_DIR

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# TEMPLATES_DIR=os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qwj2g6-th$t-8jtpdj2^!h)i8nldyu_&)uh-3&nby5r&3%=d9w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'new',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_auto_logout.middleware.auto_logout', #auto logout
]

ROOT_URLCONF = 'iisc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django_auto_logout.context_processors.auto_logout_client', #auto logout  
            ],
        },
    },
]

WSGI_APPLICATION = 'iisc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# STATICFILES_DIRS = [
#     ('static', os.path.join(BASE_DIR, "static")),
#     ('sample', os.path.join(SAMPLE_DIR, "task_tumor_design2")),
# ]

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static/"),
# ]

LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/summary/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
#EMAIL_HOST_USER = 'simgraph.iisc@gmail.com'
#EMAIL_HOST_PASSWORD = 'ecojhhdzdounewvl'
EMAIL_HOST_USER = 'iamrohit1702@gmail.com'
EMAIL_HOST_PASSWORD = 'jujwwelrbfdvsvmc'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

AUTO_LOGOUT = {
    # 'IDLE_TIME': timedelta(minutes=10),
    # 'SESSION_TIME': timedelta(minutes=50),
    'MESSAGE': 'The session has expired. Please login again to continue.',
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'upload')

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Add this line to define the UPLOAD_DIR
UPLOAD_DIR = os.path.join(BASE_DIR, 'upload')
