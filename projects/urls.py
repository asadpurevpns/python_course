from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),

    path('create/', views.createProject, name="create"),
    path('update/<str:pk>/', views.updateProject, name='update'),
    path('delete/<str:pk>/', views.deleteProject, name='delete')
]