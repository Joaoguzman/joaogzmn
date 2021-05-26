from django.db import models


class Order(models.Model):
    empresa = models.CharField(max_length=20)
    sector = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    porcentaje_ddhh = models.DecimalField(max_digits=5, decimal_places=2)