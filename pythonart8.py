import os
import time
import random

os.system('color 0b')  # Set console color to red

# Define the heart shape
heart_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
]

# Function to print the heart shape
def print_heart():
    for row in heart_matrix:
        for val in row:
            print(' ' if val == 0 else '1', end=' ')
        print()

# Print the heart shape for a certain duration
tm = 0
while tm < 5:  # Print for 5 seconds
    print_heart()
    tm += 1
    time.sleep(1)
