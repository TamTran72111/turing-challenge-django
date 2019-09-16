from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=100)
