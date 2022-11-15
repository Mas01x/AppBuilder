import tkinter as tk
from tkinter import font
from tkinter import ttk as ttk
class app():
    def __init__(self,title):
        """Init the window with a title"""
        win = tk.Tk()
        win.title(title)
        self.win = win
        #Set the font to the defult Tkinter font for the family and size
        self.__activeFont = (font.nametofont("TkDefaultFont").actual('family'),font.nametofont("TkDefaultFont").actual('size'))
    def __IntellisenceFix(self):
        #Make it easer to code
        win = tk.Tk()
        self.win = win

    def returnWindow(self):
        """Return the tkinter window object"""
        return self.win

    def title(self,title):
        """Title the window with the title arg"""
        self.win.title(title)

    def geometry(self,x,y,w,h):
        """Set the windows geometry
        X: The x position on the screen
        Y: The y position on the screen
        W: The width of the window
        H: The height of the window
        """
        self.win.geometry(str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y))

    def position(self,x,y):
        """Set the windows position to x and y"""
        self.geometry(x,y,self.win.winfo_width(),self.win.winfo_height())
    def font(self,fontFamily,size):
        self.__activeFont = (fontFamily,size)
    def text(self,tex,**kargs):
        self.__activeElement = tk.Label(self.win,text=tex,font=self.__activeFont,**kargs)

    def seperator(self,dir="h",**kargs):
        if (dir == "h"):
            dir = "horizontal"
        elif (dir == "v"):
            dir = "vertical"
        else:
            dir = "horizontal"
        self.__activeElement = ttk.Separator(self.win,orient=dir)

    def pack(self,**kargs):
        self.__activeElement.pack(**kargs)

    def launch(self):
        """Launch the window must be called to create window"""
        self.win.mainloop()
