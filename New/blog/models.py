from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    author = models.ForeignKey(User, related_name='related_postwriter')
    text = models.TextField(blank = False)
    image = models.ImageField(null = False, blank = False, upload_to='images')
    created_date = models.DateTimeField(
        default=timezone.now
        )

    def __str__(self):              # __unicode__ on Python 2
        return self.text
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    # Returns the string representation of the model.