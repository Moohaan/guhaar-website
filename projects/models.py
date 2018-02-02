from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    # project_short_description = models.CharField(max_length=100, null=True)
    # image = models.ImageField(upload_to='images/projects/', default=None)
    image = CloudinaryField('image')
    date_started = models.DateTimeField('date started', null=True)
    description = models.CharField(max_length = 2000)
    """docstring for project."""
    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    url = models.CharField(max_length=300, unique=True)
    """docstring for Video."""
    def __str__(self):
        return self.title

class Story(models.Model):
    title = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='images/stories/', default=None)
    image = CloudinaryField('image')
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    date_started = models.DateTimeField(default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_started']


class Interview(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title
