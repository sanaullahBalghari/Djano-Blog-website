from django.db import models

from django.contrib.auth.models import AbstractUser
class user(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    Bio=models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='userimage/', default='images/default-avatar-profile-.webp')

class Rewive(models.Model):
    comment=models.TextField()

    user=models.ForeignKey(user,on_delete=models.CASCADE , related_name='commentuset')
    date=models.DateTimeField(auto_now=True)

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    
    author=models.ForeignKey(user,on_delete=models.CASCADE , related_name='authorname')
    date=models.DateTimeField(auto_now=True)
    comment=models.ManyToManyField(Rewive)

    def __str__(self):
        return self.title
    
