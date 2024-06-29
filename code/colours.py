#Provides all the colours for the game

class Colours:
  
  #Colours for tetrominoes
	dark_grey = (26, 31, 40)
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
 
  #UI colours
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)

  #Returns a list of all the colours for the tetrominoes
	@classmethod
	def get_cell_colours(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]