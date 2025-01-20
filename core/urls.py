from django.contrib import admin
from django.urls import path
from pacientes import views
from consultas.views import registrar_consulta
from pacientes.views import cadastrar_paciente, sucesso_cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cadastrar_paciente),
    path("registrar/<int:paciente_id>/", registrar_consulta),
    path('sucesso/',sucesso_cadastro, name='sucesso_cadastro'),
    path('registrar_consulta', views.registrar_paciente)

] 

