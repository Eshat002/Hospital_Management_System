from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("secret-admin/", admin.site.urls),
    path("patient/", include("patient.urls")),
]
