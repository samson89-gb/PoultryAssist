from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=100)

class Symptom(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    disease = models.ManyToManyField(Disease)

class Solution(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    description = models.TextField()


# Create your models here.
