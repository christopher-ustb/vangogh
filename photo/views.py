from rest_framework import viewsets
from photo.serializers import PhotoSerializer
from photo.models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
