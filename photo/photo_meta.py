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
    if exif is not None:
        for (key, val) in exif.items():
            if 0x8825 == key:
                labeled_gps = {}
                for gpsk, gpsv in val.items():
                    labeled_gps[GPSTAGS.get(gpsk)] = gpsv
                val = labeled_gps
            labeled[TAGS.get(key)] = val

    return labeled


def get_datetime(labeled_exif):
    dt = labeled_exif.get("DateTimeOriginal")
    if dt is not None:
        return datetime.strptime(dt, "%Y:%m:%d %H:%M:%S")


def _convert_degree_minute_second_to_float(degree_minute_second):
    """
    将度分秒的二维数组位置，转换为小数的度数
    :param degree_minute_second: ((31, 1), (11, 1), (347208, 10000))
    :return: 31.194890
    """
    d = degree_minute_second[0][0] / degree_minute_second[0][1]
    m = degree_minute_second[1][0] / degree_minute_second[1][1]
    s = degree_minute_second[2][0] / degree_minute_second[2][1]
    return d + (m / 60) + (s / 3600)


def get_gps_in_float_degree(labeled_exif):
    gps = labeled_exif.get("GPSInfo")
    if gps is not None and "GPSLatitude" in gps and "GPSLongitude" in gps:
        latitude_degree = _convert_degree_minute_second_to_float(gps.get("GPSLatitude"))
        longitude_degree = _convert_degree_minute_second_to_float(gps.get("GPSLongitude"))
        return longitude_degree, latitude_degree
