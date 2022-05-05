from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title') #list_display creates the headings of table in admin for these fields
    ordering = ('title',) #tells which field to use to sort the list
    search_fields = ('first_name',)
admin.site.register(Blog, BlogAdmin)

