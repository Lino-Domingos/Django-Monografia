from pathlib import Path
import os
#rom Accounts.models import Usuario

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p8^2p@)nf56_xh(_s7(v&e%=bm#6jjtxvl9agu#=8x$=g4zi^9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Authentication Model in Accounts Model


# Application definition
INSTALLED_APPS = [
    "Accounts.apps.AccountsConfig",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.gis',
    'leaflet',
    'corsheaders',
    
    
    'Team',
    'materializecssform',
    'Panel',
    'Project',
    'Task',
   
    
    
    
    
]

AUTH_USER_MODEL = 'Accounts.User'

#ROLEPERMISSIONS_MODULE = 'Project_Management.roles'

#ROLEPERMISSIONS_REGISTER_ADMIN = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Project_Management.urls'



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
            ],
        },
    },
]

WSGI_APPLICATION = 'Project_Management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'ProjectMangeDB',
        'USER':'postgres',
        'PASSWORD':'lino123',
        'HOST':'localhost',
        'PORT':5432,
    }
}

# GDAL_LIBRARY_PATH = os.environ.get("GDAL_LIBRARY_PATH")
# GEOS_LIBRARY_PATH=os.environ.get("GEOS_LIBRARY_PATH")

#AUTH_USER_MODEL = 'Accounts.Usuario' 

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS= [
    BASE_DIR / 'static', 
]



LOGIN_REDIRECT_URL = '/panel/'
LOGIN_URL = 'login'
#LOGOUT_REDIRECT_URL = 'login'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-25.9667, 32.5833),
    'DEFAULT_ZOOM': 18,
    'MAX_ZOOM': 18,
    #'SRID': 4326,
    'MIN_ZOOM':3,
    'MINIMAP': True,
    'RESET_VIEW': False,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'UEM-DMI',
}

CCORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # URL do seu aplicativo JavaScript
]
