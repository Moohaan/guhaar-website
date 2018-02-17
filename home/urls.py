from django.conf.urls import url
import projects
from . import views

urlpatterns = [
    url(r'^create-subscriber/', views.createSubscribe, name = 'create_subscriber'),
    url(r'^', projects.views.home, name='home_view'),
]
