from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.project, name='projects_view'),
    url(r'^(?P<project_id>[0-9]+)/$', views.projectDetails, name='project_details'),
    # url(r'^(?P<project_id>[0-9]+)/stories/', views.getStories, name = 'project_stories'),
    # url(r'^(?P<project_id>[0-9]+)/videos/', views.getVideos, name = 'project_videos'),
    # url(r'^(?P<project_id>[0-9]+)/interviews/', views.getInterviews, name = 'project_interviews'),
    url(r'^(?P<project_id>[0-9]+)/related-content/(?P<object_type>[a-z]+)/(?P<object_id>[0-9]+)/', views.contentDetails, name = 'content_details'),
    url(r'^(?P<project_id>[0-9]+)/related-content/', views.getContent, name = 'project_content'),
]
