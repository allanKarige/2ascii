from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Images
from .forms import ImgUploadForm
from .ASCII_conv import to_ascii


def index_page(request):
    return render(request, 'img_ascii/index.html')


def upload_page(request):
    if request.method == 'POST':
        form = ImgUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image1 = form.cleaned_data.get('image')
            image2 = Images(image=image1)
            image2.save()
            img_path = str(image2.image.name)
            output = to_ascii(img_path)
            image2.delete()
            return render(request, 'img_ascii/success.html', {'ascii':output})

    else:    
        form = ImgUploadForm()
    return render(request, 'img_ascii/upload.html', {'form': form})


