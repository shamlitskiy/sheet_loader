from django.urls import path
from .views import change_list, update_orders

app_name = 'main_app'
urlpatterns = [
    path('', change_list, name='change-list'),
]