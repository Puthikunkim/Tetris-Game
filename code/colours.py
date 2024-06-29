#Provides all the colours for the game

class Colours:
  
  #Colours for tetrominoes
	dark_grey = (26, 31, 40)
	green = (0, 255, 0)
	red = (255, 0, 0)
	orange = (255, 165, 0)
	yellow = (255, 255, 0)
	purple = (128, 0, 128)
	cyan = (0, 255, 255)
	blue = (0, 0, 255)
 
  #UI colours
	white = (255, 255, 255)
	dark_blue = (0, 0, 0)
	light_blue = (50, 50, 50)

  #Returns a list of all the colours for the tetrominoes
	@classmethod
	def get_cell_colours(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]