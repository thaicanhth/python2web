from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Post2(models.Model):
    title = models.CharField(max_length=100)
    subTitle = models.TextField(null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.URLField()
    images = models.ImageField(null=True)
    def __str__(self):
        return self.title
