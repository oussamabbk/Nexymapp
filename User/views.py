from rest_framework import viewsets
from User.models import User,Doctor
from User.serializers import UserSerializer,DoctorSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer


    def get_queryset(self):
        return User.objects.all()


class DoctorViewSet(viewsets.ModelViewSet):

    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.all()



