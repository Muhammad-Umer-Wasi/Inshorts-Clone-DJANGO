from django.db import models

class TaskModel(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    timestamp= models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    publisher= models.CharField(max_length=400)


    

