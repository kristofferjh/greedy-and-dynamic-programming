import csv


def read_weights():
    weights = []
    with open('data/p08_weights.csv', newline='') as f:
        lines = csv.reader(f)
        for line in lines:
            weights.append(int(''.join(line)))
    return weights


def read_profits():
    profits = []
    with open('data/p08_profits.csv') as f:
        lines = csv.reader(f)
        for line in lines:
            profits.append(int(''.join(line)))
    return profits


def read_capacity():
    capacity = []
    with open('data/p08_capacity.csv') as f:
        lines = csv.reader(f)
        for line in lines:
            capacity.append(int(''.join(line)))
    return capacity


def read_optimal_capacity():
    capacities = []
    with open('data/p08_optimal_selection.csv') as f:
        lines = csv.reader(f)
        for line in lines:
            capacities.append(int(''.join(line)))
    return capacities


def getMaximumValue(weights, profits, capacity):
    total_profit = 0

    for i in range(len(weights)):
        current_weight = weights[i]
        current_value = profits[i]

        if capacity - current_weight >= 0:
            capacity -= current_weight
            total_profit += current_value
        else:
            fraction = capacity / current_weight
            total_profit += current_value * fraction
            capacity = int(capacity - (current_weight * fraction))
            break
    return total_profit


if __name__ == '__main__':
    all_weights = read_weights()
    all_profits = read_profits()
    capacity = read_capacity()
    capacity = capacity[0]
    optimal_capacities = read_optimal_capacity()

    maxValue = getMaximumValue(all_weights, all_profits, capacity)
    print("Maximum value in knapsack =", maxValue)


