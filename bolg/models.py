from django.contrib.gis.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    author = models.ForeignKey(User, related_name='related_postwriter')
    title = models.CharField(max_length=200, blank = False)
    text = models.TextField(blank = True)
    image = models.ImageField(null = False, blank = True, upload_to='images')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
        )
    created_date = models.DateTimeField(
        default=timezone.now
        )
    point = models.PointField(blank=True, null=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.title
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    # Returns the string representation of the model.


class Comment(models.Model):
    post = models.ForeignKey('bolg.Post', related_name='related_comments')
    author = models.ForeignKey(User, related_name='related_commentwriter')
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
