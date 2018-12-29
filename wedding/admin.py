from django.contrib import admin
from .models import Attendee, Suggestion, BlogPost

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_coming', 'number_attendees')

admin.site.register(Attendee, AttendeeAdmin)

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('suggestion',)

admin.site.register(Suggestion, SuggestionAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'publication_date')
    readonly_fields = ['slug']

admin.site.register(BlogPost, BlogPostAdmin)