import os
import time

from vangogh import settings
from vangogh.utils import logger


def record_photo(file):
    from photo.models import Photo

    basic_dir_length = len(settings.PHOTO_BASIC_DIR)
    sub_path = file[basic_dir_length:].replace("\\", "/")
    if Photo.objects.filter(path=sub_path).count() == 0:
        photo = Photo(path=sub_path)
        photo.save()
        logger.info("record photo: %s" % file)
    else:
        logger.info("photo %s has been recorded" % file)


def scan_dir_to_record():
    while True:
        logger.info("start to scan disk: %s" % settings.PHOTO_BASIC_DIR)
        for root, directories, filenames in os.walk(settings.PHOTO_BASIC_DIR):
            for filename in filenames:
                file = os.path.join(root, filename)
                record_photo(file)
        logger.info("end to scan disk. sleep 60s")
        time.sleep(60)
