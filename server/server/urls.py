from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
urlpatterns = [
    path('admin/', admin.site.urls),
    # Urls de la api 
    path('', include('api.urls')),
    # Urls de django-allauth
    path('accounts/', include('allauth.urls')),

    path('home/',
         TemplateView.as_view(template_name='home.html'), name='home'),


    # Urls de Schemas y Documentacion de la API
    path('openapi/', get_schema_view(
        title="Servicio REST",
        description="API desarrollada para los servicios de la mesa de ayuda del CIDETEC",
        version="1.0.0"
    ), name="openapi-schema"),
    path('documentacion/',
         TemplateView.as_view(
             template_name="documentation.html",
             extra_context={"schema_url": "openapi-schema"}
         ), name="swagger-ui"),
]
