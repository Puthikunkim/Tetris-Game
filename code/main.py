#Executes main game loop and combines everything together

import pygame,sys
from game import Game
from colours import Colours

pygame.init() #initialize pygame

title_font = pygame.font.Font(None, 40) #Set which font to use
score_surface = title_font.render("Score", True, Colours.white) #Stores score title surface object to be rendered
next_surface = title_font.render("Next", True, Colours.white) #Stores next block title surface object to be rendered
game_over_surface = title_font.render("GAME OVER", True, Colours.white) #Stores game over text surface object to be rendered

score_rect = pygame.Rect(320, 55, 170, 60) #Positions (top left) and dimensions of score rectangle
next_rect = pygame.Rect(320, 215, 170, 180) #Positions (top left) and dimensions of next block rectangle

screen = pygame.display.set_mode((500, 620)) #Set the display size
pygame.display.set_caption("Python Tetris") #Set the title of the window

clock = pygame.time.Clock() #Create a clock object

game = Game() #Create a game object

#Creates an event that is triggered every time the block's position needs to be updated (Every 200 ms)
GAME_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(GAME_UPDATE, 200)

#Main loop iterates as fast as it can
while True:
  #Event handling from the game
	for event in pygame.event.get():
   
    #If the user closes the window, the game will close
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
   
    #If the user presses a key
		if event.type == pygame.KEYDOWN:
			if game.game_over == True: #If the game is over, reset the game
				game.game_over = False
				game.reset()
			if event.key == pygame.K_LEFT and game.game_over == False: #If the user presses the left key, move the block left (given its not game over yet)
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False: #If the user presses the right key, move the block right (given its not game over yet)
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False: #If the user presses the down key, move the block down (given its not game over yet)
				game.move_down()
				game.update_score(0, 1) #Update the score (Adds 1 point for every block moved down)
			if event.key == pygame.K_UP and game.game_over == False: #If the user presses the up key, rotate the block (given its not game over yet)
				game.rotate()
    
    #If the event is the block's position update event (timer triggered), move the block down
		if event.type == GAME_UPDATE and game.game_over == False: 
			game.move_down()

	#Drawing things onto the screen
	score_value_surface = title_font.render(str(game.score), True, Colours.white) #Stores the score value text surface object to be rendered (Is in main loop as it needs to be updated every frame)

	screen.fill(Colours.dark_blue) #Fill the screen with a dark blue colour (Background colour)
	screen.blit(score_surface, (365, 20, 50, 50)) #Draw the score title onto the screen at the specified position (top left coordinates) and size
	screen.blit(next_surface, (375, 180, 50, 50)) #Draw the next block title onto the screen at the specified position (top left coordinates) and size

  #If the game is over, draw the game over text onto the screen at the specified position (top left coordinates) and size
	if game.game_over == True:
		screen.blit(game_over_surface, (320, 450, 50, 50))

	pygame.draw.rect(screen, Colours.light_blue, score_rect, 0, 5) #Draw the score rectangle onto the screen (with colour, position, dimensions and border width)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery)) #Draw the score value onto the screen at the center of the score rectangle
	pygame.draw.rect(screen, Colours.light_blue, next_rect, 0, 5) #Draw the next block rectangle onto the screen (with colour, position, dimensions and border width)
	game.draw(screen) #Draw the game section onto the screen

	pygame.display.update() #Update entire display
	clock.tick(60) #Set the frame rate to 60 fps (regulates how often the screen is updated, loop runs 60 times per second)