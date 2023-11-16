from apps.posts.models import Category
from django.urls import reverse


def blog_context(request):
    data = {
        'app_name': 'ONG Hornero',
        'categories': Category.objects.all(),
        'go_home': reverse('index'),
    }
    return data
