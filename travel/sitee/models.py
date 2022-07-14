from django.db import models

# Create your models here.
class Profile(models.Model):
    Name=models.CharField(max_length=50)
    Date_of_birth=models.DateField()
    Gender=models.CharField(max_length=5)
    Phone_number=models.IntegerField(max_length=16)

class User(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE)
    address1=models.CharField(max_length=75)
    address2=models.CharField(max_length=75, blank=True)
    pincode=models.IntegerField(max_length=5)
