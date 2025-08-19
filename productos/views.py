from django.shortcuts import render


def formulario_producto(request):
    return render(request, "productos/formulario.html")
