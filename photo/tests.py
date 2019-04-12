from django.test import TestCase

from photo.models import Photo


class PhotoModelTests(TestCase):

    def test_read_exif(self):
        """
        测试exif读取，需要准备一张含有exif的照片
        :return: None
        """
        photo = Photo(path="/IMG_20181202_084309.jpg")
        photo._read_exif()
        print("datetime_original:", photo.datetime_original)
        print("gps:", photo.gps_longitudes, photo.gps_latitudes)
        self.assertIsNotNone(photo.datetime_original)
        self.assertIsNotNone(photo.gps_longitudes)
        self.assertIsNotNone(photo.addr_text)
