from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ImageForm
from .models import Category, Location, Image


# Create your views here.

def index(request):
    all_images=Image.objects.all()

    return render(request, 'index.html',{'images':all_images})


def photos(request):
    images = Image.objects.all()
    return render(request, 'photos.html', {'images': images})


def save_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
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

def display_mod(request,id):
    image=Image.objects.get(id=id)
    return render(request,'single.html',{'image':image})

def search_results(request):
    if 'cat' in request.GET and request.GET["cat"]:
        category = request.GET.get("cat")
        searched_images = Image.objects.filter(category__name__icontains=category).all()
        message = f"{category}"
        return render(request, 'search.html', {"message": message, "images": searched_images})