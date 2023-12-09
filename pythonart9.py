import os
import time

os.system('color 0a')  # Set console color to green

# Define the characters for each letter in the name
M = [
    "1   1",
    "11 11",
    "1 1 1",
    "1   1",
    "1   1",
]
I = [
    "11111",
    "  1  ",
    "  1  ",
    "  1  ",
    "11111",
]
L = [
    "1    ",
    "1    ",
    "1    ",
    "1    ",
    "11111",
]
U = [
    "1   1",
    "1   1",
    "1   1",
    "1   1",
    "11111",
]
G = [
    " 111 ",
    "1   1",
    "1    ",
    "1 111",
    " 1111",
]
O = [
    " 111 ",
    "1   1",
    "1   1",
    "1   1",
    " 111 ",
]
E = [
    "11111",
    "1    ",
    "1111 ",
    "1    ",
    "11111",
]
F = [
    "11111",
    "1    ",
    "1111 ",
    "1    ",
    "1    ",
]
R = [
    "1111 ",
    "1   1",
    "1111 ",
    "1  1 ",
    "1   1",
]
Y = [
    "1   1",
    " 1 1 ",
    "  1  ",
    "  1  ",
    " 1   ",
]

# Map each letter to its corresponding matrix
name_matrix = {
    'M': M,
    'I': I,
    'L': L,
    'U': U,
    'G': G,
    'O': O,
    'E': E,
    'F': F,
    'R': R,
    'Y': Y,
}

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(' '.join([' ' if val == ' ' else '1' for val in row]))

# Function to print the name
def print_name(name):
    for char in name:
        if char in name_matrix:
            print_matrix(name_matrix[char])
        print()  # Add some space between letters

# Print the name for a certain duration
tm = 0
while tm < 5:  # Print for 5 seconds
    print_name("MILUGO GEOFREY")
    tm += 1
    time.sleep(1)
