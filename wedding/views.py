from django.views.generic.base import TemplateView
from .forms import ConfirmAssistance
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .emails import send_email

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
            return HttpResponseRedirect('/gracias')
        else:
            return HttpResponseRedirect('/error')

class Error(TemplateView):
    template_name = "error.html"

class Thanks(TemplateView):
    template_name = "thanks.html"