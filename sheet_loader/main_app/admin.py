from django.contrib import admin
from .models import Order


class OrderModel(admin.ModelAdmin):
    change_list_template = 'change_list.html'
    list_display = [
        'number',
        'order_number',
        'cost_usd',
        'delivery_date',
        'cost_rub',
    ]
    ordering = ['number']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Order, OrderModel)
