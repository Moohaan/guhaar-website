# from django.views.generic import TemplateView
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Member, Team
# Create your views here.
# import pdb
def aboutus(request):
    members = Member.objects.all()
    team = Team.objects.all()
    args = {
        'members':members,
        'team':team,
    }
    # pdb.set_trace()
    return render(request, 'aboutus/aboutus.html', args)
    # return render(request, 'aboutus/contactus.html')

def memberDetails(request, member_id):
    member = Member.objects.filter(pk = member_id)
    context =  serializers.serialize("json", member)
    return JsonResponse(context,safe=False)
