from django.shortcuts import render


def patient(request):
    return render(request, "pages/patient.html", {})
