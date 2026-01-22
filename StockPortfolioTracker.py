
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_value = 0
portfolio = {}

print(" 📊 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print(" ❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))
    value = stock_prices[stock] * quantity
    portfolio[stock] = value
    total_value += value

print("\n 📈 Portfolio Summary")
for stock, value in portfolio.items():
    print(f"{stock}: ₹{value}")

print(f"\n 💰 Total Investment Value: ₹{total_value}")


with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, value in portfolio.items():
        file.write(f"{stock}: ₹{value}\n")
    file.write(f"\nTotal Investment: ₹{total_value}")

print("\n📁Portfolio saved to portfolio.txt")
