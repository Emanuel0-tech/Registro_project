from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200,verbose_name = 'Nome:')
    cpf = models.CharField(max_length=11, unique=True, verbose_name = 'CPF:')
    data_nascimento = models.DateField(verbose_name = 'Data de nascimento:')
    endereco = models.CharField(max_length=255, verbose_name = 'Endereço:')
    # email = models.EmailField(max_length=100, unique=True, null=True)
    historico_medico = models.TextField(max_length=500, verbose_name = 'Histórico médico:')


    def __str__(self):
        return self.nome
    

# class Post(models.Model):
#     titulo = models.CharField(max_length=100, verbose_name='Titulo')
#     conteudo = models.TextField(verbose_name='')
#     data_criacao = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.titulo