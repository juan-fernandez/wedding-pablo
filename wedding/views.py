from django.views.generic.base import TemplateView
from .forms import ConfirmAssistance
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .emails import send_email
from .models import Attendee, BlogPost

class Landing(TemplateView):
    template_name = "index.html"
    def post(self, request, *args, **kwargs):
        form = ConfirmAssistance(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            attendance = form.cleaned_data['attendance']
            how_many = form.cleaned_data['how_many']
            is_coming = True if attendance == 'true' else False
            send_email(name, email, how_many, is_coming)
            Attendee.objects.create(
                name=name,
                email=email,
                is_coming=is_coming,
                number_attendees=how_many
            )
            return HttpResponseRedirect('/gracias')
        else:
            return HttpResponseRedirect('/error')

class Error(TemplateView):
    template_name = "error.html"

class Thanks(TemplateView):
    template_name = "thanks.html"