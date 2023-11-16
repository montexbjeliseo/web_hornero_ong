from django.views.generic import CreateView, TemplateView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contacts/create.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:thanks')
    
class ThanksView(TemplateView):
    template_name = 'contacts/thanks.html'