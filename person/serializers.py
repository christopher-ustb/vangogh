from rest_framework import serializers

from person.models import Person, Face


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ('mean_face_encoding',)


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        exclude = ('encoding',)
