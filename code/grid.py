import pygame

class Grid:
  def __init__(self):
    self.rows = 20
    self.cols = 10
    self.cell_size = 30
    self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
    self.colours = self.get_cell_colours()

  def draw_grid(self): # prints each value of the grid to the console
    for i in range(self.rows):
      for j in range(self.cols):
        print(self.grid[i][j], end=' ')
        print()

  def get_cell_colours(self): # Define the colours of the cells corresponding to the different tetrominoes

    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)

    return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

  def draw(self, display):
    for i in range(self.rows):
      for j in range(self.cols):
        cell_value = self.grid[i][j]
        cell_rect = pygame.Rect(j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(display, self.colours[cell_value], cell_rect)
        