import os
from unipath import Path
import dj_database_url


PROJECT_DIR = Path(__file__).parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'seu@email.com'
EMAIL_HOST_PASSWORD = 'suasenha'


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Aqui sua chave secreta'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.localhost', '127.0.0.1'
    ]


# Application definition

INSTALLED_APPS = [
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'descontosveg.book',
    'descontosveg.moip',
    'storages',
    
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'descontosveg.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'descontosveg.wsgi.application'






# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
   'default': dj_database_url.config(
       default = 'sqlite:///' + PROJECT_DIR.child('database.db'))
   
}



ADMIN_SITE_HEADER = "DescontosVEG | Admin"

##
# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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



# ESQUEMA DE LOGIN
AUTH_PROFILE_MODULE = 'admin'

LOGIN_URL = 'django.contrib.auth.views.login'

LOGIN_REDIRECT_URL  =  '/'

LOGOUT_REDIRECT_URL  =  '/'


LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = PROJECT_DIR.child('staticfiles',)

MEDIA_ROOT = PROJECT_DIR.child('media')

MEDIA_URL = '/media/'

MOIP_PROD = False