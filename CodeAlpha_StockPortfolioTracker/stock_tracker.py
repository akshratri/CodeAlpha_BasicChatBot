stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 350,
    "AMZN": 170
}

total = 0

print("Available Stocks:")
for stock, price in stocks.items():
    print(f"{stock}: ${price}")

n = int(input("\nHow many stocks do you own? "))

for i in range(n):
    stock_name = input("Enter stock symbol: ").upper()

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock_name] * quantity
        total += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total}")

print("Portfolio saved to portfolio.txt")
