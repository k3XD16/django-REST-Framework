from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    
    def __self__(self):
        return self.brand