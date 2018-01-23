from website.settings.base import *

import dj_database_url

DEBUG = False
# DEBUG = True

ALLOWED_HOSTS = ['guhaarwebsite.herokuapp.com', 'guhaar.com', 'www.guhaar.com', '']

DATABASES = { 'default': dj_database_url.config() }
django_heroku.settings(locals())
