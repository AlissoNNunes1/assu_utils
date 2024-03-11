from django.urls import path
from . import views

urlpatterns = [
    path('bgremover/', views.bgremover, name='bgremover'),  # URL para a view bgremover
]
