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

    class Meta:
        ordering = ['-date_started']


class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=None)
    description = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=300, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    obj_type = "video"
    """docstring for Video."""
    def __str__(self):
        return self.title

class Story(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=None)
    author = models.CharField(max_length=200)
    image = CloudinaryField('image')
    # image2 = CloudinaryField('image')
    # image3 = CloudinaryField('image')
    # image4 = CloudinaryField('image')
    description = models.TextField()
    obj_type = "story"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Interview(models.Model):
    title = models.CharField(max_length=500, blank=False)
    date_created = models.DateTimeField(default=None)
    description = models.TextField()
    url = models.CharField(null=True, blank=True, max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    obj_type = "interview"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
