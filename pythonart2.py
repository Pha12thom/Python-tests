import pygame
import sys

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Beating Heart Animation")

clock = pygame.time.Clock()

def draw_heart(surface, x, y):
    pygame.draw.polygon(surface, (255, 0, 0), [(x, y-30), (x+20, y-60), (x+40, y-30)])
    pygame.draw.polygon(surface, (255, 0, 0), [(x+40, y-30), (x+60, y-60), (x+80, y-30)])
    pygame.draw.polygon(surface, (255, 0, 0), [(x, y-30), (x+80, y-30), (x+40, y+40)])

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the screen with white
        draw_heart(screen, 400, 300)  # Draw the heart at the center
        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
