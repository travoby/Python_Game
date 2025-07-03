import pygame;
import sys;

# Initialize Pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Square")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)

# Player (square) setup
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keypress movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Draw the player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit to 60 FPS

# Exit
pygame.quit()
sys.exit()
