from flask import render_template
from figure import Figure
import re

class Result():
    def __init__(self, form):
        self.dimensions = self.get_dimensions(form['dimensions'])
        self.points = self.get_points(form['corners'])

    # evaluate data and display result
    def display(self):
        figure = Figure(self.points)
        if self.dimensions == ():
            return "Rectangle dimensions are incorrect"
        elif figure.is_rectangle():
            pixel_points = figure.get_pixels(self.dimensions)
            return render_template('result_tensor.html',
                                   resultTitle="Calculation results",
                                   pixelPoints=pixel_points)
        else:
            return "Points do not form a rectangle"

    # extract rectangle points from the request form
    def get_points(self,raw_string):
        raw_tuples = re.findall(r'\([\n\r\s]*[-+]?(?:\d*\.\d+|\d+),[\n\r\s]*[-+]?(?:\d*\.\d+|\d+)[\n\r\s]*\)',
                                str(raw_string))
        points = []
        for string in raw_tuples:
            point_string = re.findall(r'[-+]?(?:\d*\.\d+|\d+)', string)
            point = tuple(float(coord) for coord in point_string)
            points.append(point)
        return points

    # extract pixel grid dimensions from the request form
    def get_dimensions(self,raw_string):
        string_numbers = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',
                                str(raw_string))
        point = ()

        if len(string_numbers) == 2:
            point = tuple(float(dim) for dim in string_numbers)
        return point





