from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'<Department: {self.name}>'
