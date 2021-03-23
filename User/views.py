from rest_framework import viewsets, request
from User.models import User,Doctor,Patient,patient_Clinique
from User.serializers import UserSerializer,DoctorSerializer,PatientSerializer,patient_cliniqueSerializer
from  django.http import HttpResponse
import json

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer


    def get_queryset(self):
        return User.objects.all()


class DoctorViewSet(viewsets.ModelViewSet):

    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.all()


class PatientViewSet(viewsets.ModelViewSet):

    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.all()


class patient_CliniqueViewSet(viewsets.ModelViewSet):
    serializer_class = patient_cliniqueSerializer
    def get_queryset(self):
        return patient_Clinique.objects.all()


def authentification(request):
    response=json.dumps([{}])
    return HttpResponse(response,content_type='text/json')


