from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('sections/create', views.SectionContentCreateView.as_view(), name='create_section'),
    path('sections/list', views.SectionContentListView.as_view(), name='list_sections'),
    path('sections/<slug:slug>/update', views.SectionContentUpdateView.as_view(), name='update_section'),
    path('sections/<slug:slug>/delete', views.SectionContentDeleteView.as_view(), name='delete_section'),
]
