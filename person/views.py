from rest_framework import viewsets

from person.models import Person, Face
from person.serializers import PersonSerializer, FaceSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by("-face_count")
    serializer_class = PersonSerializer


class PersonFaceViewSet(viewsets.ModelViewSet):
    serializer_class = FaceSerializer

    def get_queryset(self):
        person_id = self.kwargs["person_id"]
        return Face.objects.filter(person=person_id).order_by("-gmt_created")


class FaceViewSet(viewsets.ModelViewSet):
    queryset = Face.objects.all().order_by("-gmt_created")
    serializer_class = FaceSerializer
