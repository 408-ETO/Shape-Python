from .ProtoType import Task


class Colorize(Task):
    def __init__(self, app, colorize_target):
        super().__init__(app)
        self.colorize_target = colorize_target

    def onMousePress(self, e):
        item = self.app.canvas.find_overlapping(
            e.x-1, e.y-1, e.x+1, e.y+1)
        if item:
            item = item[-1]
            kargs = {}
            kargs[self.colorize_target] = self.app.color
            self.app.canvas.itemconfig(item,**kargs)


class OutlineColorize(Colorize):
    name = '边框颜色'
    accelerator = 'Control-l'

    def __init__(self, app):
        super().__init__(app,'outline')


class FillColorize(Colorize):
    name = '填充颜色'
    accelerator = 'Control-f'

    def __init__(self, app):
        super().__init__(app,'fill')
