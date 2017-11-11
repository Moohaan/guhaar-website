from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.aboutus, name='aboutus_view'),
    url(r'^(?P<member_id>[0-9]+)/$', views.memberDetails, name='member_details'),
]
