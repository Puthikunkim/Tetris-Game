from initialise import *

class Game:
    def __init__(self):
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT)) # Creates a game surface
        self.display = pygame.display.get_surface() # Gets the display surface
        self.rectangle = self.game_surface.get_rect(topleft=(PADDING, PADDING))
    
    def draw_grid(self):
        for col in range(1, COLUMNS): 
            x = col * CELL_SIZE
            pygame.draw.line(self.game_surface, LINE_COLOR, (x, 0), (x, self.game_surface.get_height()), 1)
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.game_surface, LINE_COLOR, (0, y), (self.game_surface.get_width(), y), 1)
    
    def run(self):
        self.draw_grid()
        self.display.blit(self.game_surface, (PADDING, PADDING)) # Puts the game surface on the display
        pygame.draw.rect(self.display, LINE_COLOR, self.rectangle, 2, 2) # Draws a rectangle around the game surface