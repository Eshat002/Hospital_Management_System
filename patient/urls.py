from django.urls import path
from . import views

urlpatterns = [
    path("", views.patient, name="patient"),
    path("patient-list/", views.patient_list, name="patient-list"),
]
