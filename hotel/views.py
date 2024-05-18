from django.shortcuts import render, get_object_or_404
from .models import Category, Working, Taomlar

def home(request):
    work = Working.objects.all()
    categories = Category.objects.all()
    return render(request, 'base.html', context={"work": work, "cats": categories})

def category(request, id):
    cat = get_object_or_404(Category, id=id)
    work = cat.work.all()
    categories = Category.objects.all()
    return render(request, 'base.html', context={"work": work, "cats": categories})

def index(request, id):  
    cat = get_object_or_404(Working, id=id)
    taom = cat.taom.all()
    categories = Working.objects.all()
    return render(request, 'index.html', context={"taom": taom, "cats": categories})
