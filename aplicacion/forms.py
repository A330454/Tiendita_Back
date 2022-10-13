from tkinter import Widget
from django import forms
from .models import Producto, Transaccion

class TransaccionForm(forms.ModelForm):
    tipo=forms.BooleanField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Transaccion
        fields = ["tipo", "producto", "cantidad"]

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

