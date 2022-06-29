from datetime import datetime as dt

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Order, GoogleSheetSettings
from django.db.models import ObjectDoesNotExist

from utils.google.sheets_api.read import get_data
from utils.exchange_rate.cbr.get_rates import get_usd_rub_rate


def setup_google_sheet(request):
    spreadsheet_id = None
    range_name = None
    try:
        ggl_sht_settings = GoogleSheetSettings.objects.get()
        spreadsheet_id = ggl_sht_settings.spreadsheet_id
        range_name = ggl_sht_settings.range_name
    except ObjectDoesNotExist:
        pass

    if request.POST:
        if request.POST.get('apply_settings'):
            spreadsheet_id = request.POST.get('spreadsheet_id')
            range_name = request.POST.get('range_name')
            update_google_sheet_settings(spreadsheet_id, range_name)
            return HttpResponseRedirect(reverse('main_app:change-list'))

    return render(request, 'googel_sheet_setup.html',
                  {'spreadsheet_id': spreadsheet_id,
                   'range_name': range_name,
                   'opts': Order._meta})


def change_list(request):
    update_orders(request)
    return HttpResponseRedirect(reverse('admin:{}_{}_changelist'.format(Order._meta.app_label,
                                                                        Order._meta.model_name)))


def update_orders(request):
    try:
        ggl_sht_settings = GoogleSheetSettings.objects.get()
        spreadsheet_id = ggl_sht_settings.spreadsheet_id
        range_name = ggl_sht_settings.range_name
    except ObjectDoesNotExist:
        messages.set_level(request, messages.WARNING)
        messages.warning(request, "Google sheet id or range not set")
        return
    if not spreadsheet_id or not range_name:
        messages.set_level(request, messages.WARNING)
        messages.warning(request, "Google sheet id or range not set")
        return

    Order.objects.all().delete()
    try:
        data = get_data(spreadsheet_id=spreadsheet_id,
                        range_name=range_name,
                        res_type='list')
        usd_rub_rate = get_usd_rub_rate()
        Order.objects.bulk_create([Order(number=d[0],
                                         order_number=d[1],
                                         cost_usd=d[2],
                                         delivery_date=dt.strptime(d[3], "%d.%m.%Y"),
                                         cost_rub=float(d[2])*usd_rub_rate) for d in data[1:]])
    except Exception:
        messages.set_level(request, messages.WARNING)
        messages.error(request, "Wrong google sheet config.")
        return


def update_google_sheet_settings(spreadsheet_id, range_name):
    GoogleSheetSettings.objects.all().delete()
    new_ggl_sht_settings = GoogleSheetSettings(spreadsheet_id=spreadsheet_id, range_name=range_name)
    new_ggl_sht_settings.save()
