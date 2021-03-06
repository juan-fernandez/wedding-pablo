"""wedding URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from wedding.views import Landing, FormSubmit, Thanks, Error, Blog, Post

urlpatterns = [
    path('', Landing.as_view(), name='landing'),
    path('confirm-attendee/', FormSubmit.as_view(), {'form_name': 'confirm-attendee'}, name='confirm-attendee'),
    path('make-suggestion/', FormSubmit.as_view(), {'form_name': 'make-suggestion'}, name='make-suggestion'),
    path('gracias/', Thanks.as_view(), name='gracias'),
    path('error/', Error.as_view(), name='error'),
    path('admin/', admin.site.urls),
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/<slug:slug>/', Post.as_view(), name='post'),
    re_path(r'^froala_editor/', include('froala_editor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)