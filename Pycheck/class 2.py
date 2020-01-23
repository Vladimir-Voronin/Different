from os.path import dirname

class Counter():
    def __init__(self, first_number = 0):
        self.number = first_number

    def doing(self):
        self.number += 1

    def get(self):
        return self.number

        
class RRR():
    def ret(self):
        return self


class AntiCounter(Counter):
    def doing(self):
        self.number -= 1


class Path():
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "Parh({})".format(self.current)

    @property
    def parent(self):
        return Path(dirname(self.current))



class Point():
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Point(x = {}, y = {}, z = {})'.format(self.x, self.y, self.z)

    def __str__(self):
        return 'x = {}, y = {}, z = {}'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return Point((self.x + other.x)/2,
                     (self.y + other.y)/2,
                     (self.z + other.z)/2)




class Line():
    def __init__(self, first_point, second_point):
        self.x1 = first_point.x
        self.x2 = second_point.x
        self.y1 = first_point.y
        self.y2 = second_point.y
        self.z1 = first_point.z
        self.z2 = second_point.z

    def __repr__(self):
        return 'Line(1 point = ({}, {}, {}), 2 point = ({}, {}, {})'.format(self.x1,
                                                                            self.y1,
                                                                            self.z1,
                                                                            self.x2,
                                                                            self.y2,
                                                                            self.z2)




























