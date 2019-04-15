from rest_framework import serializers
from photo.models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        exclude = ('image_hash', )
