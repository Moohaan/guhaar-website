from django.shortcuts import render
# Create your views here.
from projects.models import Project, Video,Interview, Story
import pdb

def home(request):
    projects = Project.objects.all()
    videos = Video.objects.all()
    interviews = Interview.objects.all()
    stories = Story.objects.all()
    args = {
        'projects':projects,
        'videos':videos,
        'interviews':interviews,
        'stories':stories
    }
    return render(request, 'home/index.html', args)
    # return HttpResponse('<p>edfwe</p>')
