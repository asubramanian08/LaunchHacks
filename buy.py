""" Determine what items the user should buy contained by the amount of money they have. """


def selectBuys(budget: int, monthlyWantsPrices: list, monthlyWantsValues: list,
               oneTimeWantsPrices: list, oneTimeWantsValues: list) -> tuple[list, list, int]:
    """ Selects the optimal items to buy to maximize the happiness value.

    Parameters
    ----------
    budget : int
         - maximum amount of money that can be spent
    monthlyWantsPrices : list
    monthlyWantsValues : list
         - prices or happiness values for all the monthly wanted items
         - examples of monthly wants are netflix subscriptions or amusement park passes
    oneTimeWantsPrices : list
    oneTimeWantsValues : list
         - prices or happiness values for all wanted items that are purchased once
         - examples of one time wants are laptops or the latest fashionable clothing

    Returns
    -------
    * list -> monthly wants that should be bought
    * list -> one time purchases that should be bought
    * int -> happiness attained for all items bought
    """

    # determine the best items to buy (knapsack algorithm)
    cumulativePrices = monthlyWantsPrices + oneTimeWantsPrices
    cumulativeValues = monthlyWantsValues + oneTimeWantsValues
    allPurchases, happiness = knapsack(
        cumulativePrices, cumulativeValues, budget)

    # determine which monthly vs. one time items were bought
    monthlyPurchases = []
    oneTimePurchases = []
    mwCount = len(monthlyWantsPrice)
    for itemBought in allPurchases:
        # the item is within the range of monthly wants
        (monthlyPurchases if itemBought <
         mwCount else oneTimePurchases).append(itemBought)

    # return all monthly and one time purchases made
    # along with how happy it will make the user
    return monthlyPurchases, oneTimePurchases, happiness


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
            knapsackMat[i+1][j] = max(knapsackMat[i][j], usingItemI)

    # figure out what items to include
    including = []
    currSpent = budget
    for i in range(len(prices), 0, -1):
        if knapsackMat[i][currSpent] != knapsackMat[i-1][currSpent]:
            currSpent -= prices[i - 1]
            including.append(i - 1)

    # return the items the include, max happiness
    return including, knapsackMat[len(prices)][budget]
