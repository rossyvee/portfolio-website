from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadphoto/', views.upload_photo, name='upload_photo'),
]
