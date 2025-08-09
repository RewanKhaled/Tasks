"""
Matrix Script Decoder
This program:
- Reads matrix dimensions and characters from the user.
- Reads characters column by column.
- Removes unwanted symbols between letters and replaces them with spaces.
"""

import re
N, M = map(int, input("Enter number of rows and columns: ").split()) # Read N and M
# Read the matrix
print(f"Enter the {N} rows of the matrix (each with {M} characters):") 
matrix = []
for i in range(N):
    row = input()
    # Pad or trim to match M characters
    if len(row) < M:
        row = row.ljust(M)  # Add spaces to the right
    elif len(row) > M:
        row = row[:M]  # Trim extra characters
    matrix.append(row)

decoded = ''.join(matrix[row][col] for col in range(M) for row in range(N)) # Decode message column by column
cleaned = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', decoded) # Clean unwanted symbols between letters
print("Decoded message:", cleaned)