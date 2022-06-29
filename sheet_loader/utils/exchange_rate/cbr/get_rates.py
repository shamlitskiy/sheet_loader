import requests
import xml.etree.ElementTree as ET


def call_api():
    api_url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(api_url)
    return response


def get_usd_rub_rate():
    resp = call_api()
    root = ET.fromstring(resp.content)
    for r in root:
        if r[1].text == 'USD':
            return float(r[4].text.replace(',', '.'))
