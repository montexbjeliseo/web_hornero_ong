from django.contrib import admin
from .models import *
from apps.comments.models import *


admin.site.register(Category)
admin.site.register(Tag)

class PostCommentsTabularInline(admin.TabularInline):
    model = PostComment
    max_num: 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    inlines = [PostCommentsTabularInline]