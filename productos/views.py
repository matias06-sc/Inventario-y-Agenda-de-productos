from django.shortcuts import redirect, render

from .models import Producto


def formulario_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")

        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect("agenda_productos")

    return render(request, "productos/formulario.html")


def agenda_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/agenda_productos.html", {"productos": productos})
