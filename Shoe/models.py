from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shoes/')
    Catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE, related_name='catagory')
    
    def __str__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name