from django.http import HttpResponse
from django.shortcuts import render

from .forms import ImageForm
from .models import Category, Location, Image


# Create your views here.

def index(request):
    return render(request, 'index.html')


def photos(request):
    images = Image.objects.all()
    return render(request, 'photos.html', {'images': images})


def save_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("Upload was successful!")
        return HttpResponse("Form was not valid!")

    else:
        image_form = ImageForm()
        categories = Category.objects.all()
        locations = Location.objects.all()
        return render(request, 'upload-photo.html',
                      {"categories": categories, "locations": locations, "form": image_form})


def location(request):
    locations = Location.objects.all()
    return render(request, 'location.html', {"locations": locations})


def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {"categories": categories})
