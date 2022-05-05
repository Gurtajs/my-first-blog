from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog 


def home(request):
    return render(request, "contents/home.html")

class BlogListView(ListView):  #this kind of view always uses a "modelname"_list template (in this case loads a blog_list template)
    model = Blog
    context_object_name = 'blog_list'#tells Django what to name the QuerySet passed in the listview template, default is object."attribute"

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog_detail' #tells Django what to name the QuerySet passed in the detailview template



