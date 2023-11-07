def fractionalKnapsack(items, capacity):
    for item in items:
        item['value_per_weight'] = item['value'] / item['weight']

    items.sort(key=lambda x: x['value_per_weight'], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if item['weight'] <= capacity:
            total_value += item['value']
            knapsack.append(item)
            capacity -= item['weight']
        else:
            fraction = capacity / item['weight']
            total_value += item['value'] * fraction
            knapsack.append({'name': item['name'], 'value': item['value'] * fraction, 'weight': item['weight'] * fraction})
            break

    return total_value, knapsack

# Input from the user
n = int(input("Enter the number of items: "))
items = []
for i in range(n):
    name = input(f"Enter the name of item {i + 1}: ")
    value = float(input(f"Enter the value of item {i + 1}: "))
    weight = float(input(f"Enter the weight of item {i + 1}: "))
    items.append({'name': name, 'value': value, 'weight': weight})

capacity = float(input("Enter the knapsack capacity: "))

max_value, selected_items = fractionalKnapsack(items, capacity)
print("Maximum value that can be obtained:", max_value)
print("Selected items:", selected_items)
