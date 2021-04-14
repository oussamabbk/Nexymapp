from django.core.serializers import serialize
from rest_framework import viewsets, request
from User.models import User, Doctor, Patient, patient_Clinique
from User.serializers import UserSerializer, DoctorSerializer, PatientSerializer, patient_cliniqueSerializer
from django.http import HttpResponse
import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


def getPatientOfMedecin(request, id):
    response = json.dumps([{}])
    ListeIdClient = patient_Clinique.objects.filter(Doctor=id)
    users_list = list()

    for patId in ListeIdClient:
        print(patId.Patient.id)
        Pat = Patient.objects.filter(id=patId.Patient.id)
        print(Pat)
        users_list.append(Pat)

    return HttpResponse(users_list, content_type='text/json')
@api_view(['POST'])
def PostPatient(request,iddoctor,idPatient):
    if request.method == 'POST':
        Doc = Doctor.objects.get(id=iddoctor)
        print(Doc)
        patient = Patient.objects.get(id=idPatient)
        Doc.Patients.add(patient)
        Doc.save()
        serialize=DoctorSerializer(Doc,many=True)
        return Response("Doc")

@api_view(['GET'])
def PatientMedecin(request,idPatient):
    if request.method == 'GET':
        Doc = Doctor.objects.filter(Patients__id=idPatient)




        serialize=DoctorSerializer(Doc,many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
@api_view(['GET'])
def MedecinPatient(request,iddoctor):
    if request.method == 'GET':
        Doc = Doctor.objects.get(id=iddoctor)

        patients = Doc.Patients.all()


        serialize=PatientSerializer(patients,many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
@api_view(['DELETE'])
def DeletepatienfromMedecin(request,idDoctor,idPatient):
    patient = Patient.objects.get(id=idPatient)
    Doc = Doctor.objects.get(id=idDoctor)
    Doc.Patients.remove(patient)
    return Response("Deleted")
@api_view(['GET'])
def countPatient(request):
    numb=Patient.objects.count()
    print(numb)
    return Response(numb)
@api_view(['GET'])
def countDoctor(request):
    numb=Doctor.objects.count()
    print(numb)
    return Response(numb)