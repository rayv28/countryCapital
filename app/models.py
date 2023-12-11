from django.db import models

# Create your models here.
class country(models.Model):
  countryName = models.CharField(max_length=30, primary_key=True)
  countryCode = models.IntegerField(unique=True)
  
class capital(models.Model):
  capitalName= models.CharField(max_length=30, primary_key=True)
  countryName = models.OneToOneField(country, on_delete=models.CASCADE)