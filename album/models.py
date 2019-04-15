from django.db import models
from django.utils import timezone

from photo.models import Photo


class Album(models.Model):
    TYPE_CHOICES = (
        ('P', 'people'),
        ('A', 'address'),
        ('U', 'user customize create')
    )

    ADDRESS_LEVEL_CHOICES = (
        (1, 'country'),
        (2, 'province'),
        (3, 'city'),
        (4, 'district')
    )

    title = models.CharField(max_length=512, db_index=True)
    photos = models.ManyToManyField(Photo)
    auto = models.BooleanField(default=False)
    type = models.CharField(choices=TYPE_CHOICES, max_length=2)
    addr_name = models.CharField(max_length=64, blank=True, null=True)
    addr_level = models.IntegerField(choices=ADDRESS_LEVEL_CHOICES, blank=True, null=True)
    cover_photos = models.ManyToManyField(Photo, related_name='album_cover_photos')
    gmt_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "album"
