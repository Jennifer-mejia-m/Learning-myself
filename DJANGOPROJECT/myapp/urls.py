from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/<int:id>', views.about, name='about'), #es necesario poner el name='about'?
    path('hello/<str:username>', views.hello),
    path('projects', views.projects),
    path('tasks/<int:id>', views.tasks),
    path('aboutt', views.aboutt),
]