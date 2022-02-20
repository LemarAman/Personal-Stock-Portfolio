import sys
from art import *
import Market_Functions
from Market_Functions import *

print(text2art('''L F S''', font="block"))
print("Welcome to Lemar Financial Services")

while True:
    print("Please indicate what you like to do")
    userChoice = input(
        "Enter 'deposit' to deposit cash, 'buy' to buy stock, 'sell' to sell stock, 'balance' to view your cash/stock portfolio. 'estimate' to "
        "calculate a price. 'quit' to sign out. " '\n')

    if userChoice.lower() == 'buy':
        stockBuyChoice = input("Enter a valid stock ticker. To view available stock tickets, visit "
                            "https://stockanalysis.com/stocks/" '\n')
        checkStr = isinstance(stockBuyChoice, str)
        if checkStr:
            amountBuyChoice = float(input("Enter amount looking to purchase: "))
            checkFloat1 = isinstance(amountBuyChoice,float)
            if checkFloat1:
                Market_Functions.buyStock(stockBuyChoice,amountBuyChoice)
                Market_Functions.savePortfolio()
            else: print("Error. Enter a valid float amount.")
        else: print("Error. Enter a valid stock ticker.")

    elif userChoice.lower() == 'sell':
        stockSellChoice = input("Enter the stock ticker. To view stocks available to you to sell, enter 'portfolio' "
                                "\n")
        checkStr2 = isinstance(stockSellChoice, str)
        if checkStr2:
            if stockSellChoice == 'portfolio':
                viewPortfolio()
                continue
            else:
                amountSellChoice = input("Enter amount looking to sell:")
                checkFloat = isinstance(amountSellChoice,float)
                if checkFloat:
                    Market_Functions.sellStock(stockSellChoice, amountSellChoice)
                    Market_Functions.savePortfolio()
                else:
                    print("Please enter a float")
        else: print("Please enter a valid stock ticker or 'portfolio'")

    elif userChoice.lower() == 'balance':
            viewPortfolio()
            print(f'Your total stock portfolio value, cash + assets is:  ${int(netWorth()):,}')

    elif userChoice.lower() == 'estimate':
        estimationChoice = input("Enter the stock ticker. To view available stock tickets, visit "
                            "https://stockanalysis.com/stocks/" '\n')
        estimationAmountChoice = float(input(f"Enter amount of {estimationChoice} "))
        priceEstimator(estimationChoice, estimationAmountChoice)
    elif userChoice.lower() == 'deposit':
        depositAmount = input("Enter how much cash you want to deposit: ")
        depositCash(depositAmount)
        Market_Functions.savePortfolio()
    elif userChoice.lower() == 'quit':
        print("Thanks for using LFS")
        sys.exit(1)
    else:
        print("Enter a valid entry. 'buy' 'sell' 'balance' 'estimate' 'quit' ")

