### Jordan Duffin Wong
### 11 August 2021 -- Due 16 August 2021
### Python Camp
### Homework 1

### Goals: Be able to do each of the following:
# portfolio = Portfolio() 				# Creates a new portfolio
# portfolio.addCash(300.50) 			# Adds cash to the portfolio
# s = Stock(20, "HFH") 					# Create Stock with price 20 and symbol "HFH"
# portfolio.buyStock(5, s) 				# Buys 5 shares of stock s
# mf1 = MutualFund("BRT")				# Create MF with symbol "BRT"
# mf2 = MutualFund("GHT")				# Create MF with symbol "GHT"
# portfolio.buyMutualFund(10.3, mf1)	# Buys 10.3 shares of "BRT"
# portfolio.buyMutualFund(2, mf2)		# Buys 2 shares of "GHT"
# print(portfolio)						# Prints portfolio
										# Cash: $140.50
										# Stock: 5 HFH
										# Mutual Funds:	10.33 BRT
										#				2 GHT
# portfolio.sellMutualFund("BRT", 3)	# Sells 3 shares of BRT
# portfolio.sellStock("HFH", 1)			# Sells 1 share of HFH
# portfolio.withdrawCash(50)			# Removes $50
# portfolio.history()					# Prints a list of all transactions
										# ordered by time
# BONUS: using inheritance, show how it would be easy to add a third type of
# investments -- Bonds -- to the mix.

### Step 0: Import packages we need
import random

### Step 1: Creating the "Portfolio" class
class Portfolio:
	def __init__ (self, Cash = 0, Stocks = 0, MFs = 0):
		self.log = []		# Creates a log of transactions
		self.Cash = Cash	# Start with no cash, obviously
		self.Stocks = {}	# These are _our_ stocks (we start with none)
		self.MFs = {}		# These are _our_ mutual funds (we start with none)
		self.s = {} 		# Initialize an empty dictionary to keep track of possible stocks
		self.MF = {}		# Initialize an empty dictionary to keep track of possible mutual funds
        
	def __str__ (self):
		return 'Cash: ${}'.format(self.Cash) + '\nStocks: {}'.format(self.Stocks) + '\nMFs: {}'.format(self.MFs)

	def history(self):
		print(*self.log, sep = "\n")
        
### Step 2: creating the functions to add and withdraw cash
	def addCash(self, added):
		self.Cash = portfolio.Cash + added		# Just adds the value to the existing portfolio.
		ledger = "Added ${} cash".format(added)
		self.log.append(ledger)
	def withdrawCash(self, withdrew):
		self.Cash = portfolio.Cash - withdrew	# Same as adding, but subtraction.
		ledger = "Withdrew ${} cash".format(withdrew)
		self.log.append(ledger)
        

### Step 3: creating the function to generate new stock
	def Stock(self, value, symbol):
		self.s[symbol] = value
		ledger = "Created the {} stock valued at  ${}.".format(symbol, value)
		self.log.append(ledger)

### Step 4: creating the functions to buy and sell stock.
	def buyStock(self, quantity, symbol):
		self.Stocks[symbol] = self.Stocks.get(symbol, 0) + quantity			# Increases the number of stocks
		self.Cash = portfolio.Cash - (quantity * portfolio.s.get(symbol))	# Deducts cash as appropriate
		ledger = "Bought {} of {}.".format(quantity, symbol)
		self.log.append(ledger)
	def sellStock(self, symbol, quantity): 									# Reverse of buying stocks
		self.Stocks[symbol] = self.Stocks.get(symbol, 0) - quantity
		self.Cash = portfolio.Cash + (quantity * portfolio.s.get(symbol) * random.uniform(0.5, 1.5))	# Sell price is a random variable drawn from Unif(0.5, 1.5)
		ledger = "Sold {} of {}.".format(quantity, symbol)
		self.log.append(ledger)

### Step 5: creating the function to create mutual funds
# This is mostly the same as buying and selling stocks
	def MutualFund(self, symbol, index = 1):
		self.MF[symbol] = index		# Values of buying mutual funds are given as $1 per share
		ledger = "Created the {} mutual fund.".format(index)
		self.log.append(ledger)

### Step 6: creating the function to buy and sell mutual funds
	def buyMutualFund(self, quantity, symbol):
		self.MFs[symbol] = self.MFs.get(symbol, 0) + quantity
		self.Cash = portfolio.Cash - quantity
		ledger = "Bought {} of {}.".format(quantity, symbol)
		self.log.append(ledger)


	def sellMutualFund(self, symbol, quantity):
		self.MFs[symbol] = self.MFs.get(symbol, 0) - quantity
		self.Cash = portfolio.Cash + quantity * random.uniform(0.9, 1.2)	# Sell price is a random variable drawn from Unif(0.9, 1.2)
		ledger = "Sold {} of {}.".format(symbol, quantity)
		self.log.append(ledger)

### Step 7: View the transaction history
### For formatting error reasons, this is coded earlier in the document.
		

### Execution (does this code work?):
print("""Part 1: Testing whether the code works.
		\n\nLet's make a new portfolio!""")
portfolio = Portfolio()

# Cash
print("""How much cash do we have?\n$"""+
		"{:.2f}".format(portfolio.Cash) +
		""". Hmm. That's not much. Let's add some. Here's $300.50, on the house.\n*adds your cash*\n""")
portfolio.addCash(300.50)
print("There. Now we've got $" + "{:.2f}".format(portfolio.Cash) + ".\n")

# Getting stocks
print("""Let's create some new stock, "HFH", worth $20.00 per share.\n*creates the stock*\n""")
portfolio.Stock(20, "HFH")
print("""Let's buy 5 shares of HFH.\n*buys your stocks*\n""")
portfolio.buyStock(5, "HFH")
print("Now we have", portfolio.Stocks.get("HFH"), "stocks in HFH and $",
	"{:.2f}".format(portfolio.Cash), "left over.")

# Getting mutual funds
print("""Let's create some mutual funds, "BRT" and "GHT".\n*creates the mutual funds*\n""")
portfolio.MutualFund(1, "BRT")
portfolio.MutualFund(2, "GHT")
print("""Now let's buy 10.3 in BRT and 2 in GHT.\n*buys the mutual funds*\n""")
portfolio.buyMutualFund(10.3, "BRT")
portfolio.buyMutualFund(2, "GHT")

print("Now we have", portfolio.MFs.get("BRT"), "shares in BRT and",
	portfolio.MFs.get("GHT"), "shares in GHT.\n")

# Looking at the portfolio.
print("Let's take a look at what we have in the portfolio now.")
print(portfolio)

# Selling mutual funds and stocks.
print("""Let's sell some of our assets.\n*sells 3 mutual funds*\n*sells 1 HFH*\n""")
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)

# Withdrawing some cash.
print("""Let's withdraw $50.00.\n*withdraws $50.00*\n""")
portfolio.withdrawCash(50.00)

# Finally, let's look at all of our transactions.
print("Here's everything we've done:")
portfolio.history()

