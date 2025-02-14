from pathlib import Path
import os
from urllib.parse import urlparse
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-w!zzw2+j6i_le_e0^sb+=0+k1gkpq-@c=h0rij78b@udpq9%91')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    'chasko-coffee-stop.vercel.app',
    'chasko-coffee-stop-backend-df1uyvok4-ayush-dadhaniyas-projects.vercel.app',
    'chasko-coffee-stop-backend-git-master-ayush-dadhaniyas-projects.vercel.app',
    '*'
]

CORS_ALLOWED_ORIGINS = [
    "https://chasko-coffee-stop.vercel.app",
    "https://chasko-coffee-stop-backend-git-master-ayush-dadhaniyas-projects.vercel.app",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coffee_app',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chasko_coffee_stop.urls'

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

WSGI_APPLICATION = 'chasko_coffee_stop.wsgi.application'

# Database Configuration
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres.pygaenyeyjuelcntrgkh:PcC1zCfNUyznmaUn@aws-0-us-east-1.pooler.supabase.com:5432/postgres?sslmode=require'
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Use the database name "postgres" as per your pooler URL
        'USER': 'postgres.pygaenyeyjuelcntrgkh',  # Include the user prefix
        'PASSWORD': 'PcC1zCfNUyznmaUn',  # Use your actual password
        'HOST': 'aws-0-us-east-1.pooler.supabase.com',  # Use the Supabase session pooler hostname
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',  # Enforce SSL
        },
    }
}


CSRF_TRUSTED_ORIGINS = [
    'https://chasko-coffee-stop.vercel.app',
    'https://chasko-coffee-stop-backend-git-master-ayush-dadhaniyas-projects.vercel.app',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
