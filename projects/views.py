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
    project = Project.objects.filter(pk = project_id)
    # videos  = Video.objects.filter(project = project)[:3]
    # stories = Story.objects.filter(project= project)
    # interviews = Interview.objects.filter(project = project)
    # serialize all the data
    project =  serializers.serialize("json", project)
    # videos =  serializers.serialize("json", videos)
    # stories =  serializers.serialize("json", stories)
    # interviews = serializers.serialize("json", interviews)
    # make json data
    context = json.dumps({
        'project': project,
        # 'videos': videos,
        # 'stories': stories,
        # 'interviews': interviews,
    })
    # ajax response
    return JsonResponse(context,safe=False)
    # else:
    #     raise Http404

def getInterviews(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # get all the interviews sorted by date
    interviews = Interview.objects.filter(project = project)
    # serialize the data into json
    interviews = serializers.serialize("json", interviews)

    context = json.dumps({
        'interviews':interviews,
    })
    return JsonResponse(context, safe=False)

def getVideos(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # get all the interviews sorted by date
    videos = Video.objects.filter(project = project)
    # serialize the data into json
    videos = serializers.serialize("json", videos)

    context = json.dumps({
        'videos':videos,
    })
    return JsonResponse(context, safe=False)

def getStories(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # get all the interviews sorted by date
    stories = Story.objects.filter(project = project)
    # serialize the data into json
    stories = serializers.serialize("json", stories)

    context = json.dumps({
        'interviews':stories,
    })
    return JsonResponse(context, safe=False)

def getInterviewById(request, interview_id):
    interview = Interview.objects.filter(pk = interview_id)

    context = json.dumps({
        'interview':interview,
    })
    return JsonResponse(context, safe=False)

def getStoryById(request, story_id):
    story = Story.objects.filter(pk = story_id)

    context = json.dumps({
        'story':story,
    })
    return JsonResponse(context, safe=False)

def getVideoById(request, video_id):
    video = Video.objects.filter(pk = video_id)

    context = json.dumps({
        'video':video,
    })
    return JsonResponse(context, safe=False)

def loadMoreStory(request):
    story = Story.objects.all()[:10];
    context = json.dumps({
        'story':story,
    })
    return JsonResponse(context, safe=False)

def loadMoreVideo(request):
    video = Video.objects.all()[:10];
    context = json.dumps({
        'video':video,
    })
    return JsonResponse(context, safe=False)

def loadMoreInterview(request):
    Interview = Interview.objects.all()[:10];
    context = json.dumps({
        'interview':interview,
    })
    return JsonResponse(context, safe=False)
