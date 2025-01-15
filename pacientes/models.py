from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    historico_medico = models.TextField()

    def __str__(self):
        return self.nome