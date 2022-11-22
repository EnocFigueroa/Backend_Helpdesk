from django.urls import path
from . import views


urlpatterns = [
    path('estatus_entidad/', views.EntidadView.as_view()),
    path('estatus_entidad/<int:id>/', views.EntidadDetalle.as_view()),
    path('proyecto/', views.ProyectoView.as_view()),
    path('proyecto/<int:id>/', views.ProyectoDetalle.as_view()),
    path('area/', views.AreaView.as_view()),
    path('area/<int:id>/', views.AreaDetalle.as_view()),
    path('usuario/', views.UsuarioView.as_view()),
    path('usuario/<int:id>/', views.UsuarioDetalle.as_view()),
]

