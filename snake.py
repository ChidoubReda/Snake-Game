import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the title of the window
pygame.display.set_caption('Snake Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Define game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
food_spawn = True
score = 0

# Create a clock object
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!= 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction!= 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction!= 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction!= 'LEFT':
                change_to = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    # Update the snake body
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
        food_spawn = True

    # Check for collision with the edge
    if snake_pos[0] < 0 or snake_pos[0] > screen_width - 10:
        pygame.quit()
        sys.exit()
    elif snake_pos[1] < 0 or snake_pos[1] > screen_height - 10:
        pygame.quit()
        sys.exit()

    # Check for collision with the snake body
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    # Update the direction
    direction = change_to

    # Draw everything
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    pygame.display.update()

    # Cap the frame rate
    clock.tick(10)