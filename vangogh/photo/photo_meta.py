from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime


def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()


def get_labeled_exif(filename):
    """
    读取exif信息，并翻译为可读的label名
    :param filename: 文件名
    :return: dict
    """
    exif = get_exif(filename)
    labeled = {}
    for (key, val) in exif.items():
        if 0x8825 == key:
            labeled_gps = {}
            for gpsk, gpsv in val.items():
                labeled_gps[GPSTAGS.get(gpsk)] = gpsv
            val = labeled_gps
        labeled[TAGS.get(key)] = val

    return labeled


def get_datetime(labeled_exif):
    dt = labeled_exif["DateTimeOriginal"]
    return datetime.strptime(dt, "%Y:%m:%d %H:%M:%S")


if __name__ == "__main__":
    l_exif = get_labeled_exif("D:\\xiaofu\\pictures\\相机照片\\IMG_20181026_112720.jpg")
    for k, v in l_exif.items():
        print(k, v)
    print(get_datetime(l_exif))
