### Maze Pathfinding Challenge
For a little background this lab was a past project given to previous classes by one of my instructors. It involves a bit of CS fundamentals like using data structures and the Djikastra algorithm but the main kicker of the lab is applying the code into solving a practical problem.

The gist of it is to read an image of a maze, convert the image into a malleable data strucutre, generate the shortest route from start to finish inside the maze, and then visually plot the route on the image.

In cv2, you import images using `imread()`, this gives me a 2D numpy array with RGB values assigned to every pixel. To simplify this, I turned the image into greyscale so that each pixel is assigned a greyscale 8-bit value (0-255) with 255 being white, 0 being black.
```
img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```



Each square should be read 8x8.
Each square should be a class and possess attrs such as bottom wall, left wall, start, and finish.
Each square will then be saved into a 2D list.

The 2D list should be a custom class as well with certain attributes.
The 2D list indexes will start from the top left of the image and generate squares from left to right.
Every square on the first index of every y axis gets a "left border" attr
Every square on the last index of every y axis gets a "right border" attr
Every square on the first x axis gets a "top border" attr
Every square on the last x axis gets a "bottom border" attr

I will ignore every pixel on the last x axis and every pixel on the first y axis. By ignoring these pixels I am turning the 241x129px image into 240x128.This renders every image to be divisible by 8 and so the image can be divided into 8x8 pixel squares for parsing the walls.


