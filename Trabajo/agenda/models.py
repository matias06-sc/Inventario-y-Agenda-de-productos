from django.db import models

class Producto(models.Model):
    producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.producto
