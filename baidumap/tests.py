from django.test import TestCase

from baidumap import webservices


class WevServicesTests(TestCase):

    def test_geo_coding(self):
        locations = (35.658651, 139.745415)
        coding_result = webservices.geo_coding(locations)
        print(coding_result)
        self.assertTrue(coding_result)
