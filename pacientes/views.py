from django.shortcuts import redirect, render
from .forms import Pacienteforms

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = Pacienteforms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cadastrar_paciente.html', {'form': form, 'alerta': 'Paciente cadastrado com sucesso!'})
        else:
            return render(request, 'cadastrar_paciente.html', {'form': form})
    else:
        form = Pacienteforms()
        return render(request, 'cadastrar_paciente.html', {'form': form})

def sucesso_cadastro(request):
    return render(request, 'sucessso_cadastro.html')


from django.shortcuts import render
from .models import Paciente

def registrar_paciente(request):
    pacientes = Paciente.objects.all().order_by('nome')
    return render(request, 'registrar_pacientes.html', {'pacientes': pacientes})