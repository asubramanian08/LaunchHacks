# pick what items to buy to maximize happiness

def selectBuys(budget, monthlyWantsPrices, monthlyWantsValues,
               oneTimeWantsPrices, oneTimeWantsValues):
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


def knapsack(prices, values, budget):
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
