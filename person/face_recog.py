import face_recognition

from PIL import Image


def locate_face(photo_file):
    """

    :param photo_file:
    :return: (top, right, bottom, left)
    """
    fc_image_file = face_recognition.load_image_file(photo_file)
    face_locations = face_recognition.face_locations(fc_image_file)
    # logger.info("recognize face locations: %s" % face_locations)
    face_encodings = face_recognition.face_encodings(fc_image_file)
    print(face_locations[0])
    return face_locations


def crop_face(photo_file, face_location):
    face_crop_box = (face_location[3], face_location[0], face_location[1], face_location[2])
    img = Image.open(photo_file)
    print(img.size)
    # left, upper, right, lower
    img.crop(face_crop_box).save("D://tmp//face.jpg", "JPEG")


if __name__ == "__main__":
    file = "D:\\xiaofu\\pictures\\知乎\\0e67e4b99c2c4028a7bfc9c7dabe5152_r.jpg"
    crop_face(file, locate_face(file)[0])
