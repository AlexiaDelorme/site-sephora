from django.urls import path
from .views import specialty_detail_view, sub_specialty_detail_view, honoraires_view

urlpatterns = [
    path('compétences/<int:pk>/', specialty_detail_view, name='specialty_detail'),
    path('compétences/détails/<int:pk>/',
         sub_specialty_detail_view, name='sub_specialty_detail'),
    path('honoraires/', honoraires_view, name='honoraires'),
]
