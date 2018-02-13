from django.shortcuts import render
from django.http import HttpResponse #, Http404
from django.core import serializers
from django.http import JsonResponse
from .models import Project, Video, Story, Interview
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from operator import attrgetter
from itertools import chain
import json
# Create your views here.

# Paginator
def listing(request, data_list):
    paginator = Paginator(data_list, 10) # Show 10 results per page
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results = paginator.page(paginator.num_pages)
    return results
    # render(request, 'projects/project_related_content.html', {'data': results})

def home(request):
    projects = Project.objects.all()
    videos = Video.objects.all()
    interviews = Interview.objects.all()
    stories = Story.objects.all()
    stories = listing(request, stories)
    args = {
        'projects':projects,
        'videos':videos,
        'interviews':interviews,
        'stories':stories
    }
    return render(request, 'home/index.html', args)
    # return listing(request, stories)

def project(request):
    args = Project.objects.all()
    ctx = {
        'projects':args
    }
    return render(request, 'projects/projects.html', ctx)

def projectDetails(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # serialize all the data
    project =  serializers.serialize("json", project)
    # make json data
    context = json.dumps({
        'project': project,
    })
    # ajax response
    return JsonResponse(context,safe=False)


def getInterviews(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # get all the interviews sorted by date
    interviews = Interview.objects.filter(project = project)
    # return listing(request, interviews)
    context = {
        'data':listing(request, interviews),
        'str':'interview',
    }
    return render(request, 'projects/project_related_content.html', context)

def getVideos(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # get all the interviews sorted by date
    videos = Video.objects.filter(project = project)
    # return listing(request, videos)
    context = {
        'data':listing(request, videos),
        'str':'video'
    }
    return render(request, 'projects/project_related_content.html', context)

def getStories(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # get all the interviews sorted by date
    stories = Story.objects.filter(project = project)
    # return listing(request, stories)
    context = {
        'data':listing(request, stories),
        'str':'story',
    }
    return render(request, 'projects/project_related_content.html', context)

def getContent(request, project_id):
    project = Project.objects.filter(pk = project_id)
    # get all the content sorted by date
    stories = Story.objects.filter(project = project)
    videos = Video.objects.filter(project = project)
    interviews = Interview.objects.filter(project = project)
    result_list = sorted(chain(stories, videos, interviews),key=attrgetter('date_created'))
    # return listing(request, stories)
    context = {
        'data':listing(request, result_list),
    }
    return render(request, 'projects/project_related_content.html', context)

def interviewDetails(request, interview_id):
    interview = Interview.objects.filter(pk = interview_id)
    interview =  serializers.serialize("json", interview)
    context = json.dumps({
        'data':interview,
    })
    return JsonResponse(context, safe=False)

def storyDetails(request, story_id):
    story = Story.objects.filter(pk = story_id)
    story =  serializers.serialize("json", story)
    context = json.dumps({
        'data':story,
    })
    return JsonResponse(context, safe=False)

def videoDetails(request, video_id):
    video = Video.objects.filter(pk = video_id)
    video =  serializers.serialize("json", video)
    context = json.dumps({
        'data':video,
    })
    return JsonResponse(context, safe=False)
