from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.db import transaction

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import (
    ThemeConfig,
    Patient,
    Utilisateur,
    Consultation,
    Pathologie,
    Prescription,
    RegistreMaladie
)

from .serializers import (
    PatientSerializer,
    UtilisateurSerializer,
    ConsultationSerializer,
    PathologieSerializer,
    PrescriptionSerializer,
    RegistreMaladieSerializer
)

# =========================
# THEME CONFIG
# =========================
def get_theme(request):
    theme = ThemeConfig.objects.first()
    if not theme:
        return JsonResponse({"error": "Aucun thème défini"}, status=404)

    data = {
        "primary_color": theme.primary_color,
        "secondary_color": theme.secondary_color,
    }
    return JsonResponse(data)


# =========================
# PATIENTS API
# =========================
@api_view(['GET', 'POST'])
@transaction.atomic
def patients_api(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            patient = serializer.save()
            return Response(
                {
                    "message": "Patient enregistré avec succès",
                    "id": patient.id
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# CONSULTATIONS API
# =========================
@api_view(['GET', 'POST'])
@transaction.atomic
def consultations_api(request):
    if request.method == 'GET':
        consultations = Consultation.objects.all()
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ConsultationSerializer(data=request.data)

        if serializer.is_valid():
            consultation = serializer.save()
            return Response(
                {
                    "message": "Consultation enregistrée avec succès",
                    "id": consultation.id
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "message": "Erreur de validation",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================
# PATHOLOGIES API
# =========================
@api_view(['GET', 'POST'])
@transaction.atomic
def pathologies_api(request):
    if request.method == 'GET':
        pathologies = Pathologie.objects.all()
        serializer = PathologieSerializer(pathologies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PathologieSerializer(data=request.data)

        if serializer.is_valid():
            pathologie = serializer.save()
            return Response(
                {
                    "message": "Pathologie enregistrée avec succès",
                    "id": pathologie.id
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# PRESCRIPTIONS API
# =========================
@api_view(['GET', 'POST'])
@transaction.atomic
def prescriptions_api(request):
    if request.method == 'GET':
        prescriptions = Prescription.objects.all()
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PrescriptionSerializer(data=request.data)

        if serializer.is_valid():
            prescription = serializer.save()
            return Response(
                {
                    "message": "Prescription enregistrée avec succès",
                    "id": prescription.id
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# REGISTRE MALADIES API
# =========================
@api_view(['GET'])
def registre_maladies_api(request):
    registre = RegistreMaladie.objects.all()
    serializer = RegistreMaladieSerializer(registre, many=True)
    return Response(serializer.data)


# =========================
# UTILISATEUR (CREATION SECURISEE)
# =========================
@api_view(['POST'])
@transaction.atomic
def creer_utilisateur(request):
    data = request.data

    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        email=data.get('email', '')
    )

    return Response(
        {
            "message": "Utilisateur créé avec succès",
            "id": user.id
        },
        status=status.HTTP_201_CREATED
    )


# =========================
# PAGES HTML
# =========================
def solution(request):
    return render(request, 'solution.html')


def nouvelle_consultation(request):
    return render(request, 'nouvelle_consultation.html')


def ancienne_consultation(request):
    return render(request, 'ancienne_consultation.html')


def registre_medical(request):
    return render(request, 'registre_medical.html')


def parametres(request):
    return render(request, 'parametres.html')

