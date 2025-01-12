#main app and GUI will be built out here

from tkinter import *
from tkinter import ttk
import pylogix


#Application Rules
root = Tk()
root.title("Red Tagger")
root.geometry("800x600")

#Styles of application (Like a .css file)
style = ttk.Style()
#TODO


#Main Frame
mainFrame = ttk.Frame(root, padding=10)

#Inernal Frame Geometry
subA = ttk.Frame(mainFrame, borderwidth= 2, relief="solid")



root.mainloop()