from website.settings.base import *
SECRET_KEY = os.environ.get('SECRET_KEY')

cloudinary.config(
  cloud_name = os.environ.get('cloud_name'),
  api_key = os.environ.get('api_key'),
  api_secret = os.environ.get('api_secret')
)
DEBUG = True
SECURE_SSL_REDIRECT = False

# UPLOADCARE = {
#     'pub_key': 'd054d38a036a4221f387',
#     'secret': 'e106e526a2b3c02586af ',
# }
