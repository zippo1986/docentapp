from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    cantidad =models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    
    