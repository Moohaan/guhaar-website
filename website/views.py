from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView
# import pdb
from . import settings
from home.models import Subscriber
from aboutus.form import ContactusForm
from projects.models import Story
# Create your views here.

class ContactUs(TemplateView):
    template_name = 'aboutus/contactus.html'

# handles GET request
    def get(self, request):
        form = ContactusForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ContactusForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form_name = form.cleaned_data.get('name')
            form_email = form.cleaned_data.get('email')
            form_message = form.cleaned_data.get('message')
            subscribe = form.cleaned_data.get('subscribe')

            # Check if the person wants to get subscribed
            if subscribe:
                subscriber = Subscriber.objects.create_subscriber(form_email, form_name)
                # check if email already exist or not IF IT DOES THEN create_subscriber would return False
                if subscriber:
                    subscriber.save()
                else:
                    pass
            subject = 'Guhaar India'
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
            if sent:
                messages.success(request, 'Thank you! Your message has been sent succefully!')
            else:
                messages.error(request, "Error! Try again")
        # return htt
        form = ContactusForm()
        return render(request, self.template_name, {'form':form})
