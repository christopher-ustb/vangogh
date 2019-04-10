from rest_framework import viewsets

from person.models import Person, Face
from person.serializers import PersonSerializer, FaceSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by("-gmt_created")
    serializer_class = PersonSerializer


class FaceViewSet(viewsets.ModelViewSet):
    queryset = Face.objects.all().order_by("-gmt_created")
    serializer_class = FaceSerializer
