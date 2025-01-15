from django.shortcuts import render, redirect
from .models import Paciente
from django.contrib.auth.models import User
from .forms import ConsultaForm


def registrar_consulta(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente
            consulta.medico = request.user
            consulta.save()
            return redirect("historico_consultas.html", paciente_id=paciente.id)
        else:
            form = ConsultaForm()
        return render(
            request,
            "registro_consultas.html",
            {"form": form, "paciente": paciente},
        )

