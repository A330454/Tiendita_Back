from django.urls import path
#from . import views as ApplicationViews
from . import views

urlpatterns = [
    # configured the URL
    path('home/', views.index),
    path("home/producto/<int:id>", views.producto, name="informacionProducto"),
    path("home/producto/registro/", views.producto),
    path("home/producto/compra/<int:id>", views.crearRegistroCompra),
    path("home/producto/vender/<int:id>", views.crearRegistroVenta),
    # path("home/producto/transaccion/guardar/<int:id>", views.guardarRegistro),
]