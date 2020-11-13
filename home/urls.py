from django.urls import path
from .views import specialty_detail_view

urlpatterns = [
    path('compétences/<int:pk>/', specialty_detail_view, name='specialty_detail'),
]