import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Rocket Launch")

# Print current working directory for debugging
print("Current Working Directory:", os.getcwd())

# Load rocket image (make sure the file is in the same folder or set full path properly)
try:
    rocket_image = pygame.image.load("ML/VehicleDetectionApp/rocket.py")  # or use a full path like r"D:\python\ML\rocket.png"
except pygame.error as e:
    print("Error loading rocket.png:", e)
    pygame.quit()
    sys.exit()

# Resize the rocket
rocket_image = pygame.transform.scale(rocket_image, (100, 100))
rocket_rect = rocket_image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

# Background color
BLACK = (0, 0, 30)

# Clock to control frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move rocket upward
    rocket_rect.y -= 2
    if rocket_rect.bottom < 0:
        rocket_rect.y = HEIGHT

    # Draw rocket
    screen.blit(rocket_image, rocket_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Clean up
pygame.quit()
sys.exit()
