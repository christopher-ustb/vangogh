from django.db import models


class Photo(models.Model):
    path = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=256, blank=True, null=True)
    datetime_original = models.DateTimeField(blank=True, null=True)
    image_hash = models.CharField(max_length=128, blank=True, null=True)
    gps_longitudes = models.FloatField(blank=True, null=True)
    gps_latitudes = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "photo"


class Face(models.Model):
    name = models.CharField(max_length=64)


class FaceInPhoto(models.Model):
    face = models.ForeignKey(Face, on_delete=False)
    photo = models.ForeignKey(Photo, on_delete=False)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
