import yfinance as yf
from collections import defaultdict
import pickle
import os.path

cash = 0
stockPortfolio = defaultdict(int)

file_exists = os.path.exists('ledger.pkl')
if file_exists:
    with open('ledger.pkl', 'rb') as pickle_file:
        [cash, stockPortfolio] = pickle.load(pickle_file)


# retrieves live stock prices with stock symbols, utilized in the rest of the methods.
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0].round(2)

# Removes from the Stock Portfolio any stock that has a 0 value. Prints cash and stock holdings.
def viewPortfolio():
    global cash
    filtered = {k: v for k, v in stockPortfolio.items() if v != 0}
    stockPortfolio.clear()
    stockPortfolio.update(filtered)
    print(f'Your held cash is ${int(cash):,}')
    if len(stockPortfolio) == 0:
        print("You have no stock holdings")
    else:
        print(f"Your stock holdings include {dict(stockPortfolio)}")


# Buys stock. Subtracts from held cash based off current price and adds stock to stock portfolio.
def buyStock(symbol, amount):
    global cash
    symbol = symbol.upper()
    purchase_Price = get_current_price(symbol) * amount

    if cash >= purchase_Price:
        print(f"Successfully purchased {amount} {symbol} ")
        cash -= purchase_Price
        stockPortfolio[symbol.upper()] += amount
    else:
        print("Not enough cash. Please sell assets or deposit.")


# Sells held stock. If not enough stock, sale does not go through and error messages prints with existing stock.
def sellStock(symbol, amount):
    global cash
    symbol = symbol.upper()
    sale_Price = get_current_price(symbol) * amount

    if sale_Price > (stockPortfolio[symbol] * get_current_price(symbol)):
        print(f"You do not have enough of {symbol} to sell.")
        print(f"Current {symbol} holding: {stockPortfolio[symbol]}")
    else:
        print(f"Sucessfully sold {amount} {symbol}")
        cash += sale_Price
        stockPortfolio[symbol.upper()] -= amount

# Calculates the price of a desired stock
def priceEstimator(symbol, amount):
    symbol = symbol.upper()
    price = get_current_price(symbol) * float(amount)
    price = float(price)
    print(f"{amount} {symbol} would cost ${price.round(2)}".format())

# Deposits money for buying stocks
def depositCash(amount):
    global cash
    cash += float(amount)
    print(f'Sucessfully deposited ${int(amount):,}')


def savePortfolio():
    global cash
    global stockPortfolio
    with open('ledger.pkl', 'wb') as pickle_file:
        pickle.dump([cash,stockPortfolio], pickle_file)

def netWorth():
    global cash
    global stockPortfolio
    networth = cash
    for key in stockPortfolio:
        stockPrice = get_current_price(key) * stockPortfolio[key]
        networth += stockPrice
    return networth
