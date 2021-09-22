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
    title = models.TextField(max_length=50)
    image = models.ImageField(upload_to='photos')
    description = models.TextField(max_length=200)
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
    rating=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),)
    design=models.IntegerField(choices=rating, default=0, blank=True)
    usability=models.IntegerField(choices=rating, blank=True)
    content=models.IntegerField(choices=rating, blank=True)
    design_average=models.FloatField(default=0, blank=True)
    usability_average=models.FloatField(default=0, blank=True)
    content_average=models.FloatField(default=0, blank=True)
    score=models.FloatField(default=0, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project=models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rate.objects.filter(project_id=id).all()
        return ratings(len(ratings) == 1)

    def __str__(self):
        return f'{self.project} Rating'
   

        









