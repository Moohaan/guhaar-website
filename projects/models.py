from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    date_started = models.DateTimeField('date started', null=True)
    image = CloudinaryField('image')
    description = models.TextField()
    """docstring for project."""
    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=300, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    """docstring for Video."""
    def __str__(self):
        return self.title

class Story(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=500)
    date_started = models.DateTimeField(default=None)
    author = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_started']


class Interview(models.Model):
    title = models.CharField(max_length=500, blank=False)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title
