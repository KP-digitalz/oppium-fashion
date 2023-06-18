import os
from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admindocs",
    # External libraries
    "rest_framework",
    "mptt",
    "corsheaders",
    # Local applications
    "inventory",
    "dashboard",
]


SECRET_KEY = config("SECRET_KEY")


ROOT_URLCONF = "application.urls"
HOME_PAGE_VIEW = "oppium_fashion.views.IndexView"

WSGI_APPLICATION = "application.wsgi.application"
ASGI_APPLICATION = "application.asgi.application"
# DEBUG = True

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = []


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
]


STATIC_URL = "/static/"
STATIC_ROOT = config("STATIC_ROOT", default="static/")

MEDIA_URL = "/media/"
MEDIA_ROOT = config("MEDIA_ROOT", default="media/")


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Amsterdam"


USE_I18N = True
# USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_USE_SESSIONS = True

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASS": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 25,
}
