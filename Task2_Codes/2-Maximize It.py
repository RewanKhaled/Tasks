"""
Maximize It
This program:
- Reads K lists of numbers and a modulo value M.
- Chooses one element from each list in all possible ways.
- Calculates (sum of squares of chosen elements) % M.
- Finds and prints the maximum possible value.
"""

from itertools import product  # to generate all combinations
print("Enter K (number of lists) and M (modulo value):") # read K and M
K, M = map(int, input().split())

lists = []
for i in range(K): # read all K lists
    print(f"Enter the number of elements in list {i+1} followed by the elements:")
    data = list(map(int, input().split()))
    lists.append(data[1:])  # skip Ni, keep only list elements
max_S = 0  # store the maximum S found

print("\nCalculating all possible combinations...")
# try every combination of one element from each list
for combo in product(*lists):
    S = sum(x**2 for x in combo) % M # Calculate sum of squares and take modulo M
    max_S = max(max_S, S) # Update max_S if this is larger

print("\nThe maximum possible value is:", max_S)
