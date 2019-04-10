from django.db import models
from django.utils import timezone

from photo.models import Photo


class Person(models.Model):
    name = models.CharField(max_length=128, blank=False)
    mean_face_encoding = models.TextField()
    gmt_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "person"


class Face(models.Model):
    photo = models.ForeignKey(Photo, related_name='faces', on_delete=False, blank=False, null=True)
    person = models.ForeignKey(Person, on_delete=False, related_name='faces')
    image_path = models.CharField(max_length=256)
    person_label_is_inferred = models.NullBooleanField(db_index=True)
    person_label_probability = models.FloatField(default=0., db_index=True)
    location_top = models.IntegerField()
    location_bottom = models.IntegerField()
    location_left = models.IntegerField()
    location_right = models.IntegerField()
    encoding = models.TextField()
    gmt_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "face"
