from django.db import models

# Create your models here.

TIPO_CONTRATO_CHOICES = {
    ('PJ', 'Pessoa Jurídica'),
    ('CLT', 'Consolidação das Leis do Trabalho')
}

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=50, null=False)
    cnpj = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)

    class Meta:
        db_table = 'empresa'

class Vaga(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    descricao = models.TextField(null=False)
    salario = models.FloatField(null=False)
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO_CHOICES, null=False, max_length=50)
    status = models.BooleanField(default=True, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vaga'


class Requisito(models.Model):
    descricao = models.TextField(null=False)
    vaga = models.ForeignKey(Vaga, related_name='requisitos_vaga', on_delete=models.CASCADE)

    class Meta:
        db_table = 'requisito'

