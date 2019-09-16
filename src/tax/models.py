from django.db import models


class Tax(models.Model):
    tax_type = models.CharField(max_length=100)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'<Tag: {self.tax_type}>'
