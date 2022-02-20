This project is a personal stock portfolio. Users can enter stock tickers and retrieve real time prices. The project uses the yfinance library to retrieve prices. Users can deposit an amount of money, buy any decimal variation of a stock, sell any decimal variation of a stock that they own and calculate the price of a potential purchase.

The project should be executed into an IDE and then Ran, utilizing the console for its functionality. 

The project will run assuming proper input is entered, such as correct ticker symbols as strings when prompted and float values when entering numerical amounts. 

I chose yfinance because it was a simple straight forward to gain access to real time stock information. I found it is just a few lines of codes and works reliably with prices.

I utilized os.path to check if a pickle file exists. This is because the first time a user runs the program, there will be no pickle file that can load the cash variable and held stock dictionary. After the first time the user runs the program, the pickle data will be created and will be loaded moving forward for future uses.
