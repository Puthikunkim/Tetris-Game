from initialise import *

class Game:
    def __init__(self):
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT)) # Creates a game surface
        self.display = pygame.display.get_surface() # Gets the display surface
    
    def run(self):
        self.display.blit(self.game_surface, (0, 0)) # Puts the game surface on the display