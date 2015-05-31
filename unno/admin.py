from django.contrib import admin
from unno.models import *

class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name','email','website')
    search_fields = ('name',)
    

class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption','id','author','publish_time')
    list_filter = ('publish_time',)
    date_hierarachy = 'publish_time'
    ordering = ('-publish_time',)
    #fields = ('caption','author',)
    filter_horizontal = ('tags',)
    raw_id_fields = ('author',)

# Register your models here.

admin.site.register(Author,AuthorAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag)
