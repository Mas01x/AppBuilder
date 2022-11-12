import tkinter as tk

class app():
    def __init__(self,title):
        win = tk.Tk()
        win.title(title)
        self.win = win
    def __IntellisenceFix(self):
        win = tk.Tk()
        self.win = win
    def returnWindow(self):
        return self.win
    def title(self,title):
        self.win.title(title)
    def launch(self):
        self.win.mainloop()
