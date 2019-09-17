from django.db import models

from utils import get_object_or_404


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'<Department: {self.name}>'

    @classmethod
    def get_categories_from_id(cls, department_id):
        department = get_object_or_404(cls, id=department_id)
        return department.categories.all()
