from django.db import models
from django.db.models import (
    IntegerField,
    FloatField,
    DateField,
)


class Order(models.Model):
    number = IntegerField(editable=False, verbose_name='№')
    order_number = IntegerField(editable=False, verbose_name='Order, №')
    cost_usd = FloatField(editable=False, verbose_name='cost, $')
    delivery_date = DateField(editable=False)
    cost_rub = FloatField(editable=False, verbose_name='cost, ₽')

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
