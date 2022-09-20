
from django.db import models
from django.contrib.auth.models import User
    
class CreateTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pass