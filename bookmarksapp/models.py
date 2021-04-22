from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class BookMark(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField(max_length=2000, null=True)
    url = models.URLField(max_length=200)
    tags = TaggableManager()

    def __str__(self):
        return self.name