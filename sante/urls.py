from django.urls import path
from . import views 

urlpatterns = [
    # API Endpoints (C'est ici que votre fetch() va frapper)
    path('api/patients/', views.patients_api, name='patients_api'),
    path('api/consultations/', views.consultations_api, name='consultations_api'),
    path('api/pathologies/', views.pathologies_api, name='pathologies_api'),
    path('api/prescriptions/', views.prescriptions_api, name='prescriptions_api'),
    path('api/creer-utilisateur/', views.creer_utilisateur, name='creer_utilisateur'),

    # Pages Web
    path('', views.solution, name='solution'),
    path('nouvelle/', views.nouvelle_consultation, name='nouvelle'),
    path('ancienne/', views.ancienne_consultation, name='ancienne'),
    path('registre/', views.registre_medical, name='registre'),
    path('parametres/', views.parametres, name='parametres'),
]
