from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Tekstovi(models.Model):
    naslov = models.CharField(max_length=220)
    datum = models.DateField()
    slika = models.FileField(null=True, blank=True)
    tekst = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.naslov

    class Meta:
        verbose_name_plural = 'Nova Objava'
