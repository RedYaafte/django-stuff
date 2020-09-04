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
