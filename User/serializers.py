from rest_framework import serializers
from User.models import User
from User.models import Doctor,Patient,patient_Clinique
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
class PatientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Patient
        fields = "__all__"
class patient_cliniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = patient_Clinique
        fields = "__all__"