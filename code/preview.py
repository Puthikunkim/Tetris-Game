from initialise import *

class Preview:
    def __init__(self):
        self.preview_surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*PREVIEW_HEIGHT_FRACTION))
        self.rectangle = self.preview_surface.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))
        self.display = pygame.display.get_surface()

    def run(self):
        self.display.blit(self.preview_surface, self.rectangle)