from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo = models.ImageField(upload_to='photos')
    bio = models.TextField(max_length=100)
    contact = models.EmailField(max_length=20)
    link = models.URLField()
   
class Project(models.Model):
    title = models.TextField(max_length=10)
    image = models.ImageField(upload_to='photos')
    description = models.TextField(max_length=50)
    link  = models.URLField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=True)



