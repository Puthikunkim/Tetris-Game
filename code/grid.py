import pygame
from colours import Colours

class Grid:
  def __init__(self):
    self.rows = 20
    self.cols = 10
    self.cell_size = 30
    self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
    self.colours = Colours.get_cell_colours()

  def draw_grid(self): # prints each value of the grid to the console
    for i in range(self.rows):
      for j in range(self.cols):
        print(self.grid[i][j], end=' ')
        print()

  def draw(self, display):
    for i in range(self.rows):
      for j in range(self.cols):
        cell_value = self.grid[i][j]
        cell_rect = pygame.Rect(j*self.cell_size + 1, i*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
        pygame.draw.rect(display, self.colours[cell_value], cell_rect)
        