import pygame
import sys
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake and food
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
font = pygame.font.Font(None, 72)

#function move snake
def move_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    return [head] + snake[:-1]

#Function snake grow
def grow_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    return [head] + snake

#function screen color
def draw(snake, food):
    screen.fill(BLACK)
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

#Function when game over 
def show_game_over():
    game_over_text = font.render("Game Over", True, RED)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BLACK)
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait 2 seconds before quitting
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    elif keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    elif keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    elif keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)
    elif keys[pygame.K_w] and direction != (0,CELL_SIZE):
        direction = (0, -CELL_SIZE)
    elif keys[pygame.K_s] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    elif keys[pygame.K_a] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    elif keys[pygame.K_d] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # Move and grow
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if new_head == food:
        snake = grow_snake(snake, direction)
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    else:
        snake = move_snake(snake, direction)

    # Collision
    if (new_head in snake[1:] or
        not 0 <= new_head[0] < WIDTH or
        not 0 <= new_head[1] < HEIGHT):
        print("Game Over!")
        running = False

    draw(snake, food)

#Quit
show_game_over()
pygame.quit()
sys.exit()
