from rest_framework import viewsets

from album.models import Album
from album.serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by("-gmt_created")
    serializer_class = AlbumSerializer
