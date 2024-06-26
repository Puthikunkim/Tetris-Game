from colours import Colours

class Block:
  def __init__(self, id):
    self.id = id
    self.cells = {}
    self.cell_size = 30
    self.rotation_state = 0
    self.colors = Colours.get_cell_colours()

  def draw(self, display):
    
    