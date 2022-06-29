from datetime import datetime as dt

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings

from .models import Order

from utils.google.sheets_api.read import get_data
from utils.exchange_rate.cbr.get_rates import get_usd_rub_rate


def change_list(request):
    update_orders()
    return HttpResponseRedirect(reverse('admin:{}_{}_changelist'.format(Order._meta.app_label,
                                                                        Order._meta.model_name)))


def update_orders():
    Order.objects.all().delete()
    data = get_data(spreadsheet_id=settings.GOOGLE_SHEET_SPREADSHEET_ID,
                    range_name=settings.GOOGLE_SHEET_RANGE_NAME,
                    res_type='list')
    usd_rub_rate = get_usd_rub_rate()
    Order.objects.bulk_create([Order(number=d[0],
                                     order_number=d[1],
                                     cost_usd=d[2],
                                     delivery_date=dt.strptime(d[3], "%d.%m.%Y"),
                                     cost_rub=float(d[2])*usd_rub_rate) for d in data[1:]])
