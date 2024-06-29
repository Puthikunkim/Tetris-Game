import pygame
from colours import Colours

#Grid class that represents the game grid
class Grid:
	def __init__(self):
		self.num_rows = 20 #Number of rows in the grid
		self.num_cols = 10 #Number of columns in the grid
		self.cell_size = 30 #Size of each cell in the grid
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] #2D list to store the grid initially filled with 0s (20x10)
		self.colours = Colours.get_cell_colours() #List of colours for the grid cells

  #Prints the grid values to the console
	def print_grid(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				print(self.grid[row][column], end = " ")
			print()

  #Checks if a cell in a given row and column is inside the grid
	def is_inside(self, row, column):
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False

  #Checks if a cell in a given row and column is empty
	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False

  #Checks if a row is filled with blocks
	def is_row_full(self, row):
		for column in range(self.num_cols):
			if self.grid[row][column] == 0: #If any cell in the row is empty, return False
				return False
		return True

  #Clears a row by setting all its cells to 0
	def clear_row(self, row):
		for column in range(self.num_cols):
			self.grid[row][column] = 0

  #Moves a row down by a certain number of rows and clears the original row
	def move_row_down(self, row, num_rows):
		for column in range(self.num_cols):
			self.grid[row+num_rows][column] = self.grid[row][column]
			self.grid[row][column] = 0

  #Clears all full rows in the grid and moves the rows above down
	def clear_full_rows(self):
		completed = 0 #Counter for the number of completed rows up to this point
		for row in range(self.num_rows-1, 0, -1): #Iterating from the bottom row to the top row of the grid
			if self.is_row_full(row): #If the row is full, clear it
				self.clear_row(row)
				completed += 1 #Increment the completed rows counter
			elif completed > 0: #If the row is not full but there are completed rows, move the row down by the number of completed rows so far
				self.move_row_down(row, completed)
		return completed

  #Resets the grid by setting all cells to 0
	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0

  #Draws the grid onto the screen
	def draw(self, screen):
    #Iterating through each cell in the grid
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				cell_value = self.grid[row][column] #Get the value of the cell in the grid
				cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
				self.cell_size -1, self.cell_size -1) #Create a rectangle object for the cell (x,y,w,h) the offsets of 11 are the padding of the grid and -1 is to create a gap between cells
				pygame.draw.rect(screen, self.colours[cell_value], cell_rect) #Draw the cell onto the screen with the colour specified by the cell value