from initialise import *

class Score:
    def __init__(self):
        self.score_surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*SCORE_HEIGHT_FRACTION-PADDING))
        self.rectangle = self.score_surface.get_rect(bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display = pygame.display.get_surface()

    def run(self):
        self.display.blit(self.score_surface, self.rectangle)