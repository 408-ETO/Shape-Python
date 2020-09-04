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
            self.item = self.item[-1]
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


class RotateZoom(Transform):
    name = '旋转伸缩'
    accelerator = 'Control-r'

    def __init__(self, app):
        super().__init__(app)

    def onMouseMove(self, e):
        if self.item:
            old_coords, new_coords = self.app.canvas.coords(self.item), tuple()
            xs, ys = old_coords[::2], old_coords[1::2]
            n = len(xs)
            xc, yc = sum(xs)/n, sum(ys)/n
            zc = complex(xc, yc)
            za = complex(self.xy.x, self.xy.y)
            zb = complex(e.x, e.y)
            zt = (zb-zc)/(za-zc)
            for x, y in zip(xs, ys):
                z0 = complex(x, y)
                z = zc + zt*(z0-zc)
                new_coords += (z.real, z.imag)
            self.app.canvas.coords(self.item, new_coords)
            self.xy = e
