from django.db import models

# Create your models here.
class Farmer(models.Model):
    name= models.CharField(max_length=120)
    logo= models.ImageField(upload_to='base', default='no_picture.png')

    def __str__(self):
        return str( self.name)

