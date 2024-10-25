from django.db import models

class Agendamento(models.Model):
    SERVIÇOS_CHOICES = [
        ('corte_masculino', 'Corte Masculino'),
        ('corte_feminino', 'Corte Feminino'),
        ('corte_infantil', 'Corte Infantil'),
        ('coloracao', 'Coloração'),
        ('selagem', 'Selagem'),
        ('hidratacao', 'Hidratação'),
        ('progressiva', 'Progressiva Orgânica Sem Formol'),
        ('outros', 'Outros'),
    ]

    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)  # Campo opcional
    servicos = models.CharField(max_length=50, choices=SERVIÇOS_CHOICES)  # Pode ser ajustado para armazenar múltiplas escolhas
    data_desejada = models.DateField()
    horario_desejado = models.TimeField()
    mensagem = models.TextField(blank=True, null=True)  # Campo opcional

    def __str__(self):
        return f"{self.nome} - {self.data_desejada} {self.horario_desejado}"
