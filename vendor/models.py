from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    company_name= models.CharField(max_length=255)
    
    