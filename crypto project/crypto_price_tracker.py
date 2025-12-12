import requests
import json
from datetime import datetime

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,dogecoin",
        "vs_currencies": "inr"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    prices = {
        "Bitcoin": data["bitcoin"]["inr"],
        "Ethereum": data["ethereum"]["inr"],
        "Dogecoin": data["dogecoin"]["inr"]
    }
    
    return prices


def generate_html(prices):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_content = f"""
    <html>
    <head>
        <title>Crypto Price Dashboard</title>
        <style>
            body {{
                font-family: Arial;
                background: #f5f5f5;
                padding: 40px;
            }}
            h1 {{
                color: #333;
            }}
            table {{
                width: 40%;
                border-collapse: collapse;
                margin-top: 20px;
                background: white;
            }}
            th, td {{
                border: 1px solid #999;
                padding: 10px;
                text-align: left;
            }}
            th {{
                background: #4CAF50;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>Live Crypto Price Dashboard</h1>
        <p>Updated on: {now}</p>
        
        <table>
            <tr>
                <th>Crypto</th>
                <th>Price (INR)</th>
            </tr>
            <tr><td>Bitcoin</td><td>{prices['Bitcoin']}</td></tr>
            <tr><td>Ethereum</td><td>{prices['Ethereum']}</td></tr>
            <tr><td>Dogecoin</td><td>{prices['Dogecoin']}</td></tr>
        </table>
    </body>
    </html>
    """
    
    with open("crypto_dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("HTML Dashboard Generated: crypto_dashboard.html")


if __name__ == "__main__":
    prices = get_crypto_prices()
    print("Current Prices:", prices)
    generate_html(prices)