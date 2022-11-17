import numpy as np

class Figure(object):

    def __init__(self, points):
        self.corners = points

    # get coordinates of a top right corner
    def top_right(self):
        return max(self.corners)

    # get coordinates of a bottom left corner
    def bottom_left(self):
        return min(self.corners)

    # calculate pixel positions
    def get_pixels(self, dimensions):
        top_right = self.top_right()
        bottom_left = self.bottom_left()
        step_x = (top_right[0] - bottom_left[0]) / (dimensions[0]-1)
        step_y = (top_right[1] - bottom_left[1]) / (dimensions[1]-1)

        X = np.arange( bottom_left[0], top_right[0]+step_x, step_x, dtype=float)
        Y = np.arange( top_right[1], bottom_left[1]-step_y, -step_y, dtype=float)
        xx, yy = np.meshgrid(X, Y)

        positions = np.dstack((xx, yy))

        return positions.tolist()

    # check if the input data is rectangle or not
    def is_rectangle(self):

        points = self.corners
        if len(points) == 4:
            # opposite left and right sides should have the same length
            equal_sides1 = (((points[0][0]-points[3][0])**2+(points[0][1]-points[3][1])**2)**2
                        == ((points[1][0]-points[2][0])**2+(points[1][1]-points[2][1])**2)**2)

            # opposite top and bottom sides should have the same length
            equal_sides2 =(((points[3][0]-points[2][0])**2+(points[3][1]-points[2][1])**2)**2
                        == ((points[0][0]-points[1][0])**2+(points[0][1]-points[1][1])**2)**2)

            # diagonals should have the same length
            equal_diagonals = (((points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2) ** 2
                        == ((points[1][0] - points[3][0]) ** 2 + (points[1][1] - points[3][1]) ** 2) ** 2)

            boolean_cond = equal_sides1 and equal_sides2 and equal_diagonals

            return boolean_cond
        else:
            return False


