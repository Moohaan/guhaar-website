from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import ContactUs
from . import views
import projects, aboutus

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projects.urls')),
    url(r'^contactus/', ContactUs.as_view(), name='contactus_view'),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^team/$', aboutus.views.team, name='team_view'),
    url(r'^story/(?P<story_id>[0-9]+)/$', projects.views.storyDetails, name='story_details'),
    url(r'^video/(?P<video_id>[0-9]+)/$', projects.views.videoDetails, name='video_details'),
    url(r'^interview/(?P<interview_id>[0-9]+)/$', projects.views.interviewDetails, name='interview_details'),
    url(r'^interviews/$', projects.views.interview, name='interviews_view'),
    # url(r'^project/(?P<project_id>[0-9]+)/stories/', views.stories, name = 'stories_view'),
    url(r'^', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
