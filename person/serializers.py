from rest_framework import serializers

from person.models import Person, Face


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'gmt_created')


class FaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Face
        fields = ('image_path', 'gmt_created')
