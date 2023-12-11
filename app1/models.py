from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    
class Products(models.Model):
    name=models.CharField(max_length=225)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)
