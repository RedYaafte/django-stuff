from django.db import models


class UuId(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Formulary(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    uuid = models.ManyToManyField(UuId, verbose_name='uuids')

    def __str__(self):
        return self.name


class ContentLink(models.Model):
    FORM = 0
    EVALUATION = 1
    TEMARY = 2
    CONTRACT = 3
    WELCOME_LETTER = 4

    NAME_CHOICES = (
        (FORM, 'Formulario de Inscripción'),
        (EVALUATION, 'Evaluación Diagnóstica'),
        (TEMARY, 'Temario'),
        (CONTRACT, 'Contrato de Adheción'),
        (WELCOME_LETTER, 'Carta Bienvenida')
    )

    name = models.PositiveSmallIntegerField(choices=NAME_CHOICES, default=FORM)
    url = models.URLField()
    uuid = models.ForeignKey(UuId, on_delete=models.CASCADE)

    def __str__(self):
        name = self.NAME_CHOICES[self.name][1]
        return f'{self.uuid}: {name}'
