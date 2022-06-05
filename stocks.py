# for docstring: full file annotations, arg type, arg default, return
# look up how to annotate a class and its methods
# add in the actually stock quote code

class stockManager:
    class stock:
        def __init__(self, ticker: str, shares: int = 1):
            self.ticker = ticker
            self.shares = shares
            self.boughtAt = self.stockPrice()

        def __str__(self) -> str:
            return f"{self.shares} shares of {self.ticker} \
    bought at {self.boughtAt} now {self.stockPrice()}"

        def sellShares(self, sell: int = 1):
            toSell = min(self.shares, sell)
            self.shares -= toSell
            return toSell

        def stockPrice(self) -> int:
            return quote(self.ticker)

        @staticmethod
        def quote(ticker: str) -> int:
            return -1

    def __init__(self):
        self.portfolio = []

    def buy(self, ticker, shares) -> int:
        self.portfolio.append(stock(ticker, shares))
        return self.portfolio[-1].shares * self.portfolio[-1].boughtAt

    def sell(self, ticker, shares) -> int:
        sharesSold = 0
        currPrice = stock.quote(ticker)
        newPort = []
        for s in self.portfolio:
            if s.ticker == ticker and sharesSold < shares:
                sharesSold += s.sellShares(shares - sharesSold)
            if s.shares > 0:
                newPort.append(s)
        self.portfolio = newPort
        return sharesSold * currPrice

    def display(self):
        for p in portfolio:
            if p.shares > 0:
                print(p)

    def quote(self, ticker) -> int:
        return stock.quote(ticker)
