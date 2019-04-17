import os

from PIL import Image
from django.db import models
from django.utils import timezone

from photo import photo_meta
from baidumap import webservices as baidumap_webservices
from vangogh import utils


class Photo(models.Model):
    path = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=256, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    datetime_original = models.DateTimeField(blank=True, null=True)
    image_hash = models.CharField(max_length=128, blank=True, null=True)
    gps_longitudes = models.FloatField(blank=True, null=True)
    gps_latitudes = models.FloatField(blank=True, null=True)
    addr_country = models.CharField(max_length=64, blank=True, null=True)
    addr_province = models.CharField(max_length=64, blank=True, null=True)
    addr_city = models.CharField(max_length=64, blank=True, null=True)
    addr_district = models.CharField(max_length=64, blank=True, null=True)
    addr_town = models.CharField(max_length=64, blank=True, null=True)
    addr_street = models.CharField(max_length=64, blank=True, null=True)
    addr_text = models.CharField(max_length=256, blank=True, null=True)
    gmt_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "photo"

    @staticmethod
    def build_from_path(photo_path):
        photo = Photo(
            path=utils.absolute_path_to_server_url(photo_path)
        )._generate_thumbnail()._set_file_size()._read_exif()
        photo.save()
        photo._add_to_place_album()
        return photo

    def _generate_thumbnail(self):
        if self.path is None:
            pass
        file = utils.server_url_to_absolute_path(self.path)
        img = Image.open(file)
        self.width, self.height = img.size
        # TODO thumbnail big/middle/small
        img.thumbnail(size=(1024, 1024))
        self.thumbnail = "/.thumbnail%s" % self.path
        thumbnail_path = utils.server_url_to_absolute_path(self.thumbnail)
        os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
        img.save(thumbnail_path)
        return self

    def _set_file_size(self):
        if self.path is None:
            pass
        file = utils.server_url_to_absolute_path(self.path)
        stat_info = os.stat(file)
        self.file_size = stat_info.st_size
        return self

    def _read_exif(self):
        """
        从照片exif中读取时间、gps，并通过百度地图api解析为地址
        :return: self
        """
        if self.path is None or self.path.endswith("png"):
            return self
        file = utils.server_url_to_absolute_path(self.path)
        lb_exif = photo_meta.get_labeled_exif(file)
        self.datetime_original = photo_meta.get_datetime(lb_exif)
        degrees = photo_meta.get_gps_in_float_degree(lb_exif)
        if degrees is not None:
            self.gps_longitudes, self.gps_latitudes = degrees
            addr = baidumap_webservices.geo_coding(degrees[::-1])
            if addr is not None:
                addr_component = addr.get("addressComponent")
                self.addr_country = addr_component.get("country")
                self.addr_province = addr_component.get("province")
                self.addr_city = addr_component.get("city")
                self.addr_district = addr_component.get("district")
                self.addr_town = addr_component.get("town")
                self.addr_street = addr_component.get("street")
                self.addr_text = addr.get("formatted_address")
        return self

    def _add_to_place_album(self):
        """
        将照片自动放入对应的地点相册，国内按市分组，国外按国家分组
        """
        if self.addr_text is not None:
            if self.addr_country == "中国":
                album_addr_key = self.addr_city
                addr_level = 3
            else:
                album_addr_key = self.addr_country
                addr_level = 1

            from album.models import Album

            place_albums = Album.objects.filter(type="A", addr_name=album_addr_key)
            if len(place_albums) == 0:
                album = Album(title=album_addr_key, auto=True, type="A", addr_name=album_addr_key,
                              addr_level=addr_level)
                album.save()
            else:
                album = place_albums[0]
            album.photos.add(self)
            album.save()
