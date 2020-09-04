from .ProtoType import Task
from math import sin, cos, pi, sqrt
from numpy import linspace


class Line(Task):
    name = '绘制直线'
    accelerator = 'Control-L'

    def __init__(self, app):
        super().__init__(app)

    def onMousePress(self, e):
        self.coords_0 = (e.x, e.y)
        self.item = self.app.canvas.create_line(e.x, e.y, e.x, e.y)

    def onMouseMove(self, e):
        self.app.canvas.coords(self.item, (*self.coords_0, e.x, e.y))

    def onMouseRelease(self, e):
        x0, y0 = self.coords_0


class Shape(Task):
    name = '封闭图形'

    def __init__(self, app):
        super().__init__(app)
        self.fill = 'white'
        self.outline = 'black'


class P2Shape(Shape):
    name = '两点确定封闭图形'

    def __init__(self, app):
        super().__init__(app)

    def calculate_coords(self, target):
        cx, cy = self.center
        dx, dy = target.x - cx, target.y - cy
        return cx, cy, dx, dy

    def onMousePress(self, e):
        self.center = (e.x, e.y)
        self.item = self.app.canvas.create_polygon(
            e.x, e.y, fill=self.fill, outline=self.outline)

    def onMouseMove(self, e):
        coords = self.calculate_coords(e)
        self.app.canvas.coords(self.item, coords)

    def onMouseRelease(self, e):
        cx, cy = self.center


class Rectangle(P2Shape):
    name = '绘制矩形'
    accelerator = 'Control-R'

    def __init__(self, app):
        super().__init__(app)

    def calculate_coords(self, target):
        cx, cy, dx, dy = super().calculate_coords(target)
        return cx-dx, cy-dy, cx+dx, cy-dy, cx+dx, cy+dy, cx-dx, cy+dy


class Square(P2Shape):
    name = '绘制正方形'
    accelerator = 'Control-Q'

    def __init__(self, app):
        super().__init__(app)

    def calculate_coords(self, target):
        cx, cy, dx, dy = super().calculate_coords(target)
        return cx-dx, cy-dy, cx+dy, cy-dx, cx+dx, cy+dy, cx-dy, cy+dx


class Oval(P2Shape):
    name = '绘制椭圆'
    accelerator = 'Control-O'

    def __init__(self, app):
        super().__init__(app)

    def calculate_coords(self, target):
        cx, cy, dx, dy = super().calculate_coords(target)
        coords = tuple()
        for theta in linspace(0, 2*pi, 36):
            coords += (cx+dx*cos(theta), cy+dy*sin(theta))
        return coords


class Circle(P2Shape):
    name = '绘制圆形'
    accelerator = 'Control-C'

    def __init__(self, app):
        super().__init__(app)

    def calculate_coords(self, target):
        cx, cy, dx, dy = super().calculate_coords(target)
        r = sqrt(dx**2+dy**2)
        coords = tuple()
        for theta in linspace(0, 2*pi, 36):
            coords += (cx+r*cos(theta), cy+r*sin(theta))
        return coords


class Triangle(Shape):
    name = '绘制三角形'
    accelerator = 'Control-T'

    def __init__(self, app):
        super().__init__(app)
        self.coords = tuple()
        self.item = None

    def onMousePress(self, e):
        if not self.item:
            self.coords = [e.x, e.y]
            self.item = self.app.canvas.create_polygon(
                *self.coords, fill=self.fill, outline=self.outline)

    def onMouseRelease(self, e):
        self.coords += (e.x, e.y)
        if len(self.coords) is 6:
            self.coords = tuple()
            self.item = None

    def onMouseMove(self, e):
        if self.item:
            self.app.canvas.coords(self.item, (*self.coords, e.x, e.y))
