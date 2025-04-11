
class Tile:
    # Constructor of a tile object
    #       Create all attributes, reference to tiles north, south, east, wet, is_start, is_goal, distance, position.
    #       Only position gets initialize with x, and y. the rest gets default values.
    #   input X, Y
    def __init__(self, x, y):
        ...

    # Method set_north
    #   set the north tile reference to the tile obj in argument
    def set_north(self, tile):
        ...

    # Method set_east
    #   set the east tile reference to the tile obj in argument
    def set_east(self, tile):
        ...

    # Method set_south
    #   set the south tile reference to the tile obj in argument
    def set_south(self, tile):
        ...

    # Method set_west
    #   set the west tile reference to the tile obj in argument
    def set_west(self, tile):
        ...

    # Method __lt__
    #   Used with the < operator when comparing 2 tiles, retun the comparaision of the distance attribut
    def __lt__(self, other):
        ...

    # get_id()
    #   return the posibition as id
    def get_id(self):
        ...
