from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'<Attribute: {self.name}>'
