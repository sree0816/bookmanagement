from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    description=models.TextField(max_length=100,null=True,blank=True)
    coverimage=models.ImageField(upload_to='categoryimage',null=True,blank=True)

class BookDB(models.Model):
    title=models.CharField(max_length=20,null=True,blank=True)
    author=models.CharField(max_length=20,null=True,blank=True)
    category=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    publisher=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    coverimage = models.ImageField(upload_to='bookimage', null=True, blank=True)
