from tkinter import *

root = Tk()

canvas = Canvas(root, width=700, height=500)
canvas.pack()

task = {
    'name': None
}

menubar = Menu(root)


def drawtask(drawfunc):
    def thetask():
        global task
        task = {
            'name': 'create-bbox',
            'drawfunc': drawfunc,
            'item': None
        }
    return thetask


drawerconfig = [
    {
        'label': '直线',
        'drawtask': canvas.create_line
    },
    {
        'label': '矩形',
        'drawtask': canvas.create_rectangle
    },
    {
        'label': '椭圆',
        'drawtask': canvas.create_oval
    }
]


drawmenu = Menu(menubar, tearoff=False)
for config in drawerconfig:
    drawmenu.add_command(
        label=config['label'], command=drawtask(config['drawtask']))

menubar.add_cascade(label="绘图", menu=drawmenu)


def onMousePress(e):
    if task['name'] == 'create-bbox':
        task['item'] = task['drawfunc'](e.x, e.y, e.x, e.y)


def onMouseMove(e):
    if task['name'] == 'create-bbox':
        init_coords = canvas.coords(task['item'])[:2]
        canvas.coords(task['item'], (*init_coords, e.x, e.y))

def onMouseRelease(e):
    global task
    task = {
        'name':None 
    }


canvas.bind('<ButtonPress-1>', onMousePress)
canvas.bind('<B1-Motion>', onMouseMove)
canvas.bind('<ButtonRelease-1>',onMouseRelease)


root.config(menu=menubar)
root.mainloop()
