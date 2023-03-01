import pygame
import sys
import time
bos = 0
jump = 0
# Initialize Pygame and set screen size
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
#Engel 3'ü getirmek için
engel = 0

# Load player, background, obstacle, finish and black images
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()
obstacle_image = pygame.image.load("engel.png")
obstacle_rect1 = obstacle_image.get_rect()
obstacle_rect2 = obstacle_image.get_rect()
obstacle_rect3 = obstacle_image.get_rect()
finish_image = pygame.image.load("finish.png")
finish_rect = finish_image.get_rect()
black_image = pygame.image.load("black.png")
black_rect = black_image.get_rect()
black_rect1 = black_image.get_rect()
black_rect2 = black_image.get_rect()
black_rect3 = black_image.get_rect()
# Set platform position and size
platform_rect = pygame.Rect(0, height - 40, width, 40)
# Set obstacle positions
background_rect.centerx = 400
background_rect.centery = 300
obstacle_rect1.centerx = 200
obstacle_rect1.bottom = platform_rect.top
obstacle_rect2.centerx = 500
obstacle_rect2.bottom = platform_rect.top
#Set black positions
black_rect.centerx = 100
black_rect.bottom = platform_rect.top - 48
black_rect1.centerx = 300
black_rect1.bottom= platform_rect.top - 96
# Set finish position
finish_rect.right = width
finish_rect.bottom = platform_rect.top
# Initialize player position and gravity
player_rect.centerx = 0
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

    if player_rect.centerx >= 32 and player_rect.centerx <= 178:
        armut = 1
    else:
        armut = 0

    if player_rect.centerx >= 225 and player_rect.centerx <= 375:
        elma = 1
    else:
        elma = 0

    if keys[pygame.K_w] and player_rect.centery == 414 and engel == 2 and elma == 1:
        player_velocity = -10
    if keys[pygame.K_w] and player_rect.centery == 462 and armut == 1:
        player_velocity = -10


    if keys[pygame.K_w] and player_rect.bottom == platform_rect.top:
        player_velocity = -10


    player_velocity += gravity
    player_rect.top += player_velocity
    if player_rect.bottom >= platform_rect.top:
        player_rect.bottom = platform_rect.top
        player_velocity = 0
    if player_rect.bottom >= black_rect1.top and player_rect.colliderect(black_rect1) and engel == 2:
        player_rect.bottom = black_rect1.top
        player_velocity = 0
    if player_rect.bottom >= black_rect.top and player_rect.colliderect(black_rect):
        player_rect.bottom = black_rect.top
        player_velocity = 0


    if keys[pygame.K_a]:
        player_rect.centerx -= 5



    if keys[pygame.K_d]:
        player_rect.centerx += 5

    if keys[pygame.K_w]:
        bos = 1


    if player_rect.centery >= 462 and armut == 1:
        player_velocity += 1.334
    elif player_rect.colliderect(black_rect):
        player_rect.top = black_rect.bottom - player_rect.height - 18

    if player_rect.centery >= 414 and engel == 2 and elma == 1:
        player_velocity += 1.334
    elif engel == 2 and player_rect.colliderect(black_rect1):
        player_rect.top = black_rect1.bottom - player_rect.height - 18


    if keys[pygame.K_w]:
        bos = 1
        print(player_rect.centerx)


    else:
        bos = 0



    # Keep player within screen bounds
    player_rect.clamp_ip(screen.get_rect())

    # Check if player collides with obstacle
    if engel != 2:
        if player_rect.colliderect(obstacle_rect1) or player_rect.colliderect(obstacle_rect2) or player_rect.colliderect(obstacle_rect3):
            player_rect.centerx = 30
            player_rect.bottom = platform_rect.top



    # Load finish gate image
    finish_image = pygame.image.load("finish.png")
    finish_rect = finish_image.get_rect()
    finish_rect.right =  width
    finish_rect.bottom = platform_rect.top


    # Check if player reaches the finish gate
    if player_rect.colliderect(finish_rect):
        engel += 1
        # Remove obstacles
        obstacle_rect1.centerx = -100
        obstacle_rect2.centerx = -50
        obstacle_rect3.centerx = -50
        # Teleport player to bottom left corner
        player_rect.centerx = 30
        player_rect.bottom = platform_rect.top
        # Add 3 new obstacles
        obstacle_rect1.centerx = width / 4
        obstacle_rect1.bottom = platform_rect.top
        obstacle_rect2.centerx = width / 2
        obstacle_rect2.bottom = platform_rect.top
        obstacle_rect3.centerx = width * 3 / 4
        obstacle_rect3.bottom = platform_rect.top


    # Check if player reaches the finish gate1
    if player_rect.colliderect(finish_rect) and engel == 2:
        engel += 1
        # Remove obstacles
        obstacle_rect1.centerx = -100
        obstacle_rect2.centerx = -50
        obstacle_rect3.centerx = -50
        # Teleport player to bottom left corner
        player_rect.centerx = 30
        player_rect.bottom = platform_rect.top



    # Re-display platform, player, and obstacle
    screen.fill((255, 255,255))
    #Background
    #screen.blit(background_image, background_rect)

    #Draw platform and obstacles
    pygame.draw.rect(screen, (0, 0, 0), platform_rect)
    if engel != 2:
        screen.blit(obstacle_image, obstacle_rect1)
        screen.blit(obstacle_image, obstacle_rect2)
    screen.blit(black_image,black_rect)

    if engel == 1:
        screen.blit(obstacle_image, obstacle_rect3)
    if engel == 2:
        screen.blit(black_image, black_rect1)
    # Draw finish gate
    screen.blit(finish_image, finish_rect)

    # Draw player
    screen.blit(player_image, player_rect)

    # Update screen
    pygame.display.update()

    # Set game speed
    clock.tick(60)
