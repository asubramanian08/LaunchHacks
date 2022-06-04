# picks what item to buy to maximize happiness

def selectBuys(monthlyBudget, timeSpan, monthlyItemCosts, monthlyItemValues,
               oneTimeItemCosts, oneTimeItemValues):
    monthlyPurchases = []
    oneTimePurchases = []
    happinessValues = []
    cumulativeCosts = monthlyItemCosts + oneTimeItemCosts
    cumulativeValues = monthlyItemValues + oneTimeItemValues
    mthItmCount = len(monthlyItemCosts)
    for i in range(timeSpan):
        purchases, happiness = knapsack(cumulativeCosts, cumulativeValues)
        happinessValues.append(happiness)
        monthlyPurchases.append([])
        oneTimePurchases.append([])
        for j in purchases:
            if j < mthItmCount:
                monthlyPurchases[i].append(j)
            else:
                oneTimePurchases[i].append(j)
                # stop further uses of the item
                cumulativeValues[j] = 0
    return monthlyPurchases, oneTimePurchases, happinessValues


def knapsack(costs, values, budget):
    # run the knapsack
    knapsackMat = [[]]
    for i in range(budget):
        knapsackMat[0].append(0)
    for i in range(1, len(costs) + 1):
        knapsackMat.append([])
        for j in range(budget + 1):
            usingItemI = knapsackMat[i][j]
            if j >= costs[i]:
                usingItemI = knapsackMat[i][k - costs[i]] + values[i]
            knapsackMat[i+1][j] = max(knapsackMat[i][j], usingItemI)
    # figure out what items to include
    including = []
    currSpent = budget
    for i in range(len(costs), 0, -1):
        if knapsackMat[i][currSpent] != knapsackMat[i-1][currSpent]:
            currSpent -= costs[i - 1]
            include.append(i - 1)
    # return the items the include, max happiness
    return include, knapsackMat[len(costs)][budget]
