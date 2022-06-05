""" Determine what items the user should buy contained by the amount of money they have. """


def selectBuys(budget: int, yearlyWantsPrices: list, yearlyWantsValues: list,
               oneTimeWantsPrices: list, oneTimeWantsValues: list) -> (list, list, int, int):
    """ Selects the optimal items to buy to maximize the happiness value.

    Parameters
    ----------
    budget : int
         - maximum amount of money that can be spent
    yearlyWantsPrices : list
    yearlyWantsValues : list
         - prices or happiness values for all the yearly wanted items
         - examples of yearly wants are netflix subscriptions or amusement park passes
    oneTimeWantsPrices : list
    oneTimeWantsValues : list
         - prices or happiness values for all wanted items that are purchased once
         - examples of one time wants are laptops or the latest fashionable clothing

    Returns
    -------
    * list -> yearly wants that should be bought
    * list -> one time purchases that should be bought
    * int -> happiness attained for all items bought
    * int -> total price of all purchases
    """

    # Best items to buy (knapsack algorithm)
    cumulativePrices = yearlyWantsPrices + oneTimeWantsPrices
    cumulativeValues = yearlyWantsValues + oneTimeWantsValues
    allPurchases, happiness = knapsack(
        cumulativePrices, cumulativeValues, budget)

    # Which yearly vs. one time items were bought
    yearlyPurchases = []
    oneTimePurchases = []
    mwCount = len(yearlyWantsPrices)
    for itemBought in allPurchases:
        # the item is within the range of yearly wants
        if itemBought < mwCount:
            yearlyPurchases.append(itemBought)
        else:  # item is a one time purchase
            oneTimePurchases.append(itemBought - mwCount)

    # Total price of all purchases
    totalPrice = 0
    for item in yearlyPurchases:
        totalPrice += yearlyWantsPrices[item]
    for item in oneTimePurchases:
        totalPrice += oneTimeWantsPrices[item]

    # return all yearly and one time purchases made,
    # happy it will make the user, and how much it costs
    return yearlyPurchases, oneTimePurchases, happiness, totalPrice


def knapsack(prices: list, values: list, budget: int) -> list:
    """ Knapsack algorithms that backtracks to determine what items were brought

    Parameters
    ----------
    prices : list
         - prices of all the items that can be "packed"
    values : list
         - happiness value attained from each item
    budget : int
         - maximum amount of money that can be spent

    Returns
    -------
    * list -> items to buy
    """

    # run the knapsack algorithm
    knapsackMat = [[]]
    for i in range(budget):
        knapsackMat[0].append(0)
    for i in range(1, len(prices) + 1):
        knapsackMat.append([])
        for j in range(budget + 1):
            usingItemI = knapsackMat[i][j]
            if j >= prices[i]:
                usingItemI = knapsackMat[i][j - prices[i]] + values[i]
            knapsackMat[i + 1][j] = max(knapsackMat[i][j], usingItemI)

    # figure out what items to include
    including = []
    currSpent = budget
    for i in range(len(prices), 0, -1):
        if knapsackMat[i][currSpent] != knapsackMat[i - 1][currSpent]:
            currSpent -= prices[i - 1]
            including.append(i - 1)

    # return the items the include, max happiness
    return including, knapsackMat[len(prices)][budget]
