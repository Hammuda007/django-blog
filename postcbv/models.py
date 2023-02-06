from django.db import models

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=10000)
    image=models.ImageField(upload_to='posts/')
   


    def __str__(self):
        return self.title
