from django.db import models

class Consulta(models.Model):
    descricao = models.CharField(max_length=200)
    data_consulta = models.DateField()

    def __str__(self):
        return self.descricao