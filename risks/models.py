from django.db import models
from rest_framework import serializers

class RiskType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class DataType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class RiskTypeField(models.Model):
    name = models.CharField(max_length=50)
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    properties = models.CharField(max_length=1000, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'risk_type')
