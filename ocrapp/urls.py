from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_handwritten_image, name='upload_handwritten_image'),
    path('show/', views.show_handwritten_text, name='show_handwritten_text'),
   
]
