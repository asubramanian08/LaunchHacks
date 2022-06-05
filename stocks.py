"""  Manages the users trading portfolio with real-time stock data. """

import pandas_datareader as web


class stockManager:
    """ Manages the user's portfolio of stocks.

    Attributes
    ----------
    portfolio : list
         - All stocks (of stockManager.stock type) bought by the user
    """

    def __init__(self):
        self.portfolio = []

    def buy(self, ticker: str, shares: int, limit: float) -> (int, float):
        """ "Buys" some number of stocks and adds it to the portfolio.

        Parameters
        ----------
        ticker : str
             - Ticker of the stock to be bought
        shares : int
             - Number of shares to buy
        limit : float
             - Maximum amount of money to be spent on all the stocks
             - Limits the number of shares to buy

        Returns
        -------
        * int -> number of shares that were bought
            * Could be the given shares value
            * Limits by the limit price
            * 0 if the purchase can't be made
        * float -> price of each stock
        """

        self.portfolio.append(self.stock(ticker, shares, limit))
        return self.portfolio[-1].shares, self.portfolio[-1].boughtAt

    def sell(self, ticker: str, shares: int) -> (int, float):
        """ "Sells" some number of stocks if its in the portfolio.

        Parameters
        ----------
        ticker : str
             - Ticker of the stock to be bought
        shares : int
             - Number of shares to buy

        Returns
        -------
        * int -> number of shares that were sold
        * float -> what each stock sold for
        """

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
        """ Prints info on all the stocks in the portfolio using stocks.__str__(). """

        for p in self.portfolio:
            if p.shares > 0:
                print(p)

    def quote(self, ticker: str) -> float:
        """ Find the real time price of the stock.

        Parameters
        ----------
        ticker : str
             - Ticker of the stock to be bought

        Returns
        -------
        * float -> price of the stock
        """

        return self.stock.quote(ticker)

    class stock:
        """ One purchase of a stock (can have multiple shares).

        Attributes
        ----------
        ticker : str
             - stock ticker
        boughtAt : float
             - price the stock was bought at
        shares : int
             - number of share the user has of that stock

        Parameters
        ----------
        ticker : str
             - Ticker of the stock to be bought
        shares : int
             - Number of shares to buy
        limit : float
             - Maximum amount of money to be spent on all the stocks
             - Limits the number of shares to buy
        """

        def __init__(self, ticker: str, shares: int, limit: float):
            self.ticker = ticker
            self.boughtAt = self.price()
            if self.boughtAt == 0:
                self.shares = 0
            else:
                self.shares = min(shares, int(limit / self.boughtAt))

        def __str__(self) -> str:
            """ Short description of the stock's purchase information.

            Returns
            -------
            * str -> info about the purchase
                * Number of shares
                * Ticker
                * The price it was bought at
                * Current price of the stock
            """

            return f"{self.shares} shares of \
{self.ticker} bought at ${self.boughtAt} now ${self.price()}"

        def sellShares(self, sell: int) -> int:
            """ Remove some number of shares from the purchase.

            Parameters
            ----------
            sell : int
                 - share of the stock to sell
                 - limited buy the shares already bought

            Returns
            -------
            * int -> number of shares actually sold
            """

            sharesSold = min(self.shares, sell)
            self.shares -= sharesSold
            return sharesSold

        def price(self) -> float:
            """ The current price of the stock, taken from stock.quote().

            Returns
            -------
            * float -> real time stock price
            """

            return self.quote(self.ticker)

        @staticmethod
        def quote(ticker: str) -> float:
            """ Real time stock price using yahoo's data.

            Parameters
            ----------
            ticker : str
                 - Ticker of the stock to be bought

            Returns
            -------
            * float -> real time stock price
            """

            db = web.get_data_yahoo(ticker, start="2022-06-01")
            stockAt = db['Adj Close'][-1]
            return round(stockAt, 2)
