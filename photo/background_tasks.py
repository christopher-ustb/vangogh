import os
import time

from vangogh import settings, utils
from vangogh.utils import logger


def scan_dir_to_record():
    while True:
        logger.info("start to scan disk: %s" % settings.PHOTO_BASIC_DIR)
        for root, directories, filenames in os.walk(settings.PHOTO_BASIC_DIR):
            if ".thumbnail" not in os.path.basename(root):
                for filename in filenames:
                    file = os.path.join(root, filename)
                    sub_path = utils.absolute_path_to_server_url(file)

                    from photo.models import Photo

                    if Photo.objects.filter(path=sub_path).count() == 0:
                        photo = Photo.build_from_path(file)
                        photo.save()
                        # TODO 人脸识别：定位，裁剪，编码，持久化face，识别person

                        logger.info("record photo: %s" % sub_path)
        logger.info("end to scan disk. sleep %ss" % settings.PHOTO_SCAN_INTERVAL)
        time.sleep(settings.PHOTO_SCAN_INTERVAL)
