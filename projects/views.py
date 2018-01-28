from django.shortcuts import render
from django.http import HttpResponse #, Http404
from django.core import serializers
from django.http import JsonResponse
from .models import Project, Video, Story, Interview
import json
# Create your views here.
def project(request):
    args = Project.objects.all()
    ctx = {'projects':args}
    return render(request, 'projects/projects.html', ctx)

def projectDetails(request, project_id):
    # if request.is_ajax():
    # id = request.GET.get('id')
    project = Project.objects.filter(pk = project_id)
    videos  = Video.objects.filter(project = project)[:3]
    stories = Story.objects.filter(project= project)
    interviews = Interview.objects.filter(project = project)
    # serialize all the data
    project =  serializers.serialize("json", project)
    videos =  serializers.serialize("json", videos)
    stories =  serializers.serialize("json", stories)
    interviews = serializers.serialize("json", interviews)
    # make json data
    context = json.dumps({
    'project': project,
    'videos': videos,
    'stories': stories,
    'interviews': interviews,
    })
    # ajax response
    return JsonResponse(context,safe=False)
    # else:
    #     raise Http404
