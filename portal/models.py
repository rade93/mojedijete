from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class NovaObjava(models.Model):
    naslov = models.CharField(max_length=220)
    tekst = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.naslov

    class Meta:
        verbose_name_plural = 'Nova Objava'
