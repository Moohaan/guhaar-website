from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscriber
import json
# Create your views here.

def createSubscribe(request):
    "Create subscriber if email does not exist already"
    if request.method == 'POST' and request.is_ajax():
        email = request.POST['email']
        name = email[0:email.find('@')]
        subscriber = Subscriber.objects.create_subscriber(email,name)
        report = False
        if subscriber:
            subscriber.save()
            report = True
        else:
            report = False
        context = json.dumps({
            'saved':report,
        })
        return JsonResponse(context, safe=False)
