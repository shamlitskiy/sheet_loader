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


class GoogleSheetSettings(models.Model):
    spreadsheet_id = models.CharField(max_length=1024, blank=False, null=False,
                                       help_text='Google Sheets spreadsheet URL or spreadsheetId. '
                                                 'Example: https://docs.google.com/spreadsheets/d/%spreadsheet_id%/ '
                                                 'or %spreadsheet_id%')
    range_name = models.CharField(max_length=255, blank=False, null=False,
                                  help_text='Sheet name. Example: Sheet1!A:B')

    class Meta:
        db_table = 'google_sheet_settings'
        verbose_name = 'Google sheet settings'
