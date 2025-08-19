from django.urls import path

from . import views

urlpatterns = [
    path("formulario/", views.formulario_producto, name="formulario"),
]
