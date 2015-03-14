from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/index.html', {'doctors': doctors})


def get_by_speciality(request, speciality):
    speciality = speciality.replace('-', ' ')
    doctors = Doctor.objects.filter(speciality=speciality)
    return render(request, 'doctors/index.html', {'doctors': doctors})


def get_by_name(request, name):
    name = name.replace('-', ' ')
    doctors = Doctor.objects.filter(name=name)
    return render(request, 'doctors/index.html', {'doctors': doctors})
