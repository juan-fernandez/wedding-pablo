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

class BlogPost(models.Model):
    title = models.CharField(max_length=30, verbose_name="Título")
    slug = models.CharField(max_length=20, verbose_name="URL")
    content = models.TextField(max_length=500, verbose_name="Contenido")
    created_at = models.DateField(auto_now=True)
