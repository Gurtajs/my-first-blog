from django.db import models
from django.urls import reverse

class Blog(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True) #the null=True means that the field can be left empty
    title = models.CharField(max_length=30)
    text_box = models.TextField()
    
    
    def __str__(self):
       return self.first_name + " " + self.last_name
 




