from .ProtoType import Task


class Transform(Task):
    def __init__(self, app):
        super().__init__(app)
        self.item = None
        self.xy = None

    def onMousePress(self, e):
        self.item = self.app.canvas.find_overlapping(
            e.x-1, e.y-1, e.x+1, e.y+1)
        if self.item:
            self.item = self.item[0]
        self.xy = e

    def onMouseRelease(self, e):
        self.item = None


class Translate(Transform):
    name = '平移'
    accelerator = 'Control-d'

    def __init__(self, app):
        super().__init__(app)

    def onMouseMove(self, e):
        if self.item:
            dx, dy = e.x-self.xy.x, e.y-self.xy.y
            self.app.canvas.move(self.item, dx, dy)
            self.xy = e
            cx, cy = self.app.items_center[self.item]
            self.app.items_center[self.item] = (cx+dx, cy+dy)


def complex_transform(x, y, zt):
    z0 = complex(x, y)
    z1 = zt*z0
    return z1.real, z1.imag


class RotateZoom(Transform):
    name = '旋转伸缩'
    accelerator = 'Control-r'

    def __init__(self, app):
        super().__init__(app)

    def onMouseMove(self, e):
        if self.item:
            old_coords = [*self.app.canvas.coords(self.item)]
            new_coords = []
            cx, cy = self.app.items_center[self.item]
            ax, ay = self.xy.x, self.xy.y
            bx, by = e.x, e.y
            za = complex((ax-cx), (ay-cy))
            zb = complex((bx-cx), (by-cy))
            zt = zb/za
            while old_coords:
                x = old_coords.pop(0)
                y = old_coords.pop(0)
                dx, dy = x-cx, y-cy
                dx, dy = complex_transform(dx, dy, zt)
                new_coords.append(cx+dx)
                new_coords.append(cy+dy)
            self.app.canvas.coords(self.item, new_coords)
            self.xy = e
