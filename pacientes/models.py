from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    # email = models.EmailField(max_length=100, unique=True, null=True)
    historico_medico = models.TextField(max_length=500)


    def __str__(self):
        return self.nome