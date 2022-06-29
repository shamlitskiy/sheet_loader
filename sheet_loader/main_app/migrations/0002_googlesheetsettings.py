# Generated by Django 4.0.5 on 2022-06-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleSheetSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spreadsheet_id', models.CharField(help_text='Google Sheets spreadsheet URL or spreadsheetId. Example: https://docs.google.com/spreadsheets/d/%spreadsheet_id%/ or %spreadsheet_id%', max_length=1024)),
                ('range_name', models.CharField(help_text='Sheet name. Example: Sheet1!A:B', max_length=255)),
            ],
            options={
                'verbose_name': 'Google sheet settings',
                'db_table': 'google_sheet_settings',
            },
        ),
    ]
