from problem_5_1 import read_weights, read_profits, read_capacity, read_optimal_capacity


def binaryKnapsack(cap, weight, profit, n):
    dp = [0 for i in range(cap + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(cap, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if weight[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + profit[i - 1])

    return dp[cap]  # returning the maximum value of knapsack


if __name__ == '__main__':
    weights = read_weights()
    profits = read_profits()
    capacity = read_capacity()
    capacity = capacity[0]
    optimal_capacity = read_optimal_capacity()

    maxValue = binaryKnapsack(capacity, weights, profits, len(profits))
    print('Max value =', maxValue)
