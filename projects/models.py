from django.db import models
from cloudinary.models import CloudinaryField
# from ckeditor.fields import RichTextUploadingField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    date_started = models.DateTimeField('date started', null=True)
    image = CloudinaryField('image')
    # description = models.TextField()
    description = RichTextUploadingField()
    """docstring for project."""
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_started']


class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=None)
    # description = models.CharField(max_length=1000, blank=True)
    description = RichTextUploadingField()
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
    description = RichTextUploadingField()
    obj_type = "story"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Interview(models.Model):
    title = models.CharField(max_length=500, blank=False)
    date_created = models.DateTimeField(default=None)
    description = RichTextUploadingField()
    url = models.CharField(null=True, blank=True, max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    obj_type = "interview"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
