import os
import time

os.system('color 0a')  # Set console color to green

# Define the characters for each letter in the name
M = ["1   1", "11 11", "1 1 1", "1   1", "1   1"]
I = ["11111", "  1  ", "  1  ", "  1  ", "11111"]
L = ["1    ", "1    ", "1    ", "1    ", "11111"]
U = ["1   1", "1   1", "1   1", "1   1", "11111"]
G = [" 111 ", "1   1", "1    ", "1 111", " 1111"]
O = [" 111 ", "1   1", "1   1", "1   1", " 111 "]

# Map each letter to its corresponding matrix
name_matrix = {'M': M, 'I': I, 'L': L, 'U': U, 'G': G, 'O': O}

# Function to print a matrix with spaces
def print_matrix_with_spaces(matrix):
    for row in matrix:
        print(' '.join([' ' if val == ' ' else '1' for val in row]))

# Function to print the name with spaces
def print_name_with_spaces(name):
    for char in name:
        if char in name_matrix:
            print_matrix_with_spaces(name_matrix[char])
            print(' ' * 5)  # Add spaces between letters

# Print the name with spaces
print_name_with_spaces("MILUGO")
