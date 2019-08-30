from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Libro,Ejemplar,Prestamo

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin

def cargar_inicio(request):
    return render(request, "miapp/index.html")

class LibroList(ListView):
    model = Libro
    template_name = 'miapp/lista_libros.html'


class LibroCreate(CreateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/nuevo_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroUpdate(LoginRequiredMixin,UpdateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/actualizar_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroDelete(LoginRequiredMixin,DeleteView):
    model = Libro
    template_name = 'miapp/eliminar_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroDetalle(DetailView):
    model = Libro
    template_name =  'miapp/detalle_libro.html'

class EjemplarList(ListView):
    model = Ejemplar
    template_name = 'miapp/ejemplar_libro.html'
  #  success_url = reverse_lazy('listar_libros')

class EjemplarDelete(DeleteView):
    model = Ejemplar
    template_name = 'miapp/ejemplar_eliminar.html'
    success_url = reverse_lazy('ejemplar_libro')
class EjemplarUpdate(LoginRequiredMixin,UpdateView):
    model = Ejemplar
    fields = ['numeroejemplar','fechadecompra','libro']
    template_name = 'miapp/ejemplar_actualizar.html'
    success_url = reverse_lazy('ejemplar_libro')
class EjemplarDetalle(DetailView):
    model = Ejemplar
    template_name = 'miapp/ejemplar_detalle.html'
class EjemplarCreate(LoginRequiredMixin,CreateView):
    model = Ejemplar
    fields = ['numeroejemplar','fechadecompra','libro']
    template_name = 'miapp/ejemplar_create.html'
    success_url = reverse_lazy('ejemplar_libro')
class PrestamoList(ListView):
    model = Prestamo
    fields = ['fechaprestamo','nombre_cliente','telefono','estado']
    template_name = 'miapp/prestamo_listas.html'
class PrestamoCreate(LoginRequiredMixin,CreateView):
    model = Prestamo
    fields = ['fechaprestamo','nombre_cliente','telefono','estado']
    template_name = 'miapp/prestamo_create.html'
    success_url = reverse_lazy('prestamo_lista')
class PrestamoUpdate(LoginRequiredMixin,UpdateView):
    model = Prestamo
    fields = ['fechaprestamo','nombre_cliente','telefono','estado']
    template_name = 'miapp/prestamo_update.html'
    success_url = reverse_lazy('prestamo_lista')
