from django.urls import path

from . import views

urlpatterns = [
    path("", views.agenda_productos, name="agenda_productos"),
    path("formulario_producto", views.formulario_producto, name="formulario_producto"),
]
