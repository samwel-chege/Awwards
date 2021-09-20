from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.dispatch import receiver
from django.db.models.signals  import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo = models.ImageField(upload_to='photos')
    bio = models.TextField(max_length=100)
    contact = models.EmailField(max_length=50)
    link = models.URLField()

    @receiver(post_save,sender = User)
    def update_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        try:
            instance.profile.save()
        except AttributeError:
            pass  


   
class Project(models.Model):
    title = models.TextField(max_length=10)
    image = models.ImageField(upload_to='photos')
    description = models.TextField(max_length=50)
    link  = models.URLField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def display_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)  

    @classmethod
    def search(cls,title):
        return Project.objects.filter(title__icontains = title)    

    class Meta:
        ordering = ['-create_date']     


class Rate(models.Model):
    design = models.FloatField(blank=True)
    usability = models.FloatField(blank=True)
    content = models.FloatField(blank=True)

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()
            






