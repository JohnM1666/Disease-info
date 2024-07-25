from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom)
    cause = models.TextField(default='Unknown cause')
    precaution = models.TextField(default='No specific precaution')
    medicines = models.ManyToManyField(Medicine, blank=True)

    def __str__(self):
        return self.name
