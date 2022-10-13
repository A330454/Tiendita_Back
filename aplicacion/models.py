from django.db import models

# Create your models here.

class   Producto(models.Model):
    nombre = models.CharField(max_length = 20, null=False, blank=False)
    precio = models.PositiveIntegerField()
    imagen = models.TextField(null=True, blank= True)
    cantidad = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.nombre.title()

    def display_price(self):
        return str(self.precio)

    def calcula_ventas(self):
        total = 0
        for trasaccion in Transaccion.objects.filter(producto = self):
            if trasaccion.tipo == 1:
                total += trasaccion.cantidad
        return total

    class Meta:
        db_table = "Productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Transaccion(models.Model):
    tipo = models.BooleanField()
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    monto = models.IntegerField( null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        tipo = "venta " if self.tipo else "compra "
        return tipo + str(self.cantidad) + " " + self.producto.nombre

    def save(self, *args, **kwargs):
        if self.pk is not None:
            raise Exception("No se puede editar un registro")
        if self.tipo:
            self.producto.cantidad -= self.cantidad
            self.monto = self.producto.precio * self.cantidad
        else:
            self.producto.cantidad += self.cantidad
            self.monto = self.producto.precio * self.cantidad
        if self.producto.cantidad < 0:
            raise Exception("No hay producto que vender")
        self.producto.save()
        super(Transaccion, self).save(*args, **kwargs)
        
        class Meta:
            db_table = "Transaccion"
            verbose_name = "Transaccion"
            verbose_name_plural = "Transacciones"