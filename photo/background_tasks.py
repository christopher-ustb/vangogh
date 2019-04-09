import os
import time

import face_recognition
from PIL import Image

from photo import photo_meta
from vangogh import settings
from vangogh.utils import logger


def record_photo(file):
    from photo.models import Photo

    basic_dir_length = len(settings.PHOTO_BASIC_DIR)
    sub_path = file[basic_dir_length:].replace("\\", "/")
    if Photo.objects.filter(path=sub_path).count() == 0:
        photo = Photo(path=sub_path)

        img = Image.open(file)
        # TODO thumbnail big/middle/small
        img.thumbnail(size=(1024, 1024))
        thumbnail_path = os.path.join(settings.PHOTO_BASIC_DIR, ".thumbnail", file[basic_dir_length + 1:])
        os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
        img.save(thumbnail_path, "JPEG")
        photo.thumbnail = "/.thumbnail%s" % sub_path

        stat_info = os.stat(file)
        photo.file_size = stat_info.st_size

        lb_exif = photo_meta.get_labeled_exif(file)
        photo.datetime_original = photo_meta.get_datetime(lb_exif)

        fc_image_file = face_recognition.load_image_file(file)
        face_locations = face_recognition.face_locations(fc_image_file)
        logger.info("recognize face locations: %s" % face_locations)
        face_encodings = face_recognition.face_encodings(fc_image_file)

        photo.save()
        logger.info("record photo: %s" % sub_path)


def scan_dir_to_record():
    while True:
        logger.info("start to scan disk: %s" % settings.PHOTO_BASIC_DIR)
        for root, directories, filenames in os.walk(settings.PHOTO_BASIC_DIR):
            if ".thumbnail" not in os.path.basename(root):
                for filename in filenames:
                    file = os.path.join(root, filename)
                    record_photo(file)
        logger.info("end to scan disk. sleep 60s")
        time.sleep(60)
