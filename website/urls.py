"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import ContactUs
from . import views
import projects

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projects.urls')),
    url(r'^contactus/', ContactUs.as_view(), name='contactus_view'),
    url(r'^aboutus/', include('aboutus.urls')),
    # TODO: stories/ is use less for now
    url(r'^story/(?P<story_id>[0-9]+)/$', projects.views.storyDetails, name='story_details'),
    url(r'^video/(?P<video_id>[0-9]+)/$', projects.views.videoDetails, name='video_details'),
    url(r'^interview/(?P<interview_id>[0-9]+)/$', projects.views.interviewDetails, name='interview_details'),
    # url(r'^project/(?P<project_id>[0-9]+)/stories/', views.stories, name = 'stories_view'),
    url(r'^', projects.views.home, name='home_view'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
