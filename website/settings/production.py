from website.settings.base import *

import dj_database_url
# import cloudinary
import cloudinary.uploader
import cloudinary.api
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['guhaarwebsite.herokuapp.com', 'guhaar.com', 'www.guhaar.com']

SECRET_KEY = os.environ.get('SECRET_KEY')

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DATABASES = { 'default': dj_database_url.config() }

# # Cloudinary settings for Django. Add to your settings file.
# CLOUDINARY = {
#   'cloud_name': 'guhaar',
#   'api_key': '896979177588687',
#   'api_secret': '3ZaITYQmAnz41Qxkl0HzQkTKXeg',
# }
#

# # Cloudinary settings using python code. Run before pycloudinary is used.
cloudinary.config(
  cloud_name = 'guhaar',
  api_key = '896979177588687',
  api_secret = '3ZaITYQmAnz41Qxkl0HzQkTKXeg'
)
