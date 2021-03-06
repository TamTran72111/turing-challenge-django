from django.db import models

from attribute.models import Attribute


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f'<Attribute Value: {self.value}>'
