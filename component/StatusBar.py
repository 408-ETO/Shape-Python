from tkinter import Frame,Label


class StatusBar(Frame):
    def __init__(self, app):
        super(StatusBar, self).__init__(app)
        self.label = Label(self)
        self.label.pack()

    def set(self, status):
        self.label.config(text=status)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
