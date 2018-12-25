from django.db import models

class Attendee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    is_coming = models.BooleanField(default=False)
    number_attendees = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asistente'
        verbose_name_plural = 'Asistentes'