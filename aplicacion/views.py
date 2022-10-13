from django.shortcuts import render
from .forms import TransaccionForm
from .models import Producto

# Create your views here.
def index(request):
    prodcutos = Producto.objects.all()
    my_dict ={
        'productos': prodcutos
    }
    return render(request,'index.html',context=my_dict)

def producto(request, id):
    if request.method == "POST":
        registro= TransaccionForm(request.POST)
        print(registro.fields['tipo'])
        if registro.is_valid():
            x = registro.save() 
    producto = Producto.objects.get(pk=id)
    my_dict ={
        'producto': producto
    }
    return render(request,'informacionProducto.html',context=my_dict)

def crearRegistroCompra(request, id):
    formularioTransaccion = TransaccionForm(initial={"producto": id, "tipo":False})
    return render(request, "registro.html", {'registro':formularioTransaccion, 'producto':id})

def crearRegistroVenta(request, id):
    formularioTransaccion = TransaccionForm(initial={"producto": id, "tipo":True})
    return render(request, "registro.html", {'registro':formularioTransaccion, 'producto':id})
