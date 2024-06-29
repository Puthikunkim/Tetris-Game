# Tetris

## Colors

### Tetromino Blocks
1. **I (Cyan)**: `rgb(0, 255, 255)`
2. **J (Blue)**: `rgb(0, 0, 255)`
3. **L (Orange)**: `rgb(255, 165, 0)`
4. **O (Yellow)**: `rgb(255, 255, 0)`
5. **S (Green)**: `rgb(0, 255, 0)`
6. **T (Purple)**: `rgb(128, 0, 128)`
7. **Z (Red)**: `rgb(255, 0, 0)`

### Other Colors
- **Title**: `rgb(255, 215, 0)` (Gold)
- **Background**: `rgb(0, 0, 0)` (Black)
- **Preview Section**: `rgb(50, 50, 50)` (Dark Grey)
- **Score Section**: `rgb(75, 75, 75)` (Medium Grey)

## Main
- Handles main game loop for the game to run:
  - Updates the display with every loop
  - Sets the frame rate for the game to operate at
- Renders the overall display for the game (User Interface):
  - The actual window for the game to display on, such as the score, next block, and game over title texts
- Continuously updates current score with every loop
- Calls on the game object to render the game grid, blocks, and the little sections that display the next block
- Takes user key inputs and calls on the game object to execute the corresponding game logic
- Handles when user closes the game
- Handles the timer that moves the block down continuously

## Colours
- Class attribute contains all colours of the game
- Class method **get_cell_colours** returns a list of all grid/tetromino colours, the first one is the grid empty colour followed by the tetromino colours indexed by the tetromino id

## Position
- Class that makes it easier to store the x, y position of a tetromino block on the grid. A position object is created for each tetromino block, with the first input as the row and the second input as the column, technically stored as (y, x) values.

## Block
- Parent class to all the possible tetrominoes where each instance is a particular tetromino
- Contains logic for manipulating all tetrominoes
- Responsible for tetrominoes that still need to be placed

### Attributes
- **id**: Identifies the particular tetromino created, which also indexes the colour of the tetromino from a list of all possible block colours
- **cells**: A dictionary that stores keys corresponding to possible rotation states for the tetromino and a value which is a list containing what position each block of the tetromino in that particular rotation state occupies
- **row.offset**: Stores the y offset of the tetromino from the left corner of the grid
- **column.offset**: Stores the x offset of the tetromino from the left corner of the grid
- **rotation_state**: Stores the current rotation state number of the tetromino of interest (initially set to 0 as it appears on the grid initially in this state)

### Methods
- **move**: Changes the values in **row.offset** and **column.offset** depending on how much the tetromino is to be moved by
- **get_cell_positions**: Returns a list of block positions of how much the tetromino of interest has moved by accessing the list of initial block positions based on current rotation state and applying total **row.offset** and **column.offset**
- **rotate**: Increments **rotation_state** and has a check for when **rotation_state** goes from the last state back to the first state
- **undo_rotation**: Decrements **rotation_state** and has a check for when **rotation_state** goes from the first state back to the last state
- **draw**: Gets how much tetromino has moved by from initial state by calling **get_cell_positions** and rendering all these blocks onto the screen (Method contains offset values so that it can render both the current block on the grid and the next block preview that is rendered under the next box section) and also accounts for cell size to be visible properly on the grid (Combination method)

## Tetrominoes
- Contains classes for all the different tetrominoes
- Each class is a child of the **Block** class

### Attributes
- Calls on the super constructor and provides it with the particular tetromino id 
- Overrides the **Block** cells attribute which is the dictionary for the list of positions for each rotation state
- Each position is based relatively to where it is located to the top left of a miniature grid that encompasses all possible rotations of the tetromino 
- Calls on the **Block** move method to offset the position of each block of the tetromino to the middle of the grid as it is initially in the top left of the game grid

## Grid
- Underlying logic for the game
- Contains check and manipulation methods for cells and rows

### Attributes
- Size is 20 rows by 10 columns
- Cell size is 30
- Grid is initially filled with 0 (a list of rows where each row is a list of columns) and changes value based on id of which tetromino block occupies the grid cell

### Methods
- **is_inside**: Checks if the specific cell is within the grid
- **is_empty**: Checks if the specific cell is empty (value of 0)
- **is_row_full**: Checks if all columns of the input row is not empty (value not 0)
- **clear_row**: Gives all columns of the input row a value of zero
- **move_row_down**: Takes an input that specifies how much the row should move down by, makes the current row zero, and copies all current row values to the target row to be moved down to
- **clear_full_rows**: Has a counter for how many rows have been filled, then checks every row in the grid incrementally and sees if it is full (Calls the **is_row_full** method) and clears it if it is (Calls the **clear_row** method), it then increments the counter. At each row if the row is not full then it is moved down based on how many rows have been completed up to this point. (Combination method)
- **reset**: Sets all grid cells to 0
- **draw**: Renders all grid cells to the screen where the colour of the grid cell corresponds to its number (changed based on which tetromino occupies it) in the nested list

## Game
- Main logic for the game that combines both the grid and block classes
- Handles the score updates
- Handles what to do with user keyboard inputs
- Handles logic for collision detection, and block validity
- Generates block to be placed onto the grid and next block to be placed.

### Attributes
- **grid**: Stores the grid object
- **blocks**: Stores a list of all possible tetrominoes
- **current_block**: Stores a random current block
- **next_block**: Stores a random next block
- **game_over**: Boolean to keep track of if the game is over
- **score**: Keeps track of player score

### Methods
- **update_score**: 100 points for 1 line cleared at one moment, 300 points for 2, 500 for 3, 1 point for each time the player moves the tetromino down
- **get_random_block**: Calls on the random module to randomly select a tetromino from the blocks list and removes it from the list, also checks if the list is empty and reverts it back to the full state if it is.
- **block_fits**: Checks if the tetromino can occupy the space it needs to be moved on the grid by calling the block **get_cell_positions** method which returns a list of how much the tetromino has moved by, and for each tetromino block it checks if the corresponding grid cell is empty by calling the grid **is_empty** method and returning True if it is, and False if it is not.
- **block_inside**: Checks if the tetromino is within the grid by calling the block **get_cell_positions** method which returns a list of how much the tetromino has moved by, and for each tetromino block it checks if the corresponding grid cell is within the grid by calling the grid **is_inside** method and returning True if it is, and False if it is not.
- **lock_block**: Calls the block **get_cell_positions** method which returns a list of how much the tetromino has moved by, it then iterates through each block of the tetromino and changes the corresponding grid cell to the value of the tetromino id in that position. After this, it sets the stored **next_block** to the **current_block** and calls **get_random_block** to get a new tetromino for the **next_block**. Finally, it calls on the grid method **clear_full_rows** which also returns how many rows were cleared that is used to call the **update_score** method, and it also calls the **block_fits** method to make sure the tetromino can still fit into the grid, if not then it is **game_over** (value is True).
- **move_left/move_right**: Calls the block **move** method on the **current_block** tetromino and provides it with a -1/+1 column offset, it also calls the **block_inside** and **block_fits** methods to check that when the tetromino is moved horizontally it doesn’t move outside the grid or move into a grid cell that is already occupied by an existing block. If it does then it undoes the move by calling the block **move** method again with the opposite column offset.
- **move_down**: Calls the block **move** method on the **current_block** tetromino and provides it with a +1 row offset, it also calls the **block_inside** and **block_fits** methods and does the same check and move undo as the **move_left/move_right** methods except with a -1 row offset and additionally calls on the **lock_block** method to lock the tetromino in place.
- **rotate**: Calls the block **rotate** method on the **current_block** tetromino, it also calls the **block_inside** and **block_fits** methods to check that when the tetromino is rotated it doesn’t move outside the grid or move into a grid cell that is already occupied by an existing block. If it does then it undoes the move by calling the block **undo_rotation** method.
- **reset**: Calls the grid **reset** method, reverts the blocks list back to its full state, and calls the **get_random_block** method again for both the **current_block** and **next_block** and makes the score 0.
- **draw**: Calls the grid **draw** method and the block **draw** method on the **current_block** with an 11 x and y offset to compensate for the game grid padding on the screen. It also calls the block **draw** method on the **next_block** to render it onto the middle of the next block preview section by utilizing the offset inputs where the O and I shapes have their specific offsets.

## Improvements to be made
- Increase block fall down speed as time advances
- Have different levels and scores
- Add sound
- Recognize continuous button presses and when keys are held down
- Have different game start and game over screens added
