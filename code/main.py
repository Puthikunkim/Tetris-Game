from initialise import *
from sys import exit 
class Main:
    def __init__(self):
        pygame.init() 
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display 
            self.display.fill(GRAY)

            # update display  
            pygame.display.update()
            self.clock.tick(60)
            

if __name__ == '__main__':
    main = Main()
    main.run()