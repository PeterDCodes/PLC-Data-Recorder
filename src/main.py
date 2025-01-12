#main app and GUI will be built out here

from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
import pylogix


#Application Rules
root = Tk()
root.title("PLC Data Recorder")
root.geometry("1000x800")
root.minsize(1000, 800) #prevents downsizing of window

#Styles of application (Like a .css file)
style = ttk.Style()
style.theme_use("default")
#TODO
title_font = tkfont.Font(family="Arial", size=24, weight="bold")
style.configure("Exit.TButton", foreground = "white", background="red", borderwidth=0, font=("Helvetica", 16, "bold")) 
style.configure("Info.TButton", foreground = "black", background="gray", borderwidth=0, font=("Helvetica", 16, "bold")) 

#Level 1 subframes added to root window
#Sub Frame Level 1 Geometry
subA1 = ttk.Frame(root, padding = 0, borderwidth= 2, relief="solid")
subB1 = ttk.Frame(root, padding = 0, borderwidth= 2, relief="solid")
subC1 = ttk.Frame(root, padding = 0, borderwidth= 2, relief="solid")
#Sub Frame Level 1 Placement (3 rows)
subA1.grid(row=0, column=0, sticky="nsew")
subB1.grid(row=1, column=0, sticky="nsew")
subC1.grid(row=2, column=0, sticky="nsew")
#configure Sub Frame Grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=9)
root.grid_rowconfigure(2, weight=3)
root.grid_columnconfigure(0, weight=1)


#Level 2 subframes
#A
subA2a = ttk.Frame(subA1, padding = 0, borderwidth=2, relief="solid")
subA2b = ttk.Frame(subA1, padding = 0, borderwidth=2, relief="solid")
subA2c = ttk.Frame(subA1, padding = 0, borderwidth=2, relief="solid")
#Sub Frame Level 1 Placement (3 rows)
subA2a.grid(row=0, column=0, sticky="nsew")
subA2b.grid(row=0, column=1, sticky="nsew")
subA2c.grid(row=0, column=2, sticky="nsew")
#configure Sub Frame Grid
subA1.grid_rowconfigure(0, weight=1)
subA1.grid_columnconfigure(0, weight=4)
subA1.grid_columnconfigure(1, weight=1)
subA1.grid_columnconfigure(2, weight=1)

#title in frame A2a
ttk.Label(subA2a, text = "PLC Data Recorder", font=title_font, anchor="center").grid(column=0,row=0, sticky="nsew")
subA2a.grid_rowconfigure(0, weight=1)
subA2a.grid_columnconfigure(0, weight=1)
#button in frame A2b
ttk.Button(subA2b, text="Info", style="Info.TButton").grid(row=0,column=0, sticky="nsew")
subA2b.grid_rowconfigure(0, weight=1)
subA2b.grid_columnconfigure(0, weight=1)
#button in frame A2c
ttk.Button(subA2c, text="Exit", style="Exit.TButton", command=root.destroy).grid(row=0,column=0, sticky="nsew")
subA2c.grid_rowconfigure(0, weight=1)
subA2c.grid_columnconfigure(0, weight=1)


root.mainloop()