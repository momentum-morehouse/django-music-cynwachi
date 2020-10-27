from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    year_released = models.IntegerField()
    genre = models.CharField(max_length=30)
    mood = models.CharField(max_length=30)
 
    def __str__(self):
      return self.text
    
    
class Cover(models.Model):
    cover = models.ImageField()
    
    def __str__(self):
      return self.image 