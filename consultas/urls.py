from django.urls import include, path
from pacientes.models import views

urlpatterns = [
    path(
        "registrar/<int:paciente_id>/",
        "consultas.views.registrar_consulta",
        name="registrar_consulta",
    ),
]
