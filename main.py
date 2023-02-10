import pygame
import sys

# Initialize Pygame and set screen size
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
#Engel 3'ü getirmek için
engel = 0
# Load player and obstacle images
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
obstacle_image = pygame.image.load("engel.png")
obstacle_rect1 = obstacle_image.get_rect()
obstacle_rect2 = obstacle_image.get_rect()
obstacle_rect3 = obstacle_image.get_rect()
finish_image = pygame.image.load("finish.png")
finish_rect = finish_image.get_rect()

# Set platform position and size
platform_rect = pygame.Rect(0, height - 20, width, 20)

# Set obstacle positions
obstacle_rect1.centerx = 200
obstacle_rect1.bottom = platform_rect.top
obstacle_rect2.centerx = 500
obstacle_rect2.bottom = platform_rect.top

# Set finish position
finish_rect.right = width - 10
finish_rect.bottom = platform_rect.top

# Initialize player position and gravity
player_rect.left = 0
player_rect.bottom = platform_rect.top
player_velocity = 0
gravity = 0.5

# Initialize game loop variables
clock = pygame.time.Clock()
game_running = False
obstacle_on = True

# Function to display play button
def display_play_button():
    play_button_image = pygame.image.load("images.png")
    play_button_rect = play_button_image.get_rect()
    play_button_rect.centerx = width // 2
    play_button_rect.centery = height // 2
    screen.blit(play_button_image, play_button_rect)
    pygame.display.update()
    screen.fill((255, 255, 255))


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if not game_running:
                play_button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
                if play_button_rect.collidepoint(mouse_pos):
                    game_running = True

    if not game_running:
        display_play_button()
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_rect.bottom == platform_rect.top:
        player_velocity = -10
    player_velocity += gravity
    player_rect.top += player_velocity
    if player_rect.bottom >= platform_rect.top:
        player_rect.bottom = platform_rect.top
        player_velocity = 0
    if keys[pygame.K_a]:
        player_rect.left -= 5
    if keys[pygame.K_d]:
        player_rect.right += 5

    # Keep player within screen bounds
    player_rect.clamp_ip(screen.get_rect())

    # Check if player collides with obstacle
    if player_rect.colliderect(obstacle_rect1) or player_rect.colliderect(obstacle_rect2) or player_rect.colliderect(obstacle_rect3):
        player_rect.left = 0
        player_rect.bottom = platform_rect.top

    # Load finish gate image
    finish_image = pygame.image.load("finish.png")
    finish_rect = finish_image.get_rect()
    finish_rect.right =  width
    finish_rect.bottom = height - 20

    # Check if player reaches the finish gate
    if player_rect.colliderect(finish_rect):
        engel += 1
        # Remove obstacles
        obstacle_rect1.centerx = -100
        obstacle_rect2.centerx = -50
        # Teleport player to bottom left corner
        player_rect.left = 0
        player_rect.bottom = platform_rect.top
        # Add 3 new obstacles
        obstacle_rect1.centerx = width / 4
        obstacle_rect1.bottom = platform_rect.top
        obstacle_rect2.centerx = width / 1.83
        obstacle_rect2.bottom = platform_rect.top
        obstacle_rect3 = obstacle_image.get_rect()
        obstacle_rect3.centerx = 3 * width / 3.60
        obstacle_rect3.bottom = platform_rect.top

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw platform and obstacles
    pygame.draw.rect(screen, (0, 0, 0), platform_rect)
    screen.blit(obstacle_image, obstacle_rect1)
    screen.blit(obstacle_image, obstacle_rect2)

    if engel == 1:
        screen.blit(obstacle_image, obstacle_rect3)

    # Draw finish gate
    screen.blit(finish_image, finish_rect)

    # Draw player
    screen.blit(player_image, player_rect)

    # Update screen
    pygame.display.update()

    # Set game speed
    clock.tick(60)