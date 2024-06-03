import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "secret")

DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "*",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django_extensions",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.mailru",
    "allauth.socialaccount.providers.vk",
    "allauth.socialaccount.providers.github",
    "leaflet",
    "sslserver",
    "remembers",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "place_remeber.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(
                BASE_DIR,
                "templates",
            )
        ],
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

WSGI_APPLICATION = "place_remeber.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_DB_HOST"),
        "PORT": os.getenv("POSTGRES_DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": """django.contrib.auth.password_validation
        .UserAttributeSimilarityValidator""",
    },
    {
        "NAME": """django.contrib.auth.password_validation
        .MinimumLengthValidator""",
    },
    {
        "NAME": """django.contrib.auth.password_validation
        .CommonPasswordValidator""",
    },
    {
        "NAME": """django.contrib.auth.password_validation
        .NumericPasswordValidator""",
    },
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SOCIAL_AUTH_JSONFIELD_ENABLED = True

SOCIAL_AUTH_VK_OAUTH2_KEY = "51926124"
SOCIAL_AUTH_VK_OAUTH2_SECRET = "CxZOe9702rZ66A8lgOwx"

LOGIN_URL = "users:login"

LOGIN_REDIRECT_URL = "remembers:main"

AUTH_USER_MODEL = "users.User"

LEAFLET_WIDGET_ATTRS = {
    "map_height": "500px",
    "map_width": "50%",
    "display_raw": "true",
    "map_srid": 4326,
}

SOCIALACCOUNT_PROVIDERS = {
    "vk": {
        "APP": {
            "client_id": os.getenv("SOCIAL_ID"),
            "secret": os.getenv("SOCAIL_SECRET"),
            "key": os.getenv("SOCIAL_KEY"),
        }
    }
}

SOCIALACCOUNT_FORMS = {
    "disconnect": "allauth.socialaccount.forms.DisconnectForm",
    "signup": "allauth.socialaccount.forms.SignupForm",
}

CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
    "https://localhost",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
    "https://localhost",
]

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

SOCIALACCOUNT_CONNECTIONS_TEMPLATE = "socialaccount/social.html"
