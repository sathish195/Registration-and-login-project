from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Reg(models.Model):
    User_Name=models.CharField(max_length=20)
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Email_Id=models.EmailField()
    Phone_Number=models.IntegerField()
    password=models.CharField(max_length=20)
    Con_Password=models.CharField(max_length=20)
