from django.shortcuts import render
from .forms import Pacienteforms

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = Pacienteforms(request.POST)
        if form.is_valid():
            form.save()
        return
    else:
        form = Pacienteforms()
        return render(request, 'cadastrar_paciente.html', {'form': form})


