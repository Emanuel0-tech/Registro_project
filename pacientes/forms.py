
from django import forms
from .models import Paciente

class Pacienteform(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'historico_medico']