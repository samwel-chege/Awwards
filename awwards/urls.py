from django.urls import path
import rest_framework
from .import views
from django.conf import settings 
from django.conf.urls.static import static
# from rest_framework import routers
# from .api import ProjectViewSet

#create an instance of the router
# router = routers.DefaultRouter()
# router.register('/api/awwards', ProjectViewSet,'awwards')


urlpatterns = [
    path('', views.home,name='home'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
    path('upload/project/',views.uploadproject,name='uploadproject'),
    path('profile/',views.profile,name = 'profile'),
    path(r'^search/', views.search_projects, name='search_projects'),
    path('rate/(?P<project>\d+)',views.rate,name='rate'),

 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
