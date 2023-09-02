import pygame
import random
from itertools import permutations

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_RADIUS = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Pong Sorting Algorithm: Optimization and Efficiency Enhancement Procedure for High-Performance Data Sorting in Complex Computing Environments")

# Create paddles
player_paddle = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create a ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS // 2, SCREEN_HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddle speed
paddle_speed = 7

# AI movement
ai_speed = 5

# Scores
player_score = 0
ai_score = 0

# Create font
font = pygame.font.Font(None, 36)

askedArray = input("Array size? ")

# Initialize array and permutations
arr = list(range(int(askedArray)))
random.shuffle(arr)
permutations_list = list(permutations(arr))
permutations_remaining = len(permutations_list)

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the player's paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player_paddle.bottom < SCREEN_HEIGHT:
        player_paddle.y += paddle_speed

    # AI controls
    if ai_paddle.centery < ball.centery:
        ai_paddle.y += ai_speed
    elif ai_paddle.centery > ball.centery:
        ai_paddle.y -= ai_speed

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed_x *= -1

    # Ball collisions with screen boundaries
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Check for scoring
    if ball.left <= 0:
        ai_score += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS // 2, SCREEN_HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

        # Add a permutation back to the list
        if permutations_remaining < len(permutations_list):
            permutations_remaining += 1

    elif ball.right >= SCREEN_WIDTH:
        player_score += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS // 2, SCREEN_HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

        # Perform a permutation if there are remaining permutations
        if permutations_remaining > 0:
            random_index = random.randint(0, permutations_remaining - 1)
            arr = list(permutations_list[random_index])
            del permutations_list[random_index]
            permutations_remaining -= 1
            print(f"Array after permutation: {arr}")

    if is_sorted(arr):
        print(f"Sorted! {arr}")
        pygame.quit()
        quit()
        break

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    ai_text = font.render(f"AI: {ai_score}", True, WHITE)
    screen.blit(player_text, (20, 20))
    screen.blit(ai_text, (SCREEN_WIDTH - ai_text.get_width() - 20, 20))

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(FPS)
