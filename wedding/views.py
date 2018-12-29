from django.views.generic.base import TemplateView, View
from .forms import ConfirmAssistance
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from .emails import send_email
from .models import Attendee, BlogPost
from django.template.response import TemplateResponse

class Landing(TemplateView):
    template_name = "index.html"

    def get(self, request):
        posts = BlogPost.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:4]
        return render(request, self.template_name, {'posts': posts})

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


class Blog(TemplateView):
    template_name = "post.html"

    def get(self, request, slug):
        blog_post = get_object_or_404(BlogPost, slug=slug)
        return TemplateResponse(
            request,
            self.template_name, 
            context={'blog_post': blog_post}
        )