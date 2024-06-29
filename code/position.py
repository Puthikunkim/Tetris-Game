#Object to store the position of a tetromino block on the grid as (y,x) values
class Position:
	def __init__(self, row, column):
		self.row = row
		self.column = column