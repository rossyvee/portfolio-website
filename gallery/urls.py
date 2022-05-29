from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadphoto/', views.save_image, name='upload_photo'),
    path('category/', views.category, name='category'),
    path('location/', views.location, name='location'),
    path('photos/', views.photos, name='photos'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)