from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet,DoctorViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'User', UserViewSet, basename='User')
Doctor_router = routers.SimpleRouter()
Doctor_router.register(r'Doctor', DoctorViewSet, basename='Doctor')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(Doctor_router.urls)),

]