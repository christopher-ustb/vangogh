from django_filters import rest_framework as filters
from rest_framework import viewsets

from album.models import Album
from photo.models import Photo
from photo.serializers import PhotoSerializer


class PhotoFilter(filters.FilterSet):
    datetime_original = filters.DateTimeFromToRangeFilter(field_name="datetime_original")

    class Meta:
        model = Photo
        exclude = ["image_hash", "gps_longitudes", "gps_latitudes", "gmt_created"]


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by("-datetime_original", "-gmt_created")
    serializer_class = PhotoSerializer
    filterset_class = PhotoFilter


class AlbumPhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        album_id = self.kwargs['album_id']
        return Album.objects.get(id=album_id).photos.all().order_by("-datetime_original", "-gmt_created")
