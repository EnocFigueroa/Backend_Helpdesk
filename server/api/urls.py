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

urlpatterns = [
    path('', include(router.urls)),
]
