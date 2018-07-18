from website.settings.base import *
SECRET_KEY = os.environ.get('SECRET_KEY')

cloudinary.config(
  cloud_name = 'guhaar',
  api_key = '896979177588687',
  api_secret = '3ZaITYQmAnz41Qxkl0HzQkTKXeg'
)
DEBUG = True
SECURE_SSL_REDIRECT = False

UPLOADCARE = {
    'pub_key': 'd054d38a036a4221f387',
    'secret': 'e106e526a2b3c02586af ',
}
