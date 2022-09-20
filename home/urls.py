from django.urls import path
from home import views

urlpatterns = [
    path('',views.home),
    path('create_task',views.add_task,name='create_task'),


]
