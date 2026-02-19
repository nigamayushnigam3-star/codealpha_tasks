class StockPortfolio:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, symbol, quantity, price):
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive")
        symbol = symbol.upper()
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            self.stocks[symbol] = {'quantity': quantity, 'price': price}
    
    def update_price(self, symbol, new_price):
        symbol = symbol.upper()
        if symbol not in self.stocks:
            raise KeyError(f"Stock {symbol} not found")
        if new_price <= 0:
            raise ValueError("Price must be positive")
        self.stocks[symbol]['price'] = new_price
    
    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.stocks:
            del self.stocks[symbol]
    
    def get_total_investment(self):
        return sum(s['quantity'] * s['price'] for s in self.stocks.values())
    
    def display_portfolio(self):
        if not self.stocks:
            print("\nPortfolio is empty")
            return
        print("\n" + "="*50)
        print(f"{'Symbol':<10} {'Shares':<10} {'Price':<12} {'Value':<15}")
        print("="*50)
        for symbol, data in sorted(self.stocks.items()):
            value = data['quantity'] * data['price']
            print(f"{symbol:<10} {data['quantity']:<10} ${data['price']:<11.2f} ${value:<14.2f}")
        print("="*50)
        print(f"{'TOTAL INVESTMENT:':<34} ${self.get_total_investment():.2f}")
        print("="*50)


if __name__ == "__main__":
    portfolio = StockPortfolio()
    
    portfolio.add_stock("AAPL", 10, 150.00)
    portfolio.add_stock("GOOGL", 5, 2800.00)
    portfolio.add_stock("MSFT", 8, 300.00)
    portfolio.add_stock("aapl", 5, 150.00)
    
    portfolio.display_portfolio()
    
    print("\n--- Updating MSFT price ---")
    portfolio.update_price("MSFT", 320.00)
    portfolio.display_portfolio()
    
    print("\n--- Removing GOOGL ---")
    portfolio.remove_stock("GOOGL")
    portfolio.display_portfolio()
