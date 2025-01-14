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
version_string = "Peter Driscoll -- 1/12/2025 V 1.0"

#Styles of application (Like a .css file)
style = ttk.Style()
style.theme_use("default")
#TODO
title_font = tkfont.Font(family="Helvetica", size=32, weight="bold")
font1 = tkfont.Font(family="Helvetica", size=20, weight="bold")
style.configure("Exit.TButton", foreground = "white", background="red", borderwidth=2, font=("Helvetica", 16, "bold"), relief="raised") 
style.configure("Info.TButton", foreground = "black", background="gray", borderwidth=2, font=("Helvetica", 16, "bold"), relief="raised") 

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
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=20)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

#Level 2 subframes
#A
subA2a = ttk.Frame(subA1, padding = 0, borderwidth=1, relief="solid")
subA2b = ttk.Frame(subA1, padding = 0, borderwidth=1, relief="solid")
subA2c = ttk.Frame(subA1, padding = 0, borderwidth=1, relief="solid")
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


#B
subB2a = ttk.Frame(subB1, padding = 0, borderwidth=1, relief="solid") #left side 
subB2b = ttk.Frame(subB1, padding = 0, borderwidth=1, relief="solid")
subB2a.grid(row=0, column=0, sticky="nsew")
subB2b.grid(row=0, column=1, sticky="nsew")
subB1.grid_rowconfigure(0, weight=1)
subB1.grid_columnconfigure(0, weight=8)
subB1.grid_columnconfigure(1, weight=1)
#B2a
#3 frames
subB2a1 =ttk.Frame(subB2a, padding = 0, borderwidth=1, relief="solid")
subB2a2 =ttk.Frame(subB2a, padding = 0, borderwidth=1, relief="solid")
subB2a3 =ttk.Frame(subB2a, padding = 0, borderwidth=1, relief="solid")
subB2a1.grid(row=0, column=0, sticky="nsew")
subB2a2.grid(row=1, column=0, sticky="nsew")
subB2a3.grid(row=2, column=0, sticky="nsew")
subB2a.grid_rowconfigure(0, weight=1)
subB2a.grid_rowconfigure(1, weight=20)
subB2a.grid_rowconfigure(2, weight=1)
subB2a.grid_columnconfigure(0, weight=1)

#sub rows placed into B2a1
subB2a1a =ttk.Frame(subB2a1, padding = 0, borderwidth=1, relief="solid")
subB2a1b =ttk.Frame(subB2a1, padding = 0, borderwidth=1, relief="solid")
subB2a1c =ttk.Frame(subB2a1, padding = 0, borderwidth=1, relief="solid")
subB2a1a.grid(row=0, column=0, sticky="nsew")
subB2a1b.grid(row=0, column=1, sticky="nsew")
subB2a1c.grid(row=0, column=2, sticky="nsew")
subB2a1.grid_rowconfigure(0, weight=1)
subB2a1.grid_columnconfigure(0, weight=4)
subB2a1.grid_columnconfigure(1, weight=1)
subB2a1.grid_columnconfigure(2, weight=1)
#sub rows for 
#labels in sub B2 for PLC data entry and naming
device_name_label = ttk.Label(subB2a1a, text="Device Name", font=font1)
device_name_label.grid(column=0, row=0)
device_name_entry = ttk.Entry(subB2a1a, justify="center")
device_name_entry.grid(column=1, row=0)
ip_address_label = ttk.Label(subB2a1a, text="Device IP", font=font1)
ip_address_label.grid(column=0, row=1)
ip_address_entry = ttk.Entry(subB2a1a)
ip_address_entry.grid(column=1, row=1)

#buttons in B2a1
test_connection_button = ttk.Button(subB2a1b, text="Test Connection")
test_connection_button.grid(column=0, row=0, sticky="nsew")
subB2a1b.grid_rowconfigure(0, weight=1)
subB2a1b.grid_columnconfigure(0, weight=1)
device_status = ttk.Button(subB2a1c, text="Device Status")
device_status.grid(column=0, row=0, sticky="nsew")
subB2a1c.grid_rowconfigure(0, weight=1)
subB2a1c.grid_columnconfigure(0, weight=1)

#B2b
#3 frames
subB2b1 =ttk.Frame(subB2b, padding = 0, borderwidth=1, relief="solid")
subB2b2 =ttk.Frame(subB2b, padding = 0, borderwidth=1, relief="solid")
subB2b3 =ttk.Frame(subB2b, padding = 0, borderwidth=1, relief="solid")
subB2b1.grid(row=0, column=0, sticky="nsew")
subB2b2.grid(row=1, column=0, sticky="nsew")
subB2b3.grid(row=2, column=0, sticky="nsew")
subB2b.grid_rowconfigure(0, weight=1)
subB2b.grid_rowconfigure(1, weight=1)
subB2b.grid_rowconfigure(2, weight=1)
subB2b.grid_columnconfigure(0, weight=1)

#buttons in B2b
tag_colection_button = ttk.Button(subB2b, text="Data Collection Rules")
tag_colection_button.grid(column=0, row=0)

export_rules_button = ttk.Button(subB2b, text="Data Export Rules")
export_rules_button.grid(column=0, row=1)

start_stop_button = ttk.Button(subB2b, text="Start")  #TODO fix 
start_stop_button.grid(column=0, row=2, sticky="nsew")

#C
subC2a = ttk.Frame(subC1, padding = 0, borderwidth=1, relief="solid")
subC2a.grid(row=0, column=0, sticky="nsew")
subC2a.grid_rowconfigure(0, weight=1)
subC2a.grid_columnconfigure(0, weight=1)
ttk.Label(subC2a, text = version_string, anchor="se").grid(column=0, row=0, sticky='se')




root.mainloop()