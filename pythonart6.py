import pygame
import sys
import random
import math

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fireworks Simulation")

clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 5)
        self.speed = random.uniform(2, 5)
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.speed -= 0.1  # simulate gravity

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

def create_firework_particles(x, y, num_particles):
    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    return [Particle(x, y, color) for _ in range(num_particles)]

def main():
    particles = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Update and draw particles
        for particle in particles:
            particle.move()
            particle.draw(screen)

        particles = [particle for particle in particles if particle.speed > 0]  # Remove faded particles

        # Create a new firework when the mouse is clicked
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            particles.extend(create_firework_particles(mx, my, 50))

        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
