from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Team(models.Model):
    number_of_people = models.IntegerField()
    short_description = models.CharField(max_length=100,default=None)
    description = models.TextField()

    def __str__(self):
        return self.short_description

class Member(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    short_description = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
