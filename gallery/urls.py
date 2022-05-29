from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadphoto/', views.upload_photo, name='upload_photo'),
    path('category/', views.category, name='category'),
    path('location/', views.location, name='location'),
]
