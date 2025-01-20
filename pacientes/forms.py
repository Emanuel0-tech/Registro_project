from django import forms
from .models import Paciente

class Pacienteforms(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'endereco','historico_medico']

        