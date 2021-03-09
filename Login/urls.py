from django.urls import path

from . import views

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboardnexym/',views.dashboardView,name="dashboard"),
    path('signin/',),
    path('signup/',),
    path('signout/',),

]