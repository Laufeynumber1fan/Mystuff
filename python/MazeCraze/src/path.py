
# Handles the pathmaking and tracking of used cells to travel through the maze

class path:
    def __init__(self, start, finish):
        self.route = [start]
        self.pointer = start
        self.finish = finish

    def traverse(self, destination):
        # save last cell
        self.route.append(destination)
        self.pointer = destination