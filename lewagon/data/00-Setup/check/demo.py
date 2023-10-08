"""Dummy challenge for Kitt Demo"""
import math


def circle_area(radius):
    """Returns the area of the circle of given radius"""
    # area = math.pi * radius * radius 
    if(radius > 0):
        return math.pi * radius * radius 
    return 0