from rest_framework import serializers
from User.models import User
from User.models import Doctor,Patient,patient_Clinique
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Nom', 'Prenom', 'mobile', 'picture', 'Email','password','datedenaisance','adresse','description','sexe','statue']

class patient_cliniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_Clinique
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'Nom', 'Prenom', 'mobile', 'picture', 'Email','password','datedenaisance','adresse','description','sexe','statue','Desination','specialite']
class PatientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Patient
        fields = ['id', 'Nom', 'Prenom', 'mobile', 'picture', 'Email','password','datedenaisance','adresse','description','sexe','statue','identifiant','identifiantClinique','Groupesanguin','maladiechronique']
class patient_cliniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = patient_Clinique
        fields = "__all__"