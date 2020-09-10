from tkinter import *
from tkinter import colorchooser
from task import *


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

        self.colorzeMenu = Menu(self,tearoff=False)
        for task in colorize_tasks:
            self.colorzeMenu.add_command(label=task.name, command=task.command(app))
            self.app.bind(f'<{task.accelerator}>',task.command(app))
        self.add_cascade(label="涂色", menu=self.colorzeMenu)

        self.add_command(label="选择颜色",command=self.choose_color)

        self.add_command(label="清屏",command=self.clear)
        # self.fileMenu = Menu(self,tearoff=False)
        # self.fileMenu.add_command(label="导入")
        # self.fileMenu.add_command(label="保存")

        # self.add_cascade(label="文件",menu=self.fileMenu)

    def choose_color(self):
        (rgb,hx) = colorchooser.askcolor()
        self.app.color = hx

    def clear(self):
        self.app.canvas.delete(ALL)