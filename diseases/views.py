from django.shortcuts import render
from .models import Disease, Category, Symptom, Medicine
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'home.html')



def by_category(request):
    query = request.GET.get('search')
    if query:
        categories = Category.objects.filter(Q(name__icontains=query) | Q(disease__name__icontains=query)).distinct()
    else:
        categories = Category.objects.all()
    return render(request, 'by_category.html', {'categories': categories})


def by_symptom(request):
    query = request.GET.get('search')
    if query:
        symptoms = Symptom.objects.filter(Q(name__icontains=query) | Q(disease__name__icontains=query)).distinct()
    else:
        symptoms = Symptom.objects.all()
    return render(request, 'by_symptom.html', {'symptoms': symptoms})

def by_medicine(request):
    query = request.GET.get('search')
    if query:
        medicines = Medicine.objects.filter(Q(name__icontains=query) | Q(disease__name__icontains=query)).distinct()
    else:
        medicines = Medicine.objects.all()
    return render(request, 'by_medicine.html', {'medicines': medicines})

def all_diseases(request):
    diseases = Disease.objects.all()
    return render(request, 'all_diseases.html', {'diseases': diseases})

def disease_detail(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    return render(request, 'disease_detail.html', {'disease': disease})

