import yfinance as yf

symbol = input("Enter the stock symbol: ").upper()
stock = yf.Ticker(symbol)

try:
    price = stock.history(period="1d")["Close"].iloc[-1]
    print(f"Current price of {symbol}: ${price:2f}")
except:
    print("Invalid stock symbol or data not available")

