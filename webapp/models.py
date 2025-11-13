from django.db import models

# Create your models here.
class SignupDB(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    password=models.CharField(max_length=20,blank=True,null=True)
    confirmpass=models.CharField(max_length=20,blank=True,null=True)
    mobile=models.CharField(max_length=20,blank=True,null=True)

class ContactDB(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    subject=models.CharField(max_length=20,blank=True,null=True)
    message=models.TextField(max_length=200,blank=True,null=True)