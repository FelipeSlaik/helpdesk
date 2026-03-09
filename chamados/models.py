from django.db import models

class Ticket(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=20, default="aberto")
    prioridade = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
