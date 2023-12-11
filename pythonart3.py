import pygame
import sys

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Heart Matrix Animation")

clock = pygame.time.Clock()

def draw_heart(surface, x, y):
    pygame.draw.polygon(surface, (255, 0, 0), [(x, y-30), (x+20, y-60), (x+40, y-30)])
    pygame.draw.polygon(surface, (255, 0, 0), [(x+40, y-30), (x+60, y-60), (x+80, y-30)])
    pygame.draw.polygon(surface, (255, 0, 0), [(x, y-30), (x+80, y-30), (x+40, y+40)])

def main():
    matrix_speed = 5
    heart_x = width // 2
    heart_y = height // 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        draw_heart(screen, heart_x, heart_y)

        heart_x += matrix_speed
        if heart_x > width + 100:  # Reset heart position when it goes off the screen
            heart_x = -100

        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
