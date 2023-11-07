# dynamic programming

def knapSack(W, wt, val, n):
    # Create a table to store the results of subproblems
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build the dp table in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Take user input for the number of items
n = int(input("Enter the number of items: "))

# Initialize empty lists for values and weights
val = []
wt = []

# Input values and weights from the user
for i in range(n):
    item_val = int(input(f"Enter the value of item {i + 1}: "))
    item_wt = int(input(f"Enter the weight of item {i + 1}: "))
    val.append(item_val)
    wt.append(item_wt)

# Take user input for the knapsack capacity
W = int(input("Enter the knapsack capacity: "))

# Call the knapSack function and print the result
result = knapSack(W, wt, val, n)
print("Maximum value that can be obtained:", result)
