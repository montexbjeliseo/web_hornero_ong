from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from . import models

@receiver(post_save, sender=models.Contact)
def enviar_mensaje_nuevo_contacto(sender, instance, **kwargs):
    
    asunto = 'Nuevo contacto creado'
    mensaje = f'{instance.name} te ha dejado un mensaje en el sitio\nVer en el sitio: http://{settings.DOMAIN}{instance.get_absolute_url()}'
    destinatario = [settings.EMAIL_HOST_USER] 
    
    send_mail(asunto, mensaje, None, destinatario, fail_silently=False)
