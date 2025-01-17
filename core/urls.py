from django.contrib import admin
from django.urls import include, path
from consultas.views import registrar_consulta
from pacientes.views import cadastrar_paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cadastrar_paciente),
    path("registrar/<int:paciente_id>/", registrar_consulta,),

] 
