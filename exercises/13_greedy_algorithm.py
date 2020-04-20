def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers"""

    itemsCopy = sorted(items, key = keyFunction, reverse = true)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)): 
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    
    return (result, totalValue)

# Python's sort algorithm uses the quicksort algorithm, which is O(n log n). We also loop over each 
# item, which is O(n), because e touch each item once. Therefore, this greedy algorithm's complexity is O(n log n).
