from django.test import TestCase

from person.models import Face
from photo.models import Photo


class FaceModelTests(TestCase):

    def test_build_faces_from_photo(self):
        photo = Photo(path="/0e67e4b99c2c4028a7bfc9c7dabe5152_r.jpg")
        photo.save()
        face = Face.build_faces_from_photo(photo)
        self.assertIsNotNone(face)
