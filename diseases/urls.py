from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('by_category/', views.by_category, name='by_category'),
    path('by_symptom/', views.by_symptom, name='by_symptom'),
    path('by_medicine/', views.by_medicine, name='by_medicine'),
    path('all_diseases/', views.all_diseases, name='all_diseases'),
    path('disease/<int:disease_id>/', views.disease_detail, name='disease_detail'),
]
