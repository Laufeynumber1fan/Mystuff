import heapq
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from Tile import Tile


# Function visualize_map
# Use matplot lib module to create plot that indicate all walls using rectangles; connections between tiles (with
#   arrow); and the path using a blue highlight
# Input : map_tiles : the list of list of Tile object, properly graphed
#         width_tiles : the size in width of the map_tiles 2D array
#         height_tiles : the size in height of the map_tiles 2D array
#         path to visualize : when input, it will display the path in blue
def visualize_map(map_tiles, width_tiles, height_tiles, path=None):
    # Some initialisations

    # Loop through all tiles to draw it

            # Draw a rectangle for the each tile

            # Draw a "S" for start and a "G" for goal
            # Draw The arrows depending if there are not any wall (opening) on the north, east, south and west side

    # Draw the path if provided
    # Prepare the plot to be display in a new window
    ...


# Function build_graph
# Using the images of walls (wall##.png), it performs cv2.matchTemplate on each tiles of the maze to detect what type of
# wall it is at each block
# Input : img_gray : Image of the maze loaded and converted to grayscale
#         width : Width of the whole maze
#         height : Height of the whole maze
# Output : 2D array of Tile objects
def build_graph(img_gray, width, height) -> list[list[Tile]]:
    # load all 4 wall##.png as grayscaled images using cv2

    # Initialize a list of list tilemap with value -1.
    # Loop though the maze image, 8x8 pixel bloc at a time, cutting it from the image to they compare it with each of
    # the walls. For each wal tested, take the one that has the highest result, and that is that idx (00 - 03) that will
    # be place in that tilemap position.

    # Once we have an 2D array of idx (00-03) we can use that to create another 2D array of Tile objects this time.

    # And return that 2D array of Tile Obj
    ...


# Function find_goal
# Using the images of walls (goal##.png), it performs cv2.matchTemplate on the whole maze image to find at which
# location the goal might be located
# Input : img_maze : Image of the maze loaded in color
# Output : (int, int) : the location in tile x and y of the goal
def find_goal(img_maze) -> (int, int):
    ...


# Function find_start
# Using the images of walls (start##.png), it performs cv2.matchTemplate on the whole maze image to find at which
# location the start might be located
# Input : img_maze : Image of the maze loaded in color
# Output : (int, int) : the location in tile x and y of the start
def find_start(img_maze) -> (int, int):
    ...


# Function pathfinding
# The heart of the Dijkstra's algorithm.
# Input : map_tiles : the 2D Array of Tile objects
#         pos_start : (int, int) start position of the maze
#         pos_goal : (int, int) goal position of the maze
# Output : list : the path found
def pathfinding(map_tiles, pos_start, pos_goal) -> list:
    # get start and goal tile objects

    # Priority queue to store the tiles to be processed

    # Dictionary to store the previous tile for each tile

    # Loop while the queue is not empty
        # Pop from the priority queue

        # If we are at destination, break

        # Loop Through all the current tile neighbours
                # Assuming each move has a cost of 1

                # If the neighboor greater distance than current distance, set it and push it to the queue,
                # update previous tiles

    # Reconstruct the path, from previous_tiles array

    # return the path
    ...


def main():
    sum_paths = 0
    for i in range(12):

        # Read snailmaze## in subdirectory 'image'
        filename = os.path.join(".", "images", "snailmaze{:02d}.png".format(i))
        img = cv2.imread(filename)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # call function to find the location of the start of the maze
        pos_start = find_start(img)
        print(pos_start)

        # call function to find the location of the goal of the maze
        pos_goal = find_goal(img)
        print(pos_goal)

        # call the function to build the Tiles array, and set the start and goal attribute accordingly
        map_tiles: [[Tile]] = build_graph(img_gray, 241, 129)
        map_tiles[pos_goal[1]][pos_goal[0]].is_goal = True
        map_tiles[pos_start[1]][pos_start[0]].is_start = True

        # call the pathfinding function to find the path in the maze. As a verification, let's get the total number
        # of step to each map to check that we properly accomplish the pathfinding algorithm
        path = pathfinding(map_tiles, pos_start, pos_goal)
        sum_paths += len(path)
        print(f"len(path) = {len(path)}")

        #As a bonus we want to display the path with matplotlib
        visualize_map(map_tiles, 30, 16, path)

    # return the sum of all the path lenghts
    print(sum_paths)


if __name__ == '__main__':
    main()
