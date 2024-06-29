from grid import Grid
from tetrominoes import *
import random
import pygame

#Game class that represents the game state and logic
class Game:
	def __init__(self):
		self.grid = Grid() #Creating a grid object to represent the game grid
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] #List of all possible tetrominoes
		self.current_block = self.get_random_block() #Current block that is falling
		self.next_block = self.get_random_block() #Next block that will fall after the current block
		self.game_over = False #Flag to indicate if the game is over
		self.score = 0 #Player's score initially set to 0

  #Updates the score based on the number of lines cleared and the number of points for moving the block down
	def update_score(self, lines_cleared, move_down_points):
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared == 3:
			self.score += 500
		self.score += move_down_points

  #Returns a random block from the list of all possible tetrominoes
	def get_random_block(self):
		if len(self.blocks) == 0: #If there are no more blocks in the list, refill the list with all possible tetrominoes
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		block = random.choice(self.blocks) #Select a random tetromino from the list
		self.blocks.remove(block) #Remove the selected tetromino from the list
		return block

  #Moves the current block to the left
	def move_left(self):
		self.current_block.move(0, -1) #Decrease the column offset by 1
		if self.block_inside() == False or self.block_fits() == False: #If the block is not inside the grid or does not fit, undo the move
			self.current_block.move(0, 1)

  #Moves the current block to the right
	def move_right(self):
		self.current_block.move(0, 1) #Increase the column offset by 1
		if self.block_inside() == False or self.block_fits() == False: #If the block is not inside the grid or does not fit, undo the move
			self.current_block.move(0, -1)

  #Moves the current block down
	def move_down(self):
		self.current_block.move(1, 0) #Increase the row offset by 1
		if self.block_inside() == False or self.block_fits() == False: #If the block is not inside the grid or does not fit, undo the move and lock the block
			self.current_block.move(-1, 0)
			self.lock_block()

  #Locks the current block in place on the grid and updates the game state
	def lock_block(self):
		tiles = self.current_block.get_cell_positions() #Get the cell positions of the current block after applying the offsets
		for position in tiles: #Iterate through each cell position
			self.grid.grid[position.row][position.column] = self.current_block.id #Set the grid cell to the id of the block
		self.current_block = self.next_block #Set the current block to the next block
		self.next_block = self.get_random_block() #Get a new random block for the next block
		rows_cleared = self.grid.clear_full_rows() #Clear any full rows in the grid and get the number of rows cleared
		if rows_cleared > 0: #If any rows were cleared, update the score
			self.update_score(rows_cleared, 0)
		if self.block_fits() == False: #If the new block does not fit, the game is over
			self.game_over = True

  #Resets the game state
	def reset(self):
		self.grid.reset() #Reset the grid by setting all cells to 0
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] #Refill the list of all possible tetrominoes
		self.current_block = self.get_random_block() #Get a new random block for the current block
		self.next_block = self.get_random_block() #Get a new random block for the next block
		self.score = 0 #Reset the score to 0

  #Checks if the current block fits inside the grid
	def block_fits(self):
		tiles = self.current_block.get_cell_positions() #Get the cell positions of the current block after applying the offsets
		for tile in tiles: #Iterate through each cell position
			if self.grid.is_empty(tile.row, tile.column) == False: #If the cell is not empty, the block does not fit
				return False
		return True

  #Rotates the current block
	def rotate(self):
		self.current_block.rotate() #Rotate the block
		if self.block_inside() == False or self.block_fits() == False: #If the block is not inside the grid or does not fit, undo the rotation
			self.current_block.undo_rotation()

  #Checks if the current block is inside the grid
	def block_inside(self):
		tiles = self.current_block.get_cell_positions() #Get the cell positions of the current block after applying the offsets
		for tile in tiles: #Iterate through each cell position
			if self.grid.is_inside(tile.row, tile.column) == False: #If the cell is not inside the grid, the block is not inside the grid
				return False
		return True

  #Draws the game elements onto the screen
	def draw(self, screen):
		self.grid.draw(screen) #Draw the grid onto the screen
		self.current_block.draw(screen, 11, 11) #Draw the current block onto the screen (offset is 11 for the padding of the grid and the block initial position is accounted for in the draw method)

    #Draw the next block onto the screen into the next block rectangle
		if self.next_block.id == 3:
			self.next_block.draw(screen, 255, 290)
		elif self.next_block.id == 4:
			self.next_block.draw(screen, 255, 280)
		else:
			self.next_block.draw(screen, 270, 270)