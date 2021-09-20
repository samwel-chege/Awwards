from django.test import TestCase
from .models import Project,Profile,Rate
from django.contrib.auth.models import User
# Create your tests here.


class ProfileTestClass(TestCase):
    def setUp(self):
        self.samm = User(username = "samm", email = "samm@gmail.com",password = "1234221")
        self.profile = Profile(user= self.samm, photo='image.png',bio='bio', contact='samm@gmail', link='www.heroku.com')
        self.samm.save()
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.samm, User))
        self.assertTrue(isinstance(self.profile, Profile))

    


class ProjectTestClass(TestCase):
    def setUp(self):
        self.samm = User(username = "samm", email = "samm@gmail.com",password = "1234")
        self.profile = Profile(user= self.samm, profile_pic='mepng',bio='bio', contact='samm@gmail.com', link='www.heroku.com')
        self.project = Project(title= "pitches", image = "imageurl", description ="test project", link = "testlink", profile= self.profile)

        self.samm.save()
        self.profile.save_profile()
        self.project.save_project()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        projects = Project.objects.all()
        self.assertTrue(len(projects)> 0)

    def test_delete_project(self):
        projects1 = Project.objects.all()
        self.assertEqual(len(projects1),1)
        self.project.delete_project()
        projects2 = Project.objects.all()
        self.assertEqual(len(projects2),0)

    def test_display_projects(self):
        projects = Project.display_all_projects()
        self.assertTrue(len(projects) > 0 )

    def test_search_project(self):
        project = Project.search_project('test')
        self.assertEqual(len(project),1)

class RateTestClass(TestCase):
    def setUp(self):
        self.samm = User(username = "samm", email = "samm@gmail.com",password = "1234")
        self.profile = Profile(user= self.samm, profile_pic='mepng',bio='bio', contact='samm@gmail.com', link='www.heroku.com')
        self.project = Project(title= "pitches", image = "imageurl", description ="test project", link = "testlink", profile= self.profile)
        self.rate = Rate(project = self.project,design = 8,usability = 7,content = 9)

        self.samm.save()
        self.profile.save_profile()
        self.project.save_project()
        self.rate.save_rate()
        
    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()
        Rate.objects.all().delete()

    def test_instance(self):
        rates = Rate.objects.all()
        self.assertTrue(len(rates)>0) 

    def test_delete_rate(self):
          rates1 = Rate.objects.all()
          self.assertEqual(len(rates1),1)
          self.rate.delete_rate()
          rates2 = Rate.objects.all()
          self.assertEqual(len(rates2),0)     
    
