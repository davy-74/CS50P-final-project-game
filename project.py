import pygame, time
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Platform hoarder")

# Clock
clock = pygame.time.Clock()

# Sounds
jumping_sound = pygame.mixer.Sound("Sound_files\jump_sound.mp3")
score_sound = pygame.mixer.Sound("Sound_files\score_sound.mp3")
game_over_sound = pygame.mixer.Sound("Sound_files\game_over_scream.mp3")


# Load and resize player and platform images
player_Img = pygame.image.load("Image_files/stick_man.png")
new_size = (32, 32)
resized_player_Img = pygame.transform.scale(player_Img, new_size)
playerX = 230
playerY = 480
playerY_change = -700
playerX_change = 0
speed =  400
gravity = 1000
jump_strength = 600
player_width = 30
player_height = 32
collision_rect_height = 5

# Initial player_rect representing the bottom part of the player image
player_rect = pygame.Rect(playerX, playerY + player_height - collision_rect_height, player_width, collision_rect_height).inflate(-12, 0)

# Loading and resizing platform image
platform_Img = pygame.image.load("Image_files/minus_sign.png")
new_size = (32, 32)
resized_platform_Img = pygame.transform.scale(platform_Img, new_size)


# Scoring system
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Function to return screen color based on score
def change_col(x):
    possible_colors = [(75, 0, 130), (139, 0, 0), (101, 67, 33), (64, 64, 64), (255, 0, 255), (255, 0, 0)]
    if x < 5:
        return (51, 255, 255)
    if 5 <= x < 10:
        return possible_colors[0]
    elif 10 <= x < 15:
        return possible_colors[1]
    elif 15 <= x < 20:
        return possible_colors[2]
    elif 20 <= x < 25:
        return possible_colors[3]
    elif 25 <= x < 30:
        return possible_colors[4]
    elif x >= 30:
        return possible_colors[5]

# Function that creates a list of rectangles
def create_platform_rects(howmany):

    # Defining initial position and offsets
    initial_x = 20  # Starting x position
    initial_y = 300 # Starting y position
    rect_list = []

    for _ in range(howmany):
        plat = resized_platform_Img.get_rect().inflate(1, -20)
        random_x = random.randint(2, 22)  # Random offset for x position
        random_y = random.randint(20, 300)  # Random offset for y position
        plat.top += -25
        plat.bottomleft = (initial_x * random_x, initial_y + random_y)
        rect_list.append(plat)
    return rect_list


# Function to create the game over screen
def game_over_screen(platforms):
    over_font = pygame.font.Font("freesansbold.ttf", 48)
    screen.fill((54, 61, 56))
    over_text = over_font.render(f"GAME OVER", True, (0, 255, 255))
    screen.blit(over_text, (100, 250))
    # Deletes all platforms
    platforms.clear()
    return platforms


# Incrementing score, adding boundaries for platforms and resetting platform
def increment_score():
    global score_value
    for object in platform_rectangles:
        if object.y >= 590 :
            score_value += 1
            score_sound.play()
            object.x = random.randint(30, 470)
            object.y = random.randint(50, 450)
        if object.x == 0:
            object.x = 0
        if object.x == 470:
            object.x = 470

# Function to draw the score on the screen
def show_score(x, y):
    score = font.render(f"Score: {str(score_value)}", True, (0, 0, 0))
    screen.blit(score, (x, y))


# Function to draw the player
def player(x, y):
    screen.blit(resized_player_Img, (x, y))

# Function to draw the platforms
def platform():
    for plat in platform_rectangles:
        screen.blit(resized_platform_Img, plat.topleft)


prev_time = time.time()
FPS = 60
# Game Loop
def main():
    global playerX, playerY, playerX_change, playerY_change, resized_player_Img, score_value, prev_time, platform_rectangles
    running = True
    facing_right = True
    platform_rectangles = create_platform_rects(7)
    # Variable for playing the game end scream only once
    gameover = False
    while running:
        # Calculating time between frames to use it as a multiplier for movement to decouple movement speed from framerate
        clock.tick(FPS)
        now = time.time()
        delta_time = now - prev_time
        prev_time = now

        # Event handler
        for event in pygame.event.get():

            # Quits the game
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -speed * delta_time
                    if facing_right:  # Only flip the image if the player was facing right
                        resized_player_Img = pygame.transform.flip(resized_player_Img, True, False)
                        facing_right = False

                elif event.key == pygame.K_RIGHT:
                    playerX_change = speed * delta_time
                    if not facing_right:  # Only flip the image if the player was facing left
                        resized_player_Img = pygame.transform.flip(resized_player_Img, True, False)
                        facing_right = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0



        # Updating player position
        playerY_change += gravity * delta_time
        playerX += playerX_change
        playerY += playerY_change * delta_time

        # Updating player_rect position
        player_rect.topleft = (playerX + 5, playerY + player_height - collision_rect_height)

        # Adding boundaries on sides of the game window
        if playerX <= 0:
            playerX = 0
        elif playerX >= 470:
            playerX = 470

        # Clear the screen
        screen.fill(change_col(score_value))

        # Draw player and platform
        player(playerX, playerY)
        platform()

        # Check for collision with any platform
        for plat in platform_rectangles:
            if plat.colliderect(player_rect):
                jumping_sound.play()
                playerY_change = -jump_strength
                plat.y += random.randint(5, 100)  # Move the platform down
                plat.x += random.randint(-100, 100) # Move the platform left or right
                if plat.x <= 0:
                    plat.x = 0
                elif plat.x >= 470:
                    plat.x = 470
                break

        # incrementing score
        increment_score()


        # Displaying game over screen and showing score
        if playerY >= 600:
            game_over_screen(platform_rectangles)
            playerX = 10
            playerY = 700
            if not gameover:
                gameover = True
                game_over_sound.play()

        show_score(textX, textY)


        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()