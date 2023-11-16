from django.urls import path
from .views import *


app_name = 'posts'

urlpatterns = [
    # Posts
    path('', PostListView.as_view(), name='index'),
    path('v/<slug:slug>', PostDetailView.as_view(), name='view'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name='delete'),
    path('<slug:slug>/update', PostUpdateView.as_view(), name='update'),
    path('<slug:slug>/like', like_post, name='like'),

    # Comments
    path('<slug:slug>/comment', PostCommentCreateView.as_view(), name='add_comment'),
    path('<slug:slug>/comment/<uuid:cpk>/delete',
         PostCommentDeleteView.as_view(), name='delete_comment'),
    path('<slug:slug>/comment/<uuid:cpk>/update',
         PostCommentUpdateView.as_view(), name='update_comment'),

    # Categories
    path('category/create', PostCategoryCreateView.as_view(), name='create_category'),
    path('category/<slug:slug>/update',
         PostCategoryUpdateView.as_view(), name='update_category'),
    path('category/<slug:slug>/delete',
         PostCategoryDeleteView.as_view(), name='delete_category'),
]
