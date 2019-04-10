import os

from django.db import models

from django.utils import timezone

from photo import photo_meta
from vangogh import utils
from PIL import Image


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

    @staticmethod
    def build_from_path(photo_path):
        return Photo(
            path=utils.absolute_path_to_server_url(photo_path)
        )._generate_thumbnail()._set_file_size()._read_exif()

    def _generate_thumbnail(self):
        if self.path is None:
            pass
        file = utils.server_url_to_absolute_path(self.path)
        img = Image.open(file)
        # TODO thumbnail big/middle/small
        img.thumbnail(size=(1024, 1024))
        self.thumbnail = "/.thumbnail%s" % self.path
        thumbnail_path = utils.server_url_to_absolute_path(self.thumbnail)
        os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
        img.save(thumbnail_path, "JPEG")
        return self

    def _set_file_size(self):
        if self.path is None:
            pass
        file = utils.server_url_to_absolute_path(self.path)
        stat_info = os.stat(file)
        self.file_size = stat_info.st_size
        return self

    def _read_exif(self):
        if self.path is None:
            pass
        file = utils.server_url_to_absolute_path(self.path)
        lb_exif = photo_meta.get_labeled_exif(file)
        self.datetime_original = photo_meta.get_datetime(lb_exif)
        return self
