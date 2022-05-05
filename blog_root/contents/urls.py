from django.urls import path
from . import views
from .views import BlogDetailView, BlogListView 

urlpatterns=[
    path('', views.home, name="home"),
    path('list/', BlogListView.as_view(), name = 'list'),
    path('list/<int:pk>', BlogDetailView.as_view(), name='detail')
]

