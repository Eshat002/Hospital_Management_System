from django.shortcuts import render
from .models import Patient
from django.core.paginator import Paginator
from django.http import JsonResponse


def patient(request):
    return render(request, "pages/patient.html", {})


def patient_list(request):
    qs = Patient.objects.all()

    if len(qs) == 0:
        return JsonResponse({"data": "Your patients appear here"})

    patient_per_page = 8
    paginator = Paginator(qs, patient_per_page)
    page_number = request.GET.get("page")
    patients = paginator.get_page(page_number)

    data = []

    for patient in patients:
        patient_data = {
            "name": patient.get_full_name,
            "age": patient.age,
            "gender": patient.gender,
            "blood_group": patient.blood_group,
            "phone": patient.phone,
            "id": patient.id,
            "email": patient.email,
            "avatar": patient.avatar.url
        }
        data.append(patient_data)

    next_page = patients.next_page_number() if patients.has_next() else None
    previous_page = patients.previous_page_number() if patients.has_previous() else None

    return JsonResponse(
        {
            "data": data,
            "next_page": next_page,
            "previous_page": previous_page,
            "total_pages": paginator.num_pages,
            "total_patients": qs.count()
        }
    )
