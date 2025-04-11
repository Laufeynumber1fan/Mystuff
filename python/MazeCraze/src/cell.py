from cv2 import matchTemplate, TM_CCOEFF_NORMED
import numpy as np

# Handles the initliasation and properties of each 9x9 cell in the image

class cell:
    # xy1 - (x, y) of the top-left px of the cell
    # xy2 - top right
    # xy3 - bottom left
    # xy4 - bottom right
    def __init__(self, maze, xy1, xy4, blank, wall):
        self.xy1 = xy1
        self.xy2 = (xy1[0], xy1[1] + 8)
        self.xy3 = (xy4[0], xy4[1] - 8)
        self.xy4 = xy4
        self.center = (xy1[0] + 4, xy1[1] + 4)
        self.special = None

        # if wall is present on a direction it will be false
        # LEFT, TOP, RIGHT, BOTTOM
        self.valids = [
            self.is_wall(maze, self.xy1, self.xy3, blank, wall),
            self.is_wall(maze, self.xy1, self.xy2, blank, wall),
            self.is_wall(maze, self.xy2, self.xy4, blank, wall),
            self.is_wall(maze, self.xy3, self.xy4, blank, wall)
        ]
        #self.special = self.is_special(maze, (self.xy1[0] + 1, self.xy1[1] + 1))
    
    def is_wall(self, maze, a, b, blank, wall):
        ax = a[0]
        ay = a[1]
        bx = b[0]
        by = b[1]
        check = [a]
        wall_count = 0

        # directional check
        # if vertical
        if ay == by:
            for i in range(1, 9):
                check.append((ax + i, ay))

        # is horizontal
        # ax == bx
        else:
            for i in range(1, 9):
                check.append((ax, ay + i))

        # check becomes a list of coordinates between a and b
        # use this list of coords to save the px values between a and b
        for c in check:
                if maze[c[0]][c[1]] == wall:
                    wall_count += 1

        # if half of the 8 pixels are not walls then return True as a valid path
        if wall_count <= 4:
            return True
        else:
            return False

    def is_special(self, maze, snail, goal):
        # a is top left corner of the cell + 1 and -1 from the bottom right
        # For example, when plugging the cell on (0, 0), (8, 8). The a and b values would be (1, 1), (7, 7)

        # checker is a manually generated img based on the 8x8 area inside a 9x9 cell
        # cv2.matchTemplate is then used to compare checker to a 8x8 images of ../images/snail.png and ../images/goal.png
        ax = self.xy1[0] + 1
        ay = self.xy1[1] + 1
        checker = np.empty((7, 7), dtype='uint8')
        for x in range(0, 7):
            for y in range(0, 7):
                checker[x][y] = maze[ax + y][ay + x]

        result1 = float(matchTemplate(checker, snail, TM_CCOEFF_NORMED))
        if result1 >= 0.1:
            #
            print(f'DEBUG: Cell starting at ({self.xy1[0]}, {self.xy1[1]}) has the snail')
            self.special = 'snail'
            return "snail"
        
        result2 = float(matchTemplate(checker, goal, TM_CCOEFF_NORMED))
        if result2 >= 0.1:
            #
            print(f'DEBUG: Cell starting at ({self.xy1[0]}, {self.xy1[1]}) has the goal')
            self.special = 'goal'
            return "goal"
        
        # FOR DEBUGGING
        if result1 > 0.0 or result1 > 0.0:
            return (result1, result2)
        
        else:
            return None
            