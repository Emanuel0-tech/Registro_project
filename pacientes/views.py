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


   