from django.db import models
from django.utils import timezone
from products.models import Product
from user.models import Person
from base.models import Farmer
from .utils import genertate_code


class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"id:{self.product.name}, Quantity:{self.quantity}"


class Sales(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, default=None, null=True)
    customer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=None)
    salesman = models.ForeignKey(Person, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(blank=True, default=None)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = genertate_code()

        if self.created is None:
            self.created = timezone.now()

        return super().save(*args, **kwargs)


    def __str__(self):
        return f"sales for the amount of ksh {self.total_price}"
    
    def get_positions(self):
        return self.positions.all()
    
class CSV(models.Model):
    file_name= models.FileField(upload_to='csvs')
    activated= models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True, null=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
    


