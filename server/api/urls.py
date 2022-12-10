from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('area', views.AreaViewSet, basename="area")
router.register('ticket', views.TicketViewSet, basename="ticket")
router.register('usuario', views.UsuarioViewSet, basename="usuario")
router.register('proyecto', views.ProyectoViewSet, basename="proyecto")
router.register('comentario', views.ComentarioViewSet, basename="comentario")
router.register('historial', views.HistorialViewSet, basename="historial")
router.register('estatus', views.EstatusViewSet, basename="estatus")
router.register('especialista', views.EspecialistaViewSet,
                basename="especialista")
router.register('prioridad', views.PrioridadViewSet, basename="prioridad")
router.register('rol', views.RolViewSet, basename="rol")
urlpatterns = [
    path('', include(router.urls)),
]
