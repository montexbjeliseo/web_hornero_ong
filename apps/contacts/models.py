from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Correo electrónico')
    subject = models.CharField(max_length=150, verbose_name='Asunto')
    message = models.TextField(max_length=500, verbose_name='Mensaje')
    created_at = models.DateTimeField(auto_now = True, editable=False, verbose_name='Fecha de creación')
    readed = models.BooleanField(default=False, verbose_name='Fue leído?')
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("gallery:index")
    