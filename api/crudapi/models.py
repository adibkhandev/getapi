from django.db import models

# Create your models here.

class apidata(models.Model):
	name= models.CharField(max_length=100)
	price = models.IntegerField()
	desc = models.CharField(max_length=50)
	