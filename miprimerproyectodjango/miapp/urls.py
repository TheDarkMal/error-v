from django.urls import path
from .views import cargar_inicio, LibroList, LibroCreate,LibroUpdate,LibroDelete,LibroDetalle,EjemplarList,EjemplarDelete,EjemplarUpdate,EjemplarDetalle

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('libros/nuevo/', LibroCreate.as_view(), name = 'nuevo_libro'),
    path('libros/editar/<int:pk>', LibroUpdate.as_view(), name = 'editar_libro'),
    path('libros/Borrar/<int:pk>', LibroDelete.as_view(), name = 'borrar_libro'),
    path('libros/detalle/<int:pk>', LibroDetalle.as_view(), name = 'detalle_libro'),
    path('ejemplar/', EjemplarList.as_view(), name = 'ejemplar_libro'),
    path('ejemplar/Borrar/<int:pk>', EjemplarDelete.as_view(), name = 'Borrar_ejemplar'),
    path('ejemplar/editar/<int:pk>', EjemplarUpdate.as_view(), name = 'actualizar_ejemplar'),
    path('ejemplar/detalle/<int:pk>', EjemplarDetalle.as_view(), name = 'detalle_ejemplar')
]