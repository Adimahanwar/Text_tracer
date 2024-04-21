from django.urls import path
from . import views

urlpatterns = [
    path('translate/', views.translate_to_indian_language, name='translate_to_hindi'),
]
