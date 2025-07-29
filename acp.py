# Program to find the longest consecutive 1's in the binary representation

def longest_consecutive_ones(n):
    binary = bin(n)[2:]
    max_ones = max(len(group) for group in binary.split('0'))
    return max_ones

# Get input from the user
num = int(input("Enter your number: "))
result = longest_consecutive_ones(num)

print("Longest consecutive 1's length:", result)