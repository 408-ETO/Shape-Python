class Task:
    def __init__(self, app):
        self.app = app

    @classmethod
    def command(cls, app):
        def func(*args):
            app.task = cls(app)
        return func

    def onMousePress(self, e):
        pass

    def onMouseMove(self, e):
        pass

    def onMouseRelease(self, e):
        pass
