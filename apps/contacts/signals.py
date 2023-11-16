from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from . import models

@receiver(post_save, sender=models.Contact)
def send_new_contact_email(sender, instance, **kwargs):
    
    subject = 'Nuevo contacto creado'
    message = f'{instance.name} te ha dejado un mensaje en el sitio\nVer en el sitio: http://{settings.DOMAIN}{instance.get_absolute_url()}'
    address = [settings.EMAIL_HOST_USER] 
    
    send_mail(subject, message, None, address, fail_silently=False)
