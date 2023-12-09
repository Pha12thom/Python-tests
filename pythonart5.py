import pygame
import sys
import random

pygame.init()

# Set up the display
width, height = 300, 300
cell_size = 20
matrix_width = width // cell_size
matrix_height = height // cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matrix Slime Animation")

clock = pygame.time.Clock()

# Matrix representation of the slime
slime_matrix = [[random.choice([0, 1]) for _ in range(matrix_width)] for _ in range(matrix_height)]

def draw_slime(surface, matrix, cell_size):
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(surface, (0, 255, 0), (x * cell_size, y * cell_size, cell_size, cell_size))

def main():
    global slime_matrix

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update slime matrix (change some cells randomly)
        slime_matrix = [[random.choice([0, 1]) for _ in range(matrix_width)] for _ in range(matrix_height)]

        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_slime(screen, slime_matrix, cell_size)

        pygame.display.flip()
        clock.tick(1)  # Slow down the animation for better visibility

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
