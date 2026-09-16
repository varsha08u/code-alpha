STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 165,
    "MSFT": 420,
    "AMZN": 190
}


def calculate_portfolio():
    portfolio = []
    total_investment = 0

    print("\n=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found in the predefined list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        value = STOCK_PRICES[stock] * quantity
        total_investment += value
        portfolio.append((stock, quantity, STOCK_PRICES[stock], value))

    if not portfolio:
        print("No stocks were added.")
        return

    print("\n=== PORTFOLIO SUMMARY ===")
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Value':<12}")

    for stock, quantity, price, value in portfolio:
        print(f"{stock:<10}{quantity:<10}{price:<10}{value:<12}")

    print("-" * 42)
    print(f"Total Investment: {total_investment}")


if __name__ == "__main__":
    calculate_portfolio()
