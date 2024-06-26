import pygame, sys
from grid import Grid
from tetrominoes import *

pygame.init() # Initialize Pygame
dark_blue = (44, 44, 127) # Define a color using RGB values


display = pygame.display.set_mode((300, 600)) # 300x600 pixels is the size of the game window
pygame.display.set_caption('Tetris') # Title of the game window

clock = pygame.time.Clock() # Create a clock object to control the frame rate

game = Grid() # Create a Grid object
block = T() # Create an L block object
block.move(4, 3)

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user clicks the close button
            pygame.quit() # Quit Pygame
            sys.exit() # Exit the program

    # For drawing onto the screen
    display.fill(dark_blue) # Fill the screen with the color dark_blue
    game.draw(display) # Draw the grid (the game board) onto the screen
    block.draw(display)
    
    pygame.display.update() # Update the display
    clock.tick(60) # Limit the frame rate to 60 frames per second
            