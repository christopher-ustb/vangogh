from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from photo.serializers import PhotoSerializer
from photo.models import Photo
from vangogh import settings
import os


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(detail=False, methods=['get'])
    def scan_dir(self, request):
        picture_dir = os.path.join(settings.PHOTO_BASIC_DIR, "Douban")
        files = os.listdir(picture_dir)
        for f in files:
            statinfo = os.stat(os.path.join(picture_dir, f))
            photo_path = "Douban/" + f
            if Photo.objects.filter(path=photo_path).count() == 0:
                photo = Photo(path=photo_path)
                photo.save()
            print(statinfo.st_size)
        return Response({'status': 'scan'})


def save_disk_photo_to_db(photo_path):
    photo = Photo(path=photo_path)
    # TODO generate thumbnail, read exif
    photo.save()
    return photo
