# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

# Imports a game library that lets you use specific functions in your program.
import pygame
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
# This creates the screen and gives it the width and height specified as a 2 item sequence.
screen = pygame.display.set_mode((screen_width, screen_height))

# This creates the player and gives it the image found in this folder (similarly with the enemy image).

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
prize = pygame.image.load("prize.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later.

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy_height)

enemy2XPosition = screen_width +50
enemy2YPosition = random.randint(0, screen_height - enemy_height+50)

enemy3XPosition = screen_width -100
enemy3YPosition = random.randint(0, screen_height - enemy_height-100)

prizeXPosition = 900
prizeYPosition = 20

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False.
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other.

keyUpV = False
keyDownV = False

keyUpH = False
keyDownH = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

# This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later.
while 1:

    screen.fill(0)  # Clears the screen.
    # This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize,(prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.

            if event.key == pygame.K_UP or event.key == ord('w'):  # pygame.K_UP represents a keyboard key constant.
                keyUpV = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                keyDownV = True
            if event.key == pygame.K_LEFT or event.key == ord('a'):  # pygame.K_UP represents a keyboard key constant.
                keyUpH = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                keyDownH = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.

            if event.key == pygame.K_UP or event.key == ord('w'):
                keyUpV = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                keyDownV = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                keyUpH = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                keyDownH = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUpV == True:
        # This makes sure that the user does not move the player above the window.
        if playerYPosition > 0:
            playerYPosition -= 3
    if keyDownV == True:
        # This makes sure that the user does not move the player below the window.
        if playerYPosition < screen_height - image_height:
            playerYPosition += 3
    if keyUpH == True:
        # This makes sure that the user does not move the player above the window.
        if playerXPosition > 0:
            playerXPosition -= 3
    if keyDownH == True:
        # This makes sure that the user does not move the player below the window.
        if playerXPosition < screen_width - image_height:
            playerXPosition += 3

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemy:

    enemyBox1 = pygame.Rect(enemy.get_rect())
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition

    enemyBox2 = pygame.Rect(enemy.get_rect())
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition

    enemyBox3 = pygame.Rect(enemy.get_rect())
    enemyBox3.top = enemy3YPosition
    enemyBox3.left = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:

    if playerBox.colliderect(enemyBox1) or playerBox.colliderect(enemyBox2) or playerBox.colliderect(enemyBox3):

        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:

    if enemy1XPosition < 0 - enemy_width and enemy2XPosition < 0 - enemy_width and enemy3XPosition < 0 - enemy_width:

        # Display wining status to the user:

        print("You win!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    # Make enemy approach the player.

    enemy1XPosition -= 0.35
    enemy2XPosition -= 1.50
    enemy3XPosition -= 0.90


    if playerBox.colliderect(prizeBox): 

        # Display losing status to the user:

        print("You win!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)
