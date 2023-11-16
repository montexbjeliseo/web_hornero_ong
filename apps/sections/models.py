from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse
import os
import uuid


class SectionContent(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(
        max_length=250, verbose_name='Título')
    parent = models.CharField(
        max_length=250, verbose_name='Página a la que pertenece')
    content = models.TextField(verbose_name='Contenido de la sección')
    description = models.TextField(verbose_name='Descripcion del contenido', blank=True, null=True)
    css = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Contenido de sección'
        verbose_name_plural = 'Contenidos de secciones'

    def __str__(self):
        return f"{self.title}, contenido para \"{self.parent}\""

    def get_absolute_url(self):
        return reverse("update_section", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("delete_section", kwargs={"slug": self.slug})


class SectionImage(models.Model):
    section = models.ForeignKey(SectionContent, on_delete=models.CASCADE,
                                related_name='images', verbose_name='Sección a la que pertenece')
    image = models.ImageField(
        upload_to='section_images/', verbose_name='Archivo de imagen')

    class Meta:
        verbose_name = 'Imagen de sección'
        verbose_name_plural = 'Imágenes de secciones'

    def __str__(self):
        return f"Imagen para {self.section.title}"

    def save(self, *args, **kwargs):
        ext = self.image.name.split('.')[-1]
        unique_filename = f"{uuid.uuid4()}.{ext}"
        self.image.name = unique_filename
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            if storage.exists(path):
                storage.delete(path)
        super().delete(*args, **kwargs)


@receiver(pre_delete, sender=SectionImage)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
