class stockManager:
    class stock:
        def __init__(self, ticker: str, shares: int, limit: float):
            self.ticker = ticker
            self.boughtAt = self.price()
            self.shares = min(shares, int(limit / self.boughtAt))

        def __str__(self) -> str:
            return f"{self.shares} shares of \
{self.ticker} bought at {self.boughtAt} now {self.price()}"

        def sellShares(self, sell: int = 1) -> int:
            sharesSold = min(self.shares, sell)
            self.shares -= sharesSold
            return sharesSold

        def price(self) -> float:
            return self.quote(self.ticker)

        @staticmethod
        def quote(ticker: str) -> float:
            stockAt = 0.000
            return round(stockAt, 2)

    def __init__(self):
        self.portfolio = []

    def buy(self, ticker, shares, limit) -> (int, float):
        self.portfolio.append(self.stock(ticker, shares, limit))
        return self.portfolio[-1].shares, self.portfolio[-1].boughtAt

    def sell(self, ticker, shares) -> (int, float):
        sharesSold = 0
        currPrice = self.stock.quote(ticker)
        newPort = []
        for s in self.portfolio:
            if s.ticker == ticker and sharesSold < shares:
                sharesSold += s.sellShares(shares - sharesSold)
            if s.shares > 0:
                newPort.append(s)
        self.portfolio = newPort
        return sharesSold, currPrice

    def display(self) -> None:
        for p in self.portfolio:
            if p.shares > 0:
                print(p)

    def quote(self, ticker) -> float:
        return self.stock.quote(ticker)
