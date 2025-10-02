import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200 or target_currency not in data['rates']:
            print("Error fetching exchange rate.")
            return None
        return data['rates'][target_currency]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def convert_currency(base_currency, target_currency, amount):
    rate = get_exchange_rate(base_currency.upper(), target_currency.upper())
    if rate:
        converted = amount * rate
        print(f"{amount} {base_currency.upper()} = {converted:.2f} {target_currency.upper()}")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    print("💱 Currency Converter (Live Rates)")
    base = input("Enter base currency (e.g., USD): ")
    target = input("Enter target currency (e.g., EUR): ")
    try:
        amount = float(input(f"Enter amount in {base.upper()}: "))
        convert_currency(base, target, amount)
    except ValueError:
        print("Invalid amount entered.")
