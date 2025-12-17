import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY_HERE" 

def fetch_historical_rates(base, target, days=30):
    start_date = datetime.today() - timedelta(days=days)
    dates, rates = [], []

    for i in range(days):
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        url = f"https://api.currencyapi.com/v3/historical?apikey={API_KEY}&date={date}&base_currency={base}&target_currency={target}"
        
        try:
            response = requests.get(url)
            data = response.json()

            rate = data.get("data", {}).get(target, {}).get("value")
            if rate:
                dates.append(date)
                rates.append(rate)
        except requests.RequestException:
            print(f"Error fetching data for {date}")
    
    return dates, rates

def plot_trend(base, target, days=30):
    print("Fetching data...")
    dates, rates = fetch_historical_rates(base, target, days)

    if not rates:
        print("No valid data available to plot.")
        return

    # Plot
    plt.plot(dates, rates, marker='o', color='blue')
    plt.title(f"{base} to {target} - Last {days} Days")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def show_trends_gui(base, target, days=30):
    plot_trend(base, target, days)
