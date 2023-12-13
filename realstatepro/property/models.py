
# Create your models here.
# property/models.py

from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=100)
    features = models.TextField()

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)

    TYPE_CHOICES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    ]
    unit_type = models.CharField(max_length=4, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.unit_type} in {self.property.name}"
