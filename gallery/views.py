from django.shortcuts import render
from .models import Category, Location


# Create your views here.

def index(request):
    return render(request, 'index.html')


def upload_photo(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'upload-photo.html', {"categories": categories, "locations": locations})


def location(request):
    locations = Location.objects.all()
    return render(request, 'location.html', {"locations": locations})


def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {"categories": categories})
