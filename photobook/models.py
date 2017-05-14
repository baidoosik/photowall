from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(TimeStamp):
    title = models.CharField(max_length=100,default='photo')
    category= models.CharField(max_length=100,
        choices = (
            ('미국','미국' ),
            ('은지', '은지'),
            ('졸업식', '졸업식'),
        ),default=False)
    story = models.CharField(max_length=200)
    photo = models.ImageField()

    def __str__(self):
        return self.title