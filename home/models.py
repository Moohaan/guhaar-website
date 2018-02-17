from django.db import models

# Create your models here.
class SubscriberManager(models.Manager):
    def create_subscriber(self, email, name=None):
        subscriber = None
        if self.filter(email=email):
            return False
        else:
            subscriber = self.create(name=name , email=email)
            return subscriber

class Subscriber(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)

    objects = SubscriberManager()
    def __str__(self):
        return '{} < {} >'.format(self.name, self.email)

    # def
