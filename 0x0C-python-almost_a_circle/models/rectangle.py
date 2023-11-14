#!/usr/bin/python3
"""
class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Set the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """ width value"""
            self.integer_validator("width", value)
            self.__height = value

        @property
        def height(self):
            """Get the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Set the height of the rectangle."""
            self.integer_validator("height", value)
            self.__height = value

        @property
        def x(self):
            """Set the x-coordinate of the rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            """ value assignment"""
            self.integer_validator("x", value)
            self.__x = value

        @property
        def y(self):
            """Set the y-coordinate of the rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            """ value assignment"""
            self.integer_validator("y", value)
            self.__y = value

        def validate_integer(self, name, value, eq=True):
            '''Method for validating the value.'''
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if eq and value < 0:
                raise ValueError("{} must be >= 0".format(name))
            elif not eq and value <= 0:
                raise ValueError("{} must be > 0".format(name))
