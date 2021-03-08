from rest_framework import viewsets
from User.models import User,Doctor,Patient
from User.serializers import UserSerializer,DoctorSerializer,PatientSerializer

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



