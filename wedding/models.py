from django.db import models
from django.template.defaultfilters import slugify

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

class Suggestion(models.Model):
    suggestion = models.TextField(max_length=240)
    def __str__(self):
        return self.suggestion

    class Meta:
        verbose_name = 'Sugerencia'
        verbose_name_plural = 'Sugerencias'

class BlogPost(models.Model):
    slug = models.SlugField(max_length=30, unique=True)
    title = models.CharField(max_length=30, verbose_name="Título")
    subtitle = models.CharField(
        max_length=100,
        verbose_name="Subtítulo",
        null=True,
        blank=True,
    )
    image = models.ImageField(null=True)
    content = models.TextField(max_length=500, verbose_name="Contenido")
    created_at = models.DateField(auto_now=True)
    publication_date = models.DateField(
        verbose_name="Fecha de publicación automática",
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)