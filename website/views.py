from django.views.generic import TemplateView
from aboutus.form import ContactusForm
from django.core.mail import send_mail
from django.shortcuts import render
from projects.models import Story
from . import settings
# import pdb
# Create your views here.

def aboutus(request):
    members = Member.objects.all()
    args = {
        'members':members,
    }
    # pdb.set_trace()
    return render(request, 'home/about.html', args)

# def contactus(request):
#     form = ContactusForm()
#     return render(request, 'aboutus/contactus.html', {'form':form})

def stories(request):
    stories = Story.objects.all()
    args = {
        'stories':stories,
    }
    return render(request, 'projects/stories.html', args)

class ContactUs(TemplateView):
    template_name = 'aboutus/contactus.html'

# handles GET request
    def get(self, request):
        form = ContactusForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ContactusForm(request.POST or None)
        if form.is_valid():
            form_name = form.cleaned_data.get('name')
            form_email = form.cleaned_data.get('email')
            form_message = form.cleaned_data.get('message')
            subject = 'Guhaar'
            html_message = "%s:%s via %s"%(form_name, form_message, form_email)
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'contactguhaar@gmail.com']
            sent = send_mail(
                subject,
                form_message,
                from_email,
                to_email,
                fail_silently=True,
            )
        # return htt
        form = ContactusForm()
        return render(request, self.template_name, {'form':form,'success_message':sent})
