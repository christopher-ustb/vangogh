from django.db import models

from django.utils import timezone


class Photo(models.Model):
    path = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=256, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    datetime_original = models.DateTimeField(blank=True, null=True)
    image_hash = models.CharField(max_length=128, blank=True, null=True)
    gps_longitudes = models.FloatField(blank=True, null=True)
    gps_latitudes = models.FloatField(blank=True, null=True)
    gmt_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "photo"


class Person(models.Model):
    name = models.CharField(max_length=128, blank=False)
    mean_face_encoding = models.TextField()

    class Meta:
        db_table = "person"


class Face(models.Model):
    photo = models.ForeignKey(Photo, related_name='faces', on_delete=False, blank=False, null=True)
    person = models.ForeignKey(Person, on_delete=False, related_name='faces')
    name = models.CharField(max_length=64)
    location_top = models.IntegerField()
    location_bottom = models.IntegerField()
    location_left = models.IntegerField()
    location_right = models.IntegerField()
    encoding = models.TextField()

    class Meta:
        db_table = "face"
