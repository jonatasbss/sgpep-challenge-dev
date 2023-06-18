from django.db import models


# Create your models here.
class Proposta(models.Model):
    STATUS_PROPOSTA = (
        ('Em Análise', 'Em Análise'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado')
    )

    cliente = models.ForeignKey('usuario.CustomUser', related_name='propostas', on_delete=models.CASCADE, blank=True)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    valor_emprestico = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, choices=STATUS_PROPOSTA, default='Em Análise')

    class Meta:
        db_table = 'proposta'
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'

    def __str__(self):
        return '{} - {}'.format(self.nome_completo, self.cpf)
