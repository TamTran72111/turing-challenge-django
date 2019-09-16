from django.db import models

from orders.models import Orders


class Audit(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    code = models.IntegerField()

    def __str__(self):
        return f'<Audit order {self.order.id} on {self.created_on}>'
