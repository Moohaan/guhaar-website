from django.db import models

# Create your models here.
class Team(models.Model):
    number_of_people = models.IntegerField()
    short_description = models.CharField(max_length=100,default=None)
    description = models.TextField()

class Member(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/members',default=None)
    short_description = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
