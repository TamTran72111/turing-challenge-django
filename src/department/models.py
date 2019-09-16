from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
