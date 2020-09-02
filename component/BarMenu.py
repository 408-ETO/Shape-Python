from tkinter import *
from task import draw_tasks,trans_tasks


class BarMenu(Menu):
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        self.drawMenu = Menu(self,tearoff=False)
        for task in draw_tasks:
            self.drawMenu.add_command(label=task.name, command=task.command(app))
            self.app.bind(f'<{task.accelerator}>',task.command(app))
        self.add_cascade(label="绘图", menu=self.drawMenu)

        self.tranMenu = Menu(self,tearoff=False)
        for task in trans_tasks:
            self.tranMenu.add_command(label=task.name, command=task.command(app))
            self.app.bind(f'<{task.accelerator}>',task.command(app))
        self.add_cascade(label="变换", menu=self.tranMenu)
