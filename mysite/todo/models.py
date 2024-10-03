from django.db import models


# Create your models here.
class Todo(models.Model):
    """Aqui eu configurarei como funcionará todo o esquema do banco de dados do app Todo, onde cada atributo de classe representará
    uma coluna do banco de dados, por exemplo, titulo.
    """

    tarefa_tipo_tempo = [("R", "Recorrente"), ("U", "Única")]

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    criado_em = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    tipo_tarefa = models.CharField(
        null=False, blank=False, max_length=1, choices=tarefa_tipo_tempo
    )
    descricao = models.CharField(max_length=255, blank=False, null=False)
    frequencia = models.PositiveIntegerField(blank=False, null=True)
    horario = models.TimeField(blank=False, null=True)
    termino_tarefa = models.DateField(blank=False, null=True)
