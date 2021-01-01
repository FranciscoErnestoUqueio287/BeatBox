from pathlib import Path
import os
WEB_CONCURRENCY = 3
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ERROR_400_TEMPLATE_NAME = '404.html'
ERROR_403_TEMPLATE_NAME = '404.html'
ERROR_404_TEMPLATE_NAME = '404.html'
ERROR_500_TEMPLATE_NAME = '500.html'
ALLOWED_HOSTS = ["*","https://bbmz.herokuapp.com/"]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-%5g7gbqk+=+v&gwyu0!+d8t8*%omc!tfz7^1m-o^b6&z8=h88'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#SQL_ALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'beatbox',
    'beatboxapp',
    'db_file_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'beatbox.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'beatbox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#postgres://vhiwpdasrjjeyj:ead24368f75cf6ff54e7b9e0ba4a5a9361047830eae48a5310580bcb532b27df@ec2-54-196-89-124.compute-1.amazonaws.com:5432/d6375g9lo7ouqm
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST':'ec2-54-196-89-124.compute-1.amazonaws.com',
        #'NAME': str(BASE_DIR / 'db.sqlite3'),
        'PORT':'5432',
        'USER':'vhiwpdasrjjeyj',
        'PASSWORD':'ead24368f75cf6ff54e7b9e0ba4a5a9361047830eae48a5310580bcb532b27df'
        }
    }
import dj_database_url
DATABASES['default'] = dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-pt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_FILE_STORAGE = "db_file_storage.storage.DatabaseFileStorage"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATIC_TMP = os.path.join(BASE_DIR,'static')
MEDIA_URL = '/ourfiles/'
os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)
os.makedirs(MEDIA_ROOT, exist_ok=True)
