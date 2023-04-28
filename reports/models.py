from django.db import models
from user.models import Person

# Create your models here.
class Report(models.Model):
    name= models.CharField(max_length=120)
    image= models.ImageField(upload_to='reports', blank=True)
    remarks= models.TextField()
    author= models.ForeignKey(Person, on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)