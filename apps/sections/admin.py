from django.contrib import admin
from .models import *


class SectionImages(admin.TabularInline):
    model = SectionImage
    max_num: 0


@admin.register(SectionContent)
class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    inlines = [SectionImages]
