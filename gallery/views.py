from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def upload_photo(request):
    return render(request, 'upload-photo.html')
