from django.db import models

from department.models import Department


class Category(models.Model):
    department = models.ForeignKey(
        Department,
        related_name='categories',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'<Category: {self.name}>'
