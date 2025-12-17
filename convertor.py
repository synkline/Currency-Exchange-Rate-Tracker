import requests

def get_currency_list():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API Error! Check your connection.")
    data = response.json()
    return list(data["rates"].keys())


def get_conversion_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API Error! Check your connection.")

    data = response.json()
    if to_currency not in data["rates"]:
        raise Exception("Invalid currency code!")

    return data["rates"][to_currency]


def convert_currency(amount, from_currency, to_currency):
    rate = get_conversion_rate(from_currency, to_currency)
    return round(amount * rate, 2)