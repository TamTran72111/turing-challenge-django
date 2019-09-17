from django.db import models

from utils import get_object_or_404


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'<Attribute: {self.name}>'

    @classmethod
    def get_values_from_id(cls, attribute_id):
        attribute = get_object_or_404(cls, id=attribute_id)
        return attribute.attributevalue_set.all()
