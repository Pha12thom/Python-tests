import pygame
import random
import sys

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Matrix Animation")

clock = pygame.time.Clock()

# Define coordinates for the heart and letter 'A'
heart_coordinates = [(0, -30), (20, -60), (40, -30), (60, -60), (80, -30), (40, 40)]
a_coordinates = [(0, 0), (35, 100), (65, 100), (50, 55)]

def draw_shape(surface, coordinates, x, y):
    transformed_coordinates = [(coord[0] + x, coord[1] + y) for coord in coordinates]
    pygame.draw.polygon(surface, (255, 0, 0), transformed_coordinates)

def main():
    matrix_speed = 4
    x_position = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        draw_shape(screen, heart_coordinates, x_position, height // 2 - 50)
        draw_shape(screen, a_coordinates, x_position + 100, height // 2 - 50)

        x_position += matrix_speed
        if x_position > width:  # Reset position when it goes off the screen
            x_position = -100

        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
