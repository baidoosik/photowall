from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(TimeStamp):
    title = models.CharField(max_length=100,default=None)
    category= models.CharField(max_length=100,
        choices = (
            ('글로벌 챌린지','글로벌 챌린지' ),
            ('은지', '은지'),
            ('바르셀로나mwc', '바르셀로나mwc'),
            ('인도네시아 코이카 탐방','인도네시아 코이카 탐방'),
        ),default=False)
    story = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='blog/%Y/%M/%D')

    def __str__(self):
        return self.title