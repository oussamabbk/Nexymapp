from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet,DoctorViewSet,PatientViewSet,authentification,patient_CliniqueViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'User', UserViewSet, basename='User')
Doctor_router = routers.SimpleRouter()
Doctor_router.register(r'Doctor', DoctorViewSet, basename='Doctor')
Doctor_patient = routers.SimpleRouter()
Doctor_patient.register(r'Patient', PatientViewSet, basename='patient')
patient_Clinique =routers.SimpleRouter()
patient_Clinique.register(r'patient_Clinique',patient_CliniqueViewSet,basename='patient_Clinique')
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(Doctor_router.urls)),
    path('', include(Doctor_patient.urls)),
    path('',include(patient_Clinique.urls)),
    path('authentification', authentification),


]