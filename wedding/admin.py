from django.contrib import admin
from .models import Attendee, BlogPost

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_coming', 'number_attendees')

admin.site.register(Attendee, AttendeeAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')

admin.site.register(BlogPost, BlogPostAdmin)