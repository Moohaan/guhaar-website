from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.project, name='projects_view'),
    url(r'^(?P<project_id>[0-9]+)/$', views.projectDetails, name='project_details'),
]
