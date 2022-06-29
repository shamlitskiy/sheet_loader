from django.urls import path
from .views import change_list, setup_google_sheet

app_name = 'main_app'
urlpatterns = [
    path('', change_list, name='change-list'),
    path('setup-google-sheet', setup_google_sheet, name='setup-google-sheet'),
]