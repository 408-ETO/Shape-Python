from tkinter import *
from component import *


class App(Tk):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas(self, width=800, height=600)

        self.statusBar = StatusBar(self)

        self.barMenu = BarMenu(self)
        self.config(menu=self.barMenu)

        self.canvas.pack()
        self.statusBar.pack()

        self.canvas.bind('<ButtonPress-1>', self.onMousePress)
        self.canvas.bind('<B1-Motion>', self.onMouseMove)
        self.canvas.bind('<ButtonRelease-1>', self.onMouseRelease)

        self.task = None
        self.color = 'blue'

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, task):
        self._task = task
        self.statusBar.set(task.name if task else '等待指令')

    def onMousePress(self, e):
        self.task and self.task.onMousePress and self.task.onMousePress(e)

    def onMouseMove(self, e):
        self.task and self.task.onMouseMove and self.task.onMouseMove(e)

    def onMouseRelease(self, e):
        self.task and self.task.onMouseRelease and self.task.onMouseRelease(e)


if __name__ == "__main__":
    App().mainloop()
