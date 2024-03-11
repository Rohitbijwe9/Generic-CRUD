from django.db import models

class Studet(models.Model):
    roll=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50)
    add=models.CharField(max_length=50)
    email=models.EmailField()
    