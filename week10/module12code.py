## the assignment before the rat 

import numpy as np

# Read the file
with open("module12quizF25.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

#Reshape into 100x100 matrix
matrix = np.array(numbers).reshape(100, 100)

#Calculate the key values
# Average of the numbers in the 6th row (index 5)
val1 = int(round(np.mean(matrix[5])))

# Minimum number in the 29th column (index 28)
val2 = int(np.min(matrix[:, 28]))

# Maximum of the first 3 numbers in the 24th column (index 23)
val3 = int(np.max(matrix[:3, 23]))

# Sum of the last 3 numbers in the 100th row (index 99)
val4 = int(np.sum(matrix[99, -3:]))

# Minimum of the last 3 numbers in the 91st row (index 90)
val5 = int(np.min(matrix[90, -3:]))

key_values = [val1, val2, val3, val4, val5]

# Convert key numbers to letters (0 = a, 25 = z)
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = ""
for v in key_values:
    key += alphabet[v]

print("Key:", key)

# Construct ciphertext alphabet
plaintext = alphabet
ciphertext = ""
seen = []

# Add key letters first
for c in key:
    if c not in seen:
        ciphertext += c
        seen.append(c)

# Add remaining letters in order
for c in plaintext:
    if c not in seen:
        ciphertext += c

# Decipher the message
message = "zpvtplwcihu"
deciphered = ""
for c in message:
    index = ciphertext.index(c)
    deciphered += plaintext[index]

print("Deciphered message:", deciphered)