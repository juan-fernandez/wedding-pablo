from django.views.generic.base import TemplateView
from .forms import ConfirmAssistance
from django.shortcuts import render
from django.http import HttpResponseRedirect

class Landing(TemplateView):
    template_name = "index.html"
    
    def post(self, request, *args, **kwargs):
        form = ConfirmAssistance(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/gracias')
        else:
            return HttpResponseRedirect('/error')
