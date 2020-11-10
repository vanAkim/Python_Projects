# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, rat_char, row_start, col_start):
        ' (Rat, str, int, int) -> NoneType​'

        self.symbol = rat_char
        self.row = row_start
        self.col = col_start
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        ''' (Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.

        '''

        self.row = row
        self.col = col

    def eat_sprout(self):
        ''' (Rat) -> NoneType

        Add one to the rat's instance variable num_sprouts_eaten.
        '''

        self.num_sprouts_eaten += 1

    def __str__(self):
        ''' (Rat) -> str

        Return a string representation of the rat with it's name, location and the number
        of sprouts eaten

        >>> print(Rat_ex)
        >>> 'J at (4, 3) ate 2 sprouts.'
        '''

        return str('{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten))

class Maze:
    """ A 2D maze. """

    def __init__(self, maze_map, rat_1, rat_2):
        ' (Maze, list of list of str, Rat, Rat) -> NoneType '

        self.maze = maze_map
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        self.num_sprouts_left = 0
        for item in self.maze:
            self.num_sprouts_left += item.count(SPROUT)

    def is_wall(self, row, col):
        ' (Maze, int, int) -> bool​'

        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        ' (Maze, int, int) -> str​'

        if [self.rat_1.row, self.rat_1.col] == [row, col]:
            return self.rat_1.symbol
        elif [self.rat_2.row, self.rat_2.col] == [row, col]:
            return self.rat_2.symbol

        return self.maze[row][col]

    def move(self, rat, vert_dir, hori_dir):
        ' (Maze, Rat, int, int) -> bool​'

        updated_row = rat.row + vert_dir
        updated_col = rat.col + hori_dir

        if self.maze[updated_row][updated_col] == WALL:
            return None
        elif self.maze[updated_row][updated_col] == SPROUT:
            rat.eat_sprout()
            self.maze[updated_row][updated_col] = HALL

        rat.set_location(updated_row, updated_col)
        return True

    def __str__(self):
        maze = ''
        for item in self.maze:
            maze = maze + ''.join(item) + '\n'

        maze = maze[:self.rat_1.row*len(self.maze[0]) + self.rat_1.col + self.rat_1.row] + self.rat_1.symbol + maze[self.rat_1.row*len(self.maze[0]) + self.rat_1.col + 1 + self.rat_1.row:]
        maze = maze[:self.rat_2.row*len(self.maze[0]) + self.rat_2.col + self.rat_2.row] + self.rat_2.symbol + maze[self.rat_2.row*len(self.maze[0]) + self.rat_2.col + 1 + self.rat_2.row:]
        return str(maze) + str(self.rat_1) + '\n' + str(self.rat_2)

