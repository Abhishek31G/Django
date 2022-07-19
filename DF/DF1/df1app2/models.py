from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    read_date = models.DateField()

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=60)
    book = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name