from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    
    def __self__(self):
        return self.brand
    
    @property
    def sale_price(self):
        if self.brand == "Samsung":
            return "%.2f" %(float(self.price) * 0.95)
        
        elif self.brand == "Apple" or self.brand == "Google":
            return "%.2f" %(float(self.price) * 0.94)
        
        elif self.brand == "Nothing":
            if self.model == "Phone(2)":
                return "%.2f" %(float(self.price) * 0.95)
            else:
                return None
        
        else:
            return "%.2f" %(float(self.price) * 0.90)
    
    def get_discount(self):
        if self.brand == "Samsung":
            return "Flat 5% OFF"
        
        elif self.brand == "Apple" or self.brand == "Google":
            return "Flat 6% OFF"
        
        elif self.brand == "Nothing":
            if self.model == "Phone(2)":
                return "Flat 5% OFF"
            else:
                return "No OFFer"
        else:
            return "Flat 10% OFF"
    
    def availability(self):
        if self.sale_price != self.price:
            return "YES"
        else:
            return "NO"