from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Tag
from .forms import ImageForm, TagForm, AddTagForm
from django.http import JsonResponse

def index(request):
    return render(request,'photo_app/index.html')

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'photo_app/add_image.html', {'form': form})

def delete_image(request):
    images = Image.objects.all()
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        if image_id:
            image = Image.objects.get(pk=image_id)
            image.delete()
            return redirect('image_list')
    return render(request, 'photo_app/delete_image.html', {'images': images})



