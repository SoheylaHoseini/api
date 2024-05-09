import requests
import matplotlib.pyplot as plt
from datetime import datetime

def get_bitcoin_data():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': '30'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def plot_bitcoin_price(data):
    prices = [entry[1] for entry in data['prices']]
    timestamps = [datetime.fromtimestamp(entry[0] / 1000) for entry in data['prices']]
    
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, marker='o', linestyle='-')
    plt.title('Bitcoin Price in USD Over the Last 30 Days')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.show()

bitcoin_data = get_bitcoin_data()
plot_bitcoin_price(bitcoin_data)
