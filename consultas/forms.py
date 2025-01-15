from django import forms
from ..pacientes.models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data_consulta', 'descricao']