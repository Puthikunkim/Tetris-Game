from colours import Colours
import pygame
from position import Position

#Parent class for all tetrominoes and is logic for block to placed on the grid (both current and next tetrominoess)
class Block:
	def __init__(self, id): #To create a block, we need to know its id. The id is used to identify what tetromino the block is part of and assign it a colour.
		self.id = id #Storing block id
		self.cells = {} #Storing the positions of the cells of the block in each rotation state
		self.cell_size = 30 #Storing the size of each cell in the grid
		self.row_offset = 0 #Storing the y offset of the block from the top corner of the grid
		self.column_offset = 0 #Storing the x offset of the block from the left corner of the grid
		self.rotation_state = 0 #Storing the current rotation state of the block
		self.colours = Colours.get_cell_colours() #List storing all possible colours for the blocks

  #Takes how many rows and columns to move and stores it in their respecting offsets depending on the input parameters.
	def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns

  #Returns the positions of the cells of the tetromino in the current rotation state after applying the offsets.
	def get_cell_positions(self):
		tiles = self.cells[self.rotation_state] #List of the cell positions in the current rotation state
		moved_tiles = [] #List to store the cell positions after applying the offsets to the block
		for position in tiles: #Iterating through each cell position in the current rotation state list
			position = Position(position.row + self.row_offset, position.column + self.column_offset) #Creating a new cell position based on the offsets to the initial cell position
			moved_tiles.append(position) #Adding the new cell position to the list of moved cell positions
		return moved_tiles 

  #Rotates the block by incrementing the rotation state by 1. If the rotation state is one greater than the last one, it will loop back to the first rotation state.
	def rotate(self):
		self.rotation_state += 1
		if self.rotation_state == len(self.cells):
			self.rotation_state = 0

  #Undoes the rotation of the block by decrementing the rotation state by 1. If the rotation state is -1, it will loop back to the last rotation state.
	def undo_rotation(self):
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1

  #Draws the tetromino onto the screen at the given offset position (the offsets are used to position where the current and next block should in the grid)
	def draw(self, screen, offset_x, offset_y):
		tiles = self.get_cell_positions() #List of the cell positions of the block after applying the offsets
		for tile in tiles: #Iterating through each cell position in the list
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) #Creating a rectangle object for each block of the tetromino (x,y,w,h)
			pygame.draw.rect(screen, self.colours[self.id], tile_rect) #Drawing the rectangle onto the screen with the colour of the block (from the list) specified by its id