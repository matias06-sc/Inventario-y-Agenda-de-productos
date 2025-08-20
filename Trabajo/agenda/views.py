from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# LISTAR y CREAR en la misma página
def producto_list(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'agenda/producto_list.html', {'form': form, 'productos': productos})

# EDITAR
def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'agenda/producto_edit.html', {'form': form})

# ELIMINAR
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('producto_list')

# FILTRO
def producto_filter(request):
    query = request.GET.get('q')
    resultados = Producto.objects.filter(producto__icontains=query) if query else []
    return render(request, 'agenda/producto_filter.html', {'resultados': resultados})
