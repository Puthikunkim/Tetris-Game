import pygame
from colours import Colours
from position import Position

class Block:
  def __init__(self, id):
    self.id = id
    self.cells = {}
    self.cell_size = 30
    self.row_offset = 0
    self.column_offset = 0
    self.rotation_state = 0
    self.colors = Colours.get_cell_colours()

  def move(self, rows, columns):
    self.row_offset += rows
    self.column_offset += columns

  def get_cell_positions(self):
    tiles = self.cells[self.rotation_state]
    moved_tiles = []
    for position in tiles:
      position = Position(position.row + self.row_offset, position.column + self.column_offset)
      moved_tiles.append(position)
    return moved_tiles
  
  def draw(self, display):
    tiles = self.get_cell_positions()
    for tile in tiles:
      tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
      pygame.draw.rect(display, self.colors[self.id], tile_rect)