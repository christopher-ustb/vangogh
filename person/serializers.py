from rest_framework import serializers

from person.models import Person, Face
from photo.serializers import PhotoSerializer


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ('mean_face_encoding',)


class FaceSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)

    class Meta:
        model = Face
        exclude = ('encoding',)
