from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=200)
    # project_short_description = models.CharField(max_length=100, null=True)
    project_description = models.CharField(max_length = 2000)
    project_img = models.ImageField(upload_to='images/projects/', default=None)
    start_date_project = models.DateTimeField('date started', null=True)
    """docstring for project."""
    def __str__(self):
        return self.project_title


class Video(models.Model):
    video_title = models.CharField(max_length=200, blank=True)
    video_description = models.CharField(max_length=1000, blank=True)
    video_from_project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    video_youtube_url = models.CharField(max_length=300, unique=True)
    """docstring for Video."""
    def __str__(self):
        return self.video_title

class Story(models.Model):
    story_title = models.CharField(max_length=200)
    story_img = models.ImageField(upload_to='images/stories/', default=None)
    story_person = models.CharField(max_length=100)
    story_description = models.CharField(max_length=2000)
    story_from_project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    date_started = models.DateTimeField(default=None)

    def __str__(self):
        return self.story_title

    class Meta:
        ordering = ['-date_started']


class Interview(models.Model):
    interview_person = models.CharField(max_length=100, blank=True)
    interview_description = models.CharField(max_length=2000, blank=True)
    interview_from_project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.interview_person
