from website.settings.base import *

import dj_database_url
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# DEBUG = False
DEBUG = True
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['guhaarwebsite.herokuapp.com', 'guhaar.com', 'www.guhaar.com']
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES = { 'default': dj_database_url.config() }
# # Cloudinary settings using python code. Run before pycloudinary is used.
cloudinary.config(
  cloud_name = os.environ.get('cloud_name'),
  api_key = os.environ.get('api_key'),
  api_secret = os.environ.get('api_secret')
)
