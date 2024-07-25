from django.contrib import admin
from .models import Category, Symptom, Medicine, Disease

admin.site.register(Category)
admin.site.register(Symptom)
admin.site.register(Medicine)
admin.site.register(Disease)
