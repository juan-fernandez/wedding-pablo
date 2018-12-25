from django.contrib import admin
from .models import Attendee

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_coming', 'number_attendees')


admin.site.register(Attendee, AttendeeAdmin)