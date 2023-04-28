from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField(default='write your bio....')
    profile_picture= models.ImageField(upload_to='user', default= 'no_profile.png')
    email= models.EmailField(max_length=100)
    created= models.DateTimeField(auto_now_add=True, null=True)
    updated= models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username}"
    
