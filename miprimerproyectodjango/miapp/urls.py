from django.urls import path
from .views import cargar_inicio, LibroList, LibroCreate,LibroUpdate,LibroDelete,LibroDetalle,EjemplarList,EjemplarDelete,EjemplarUpdate,EjemplarDetalle,EjemplarCreate,PrestamoList,PrestamoCreate,PrestamoUpdate,LoginView,LogoutView

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
    path('ejemplar/detalle/<int:pk>', EjemplarDetalle.as_view(), name = 'detalle_ejemplar'),
    path('ejemplar/nuevo', EjemplarCreate.as_view(), name = 'nuevo_ejemplar'),

    path('prestamo/', PrestamoList.as_view(), name = 'prestamo_lista'),
    path('prestamo/nuevo', PrestamoCreate.as_view(), name = 'prestamo_nuevo'),
    path('prestamo/editar/<int:pk>', PrestamoUpdate.as_view(), name = 'actualizar_prestamo'),

    path('iniciosesion', LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logoutsesion', LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
]