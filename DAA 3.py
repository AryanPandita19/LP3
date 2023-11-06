def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item.append(item[0] / item[1])

    # Sort the items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    knapsack = []

    for item in items:
        if capacity >= item[1]:  # If the whole item can be added
            capacity -= item[1]
            total_value += item[0]
            knapsack.append((item[0], item[1], 1.0))  # Fraction = 1 (whole item added)
        else:
            fraction = capacity / item[1]
            total_value += item[0] * fraction
            knapsack.append((item[0], item[1], fraction))
            break

    return total_value, knapsack

# Input the number of items and the knapsack capacity
n = int(input("Enter the number of items: "))
capacity = float(input("Enter the knapsack capacity: "))

items = []

# Input item values and weights
for i in range(n):
    value = float(input(f"Enter the value of item {i + 1}: "))
    weight = float(input(f"Enter the weight of item {i + 1}: "))
    items.append([value, weight])

# Solve the Fractional Knapsack problem
total_value, knapsack = fractional_knapsack(items, capacity)

# Display the results
print("\nOptimal value in knapsack:", total_value)
print("Selected items:")
for item in knapsack:
    print(f"Value: {item[0]}, Weight: {item[1]}, Fraction: {item[2]}")
