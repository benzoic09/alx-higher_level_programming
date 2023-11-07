#!/usr/bin/python3
"""
class Student that defines a student
"""


class student:
    """ student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
         if attrs is None:
            return self.__dict__
        return {key: value for (key, value) in self.__dict__.items()
                if key in attrs}
