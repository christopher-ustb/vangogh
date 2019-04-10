import os

import face_recognition
import numpy as np
from PIL import Image
from django.db import models
from django.utils import timezone

from photo.models import Photo
from vangogh import utils
from vangogh.utils import logger


class Person(models.Model):
    name = models.CharField(max_length=128, blank=False)
    mean_face_encoding = models.TextField()
    gmt_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "person"

    @staticmethod
    def select_by_encoding(face_encoding):
        same_people = []
        all_people = Person.objects.all()
        face_encoding_num_list = [p.get_mean_face_encoding_array() for p in all_people]
        compare_result = face_recognition.compare_faces(face_encoding_num_list, face_encoding)
        for idx, r in enumerate(compare_result):
            if r:
                same_people.append(all_people[idx])
        return same_people

    def get_mean_face_encoding_array(self):
        return [float(ecd) for ecd in self.mean_face_encoding.split(",")]

    def update_mean_when_found_new_face(self, face_encoding):
        """
        当发现人物的新的面孔时，更新平均encoding向量
        :param face_encoding: 新面孔encoding
        :return: self
        """
        count_faces_of_same_person = Face.objects.filter(person=self).count()
        encoding_arr = self.get_mean_face_encoding_array()
        new_encoding_arr = (
                                   np.array(encoding_arr) * count_faces_of_same_person + np.array(face_encoding)
                           ) / (count_faces_of_same_person + 1)
        self.mean_face_encoding = ",".join(map(str, new_encoding_arr))
        return self


class Face(models.Model):
    photo = models.ForeignKey(Photo, related_name='faces', on_delete=False, blank=False, null=True)
    person = models.ForeignKey(Person, on_delete=False, related_name='faces', blank=True, null=True)
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

    @staticmethod
    def build_faces_from_photo(photo):
        """
        从照片中发现face，并构造出face列表
        :param photo: photo model instance
        :return: face列表
        """
        faces = []
        photo_path = utils.server_url_to_absolute_path(photo.path)
        fc_image_file = face_recognition.load_image_file(photo_path)
        face_locations = face_recognition.face_locations(fc_image_file)
        # (top, right, bottom, left)
        face_encodings = face_recognition.face_encodings(fc_image_file)
        if len(face_locations) > 0:
            logger.info("locate face %s on photo %s" % (face_locations, photo.path))
            for face_location, face_encoding in zip(face_locations, face_encodings):
                face = Face(
                    photo=photo,
                    location_top=face_location[0],
                    location_bottom=face_location[2],
                    location_left=face_location[3],
                    location_right=face_location[1],
                    encoding=",".join(map(str, face_encoding))
                )
                same_people = Person.select_by_encoding(face_encoding)
                if len(same_people) == 0:
                    person = Person(name="unknown", mean_face_encoding=",".join(map(str, face_encoding)))
                    logger.info("found new person on photo %s" % photo.path)
                    person.save()
                    face.person = person
                else:
                    face.person = same_people[0]
                    face.person.update_mean_when_found_new_face(face_encoding)

                face.save()
                # TODO 根据person保存文件名，减少这次save()
                face._generate_face_image()
                face.save()
                faces.append(face)

    def _generate_face_image(self):
        photo_path = utils.server_url_to_absolute_path(self.photo.path)
        _, img_ext = os.path.splitext(photo_path)
        img = Image.open(photo_path)
        # left, upper, right, lower
        face_crop_box = (self.location_left, self.location_top, self.location_right, self.location_bottom)
        img = img.crop(face_crop_box)
        self.image_path = "/.face/%s%s" % (self.id, img_ext)
        face_image_file_path = utils.server_url_to_absolute_path(self.image_path)
        os.makedirs(os.path.dirname(face_image_file_path), exist_ok=True)
        img.save(face_image_file_path)
        logger.info("crop face image %s from photo %s" % (self.image_path, self.photo.path))
        return self
