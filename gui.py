from tkinter import *
import  tkinter as tk
import numpy as np
from predict import get_probs, list_all_teams
from PIL import ImageTk, Image

firstclick1 = True
firstclick2 = True

from tkinter import messagebox

OptionList=list_all_teams()

def get_preds():
    "Returns predictions on button's click"
    print("Getting Predictions")
    ht=str(variable.get())
    at=str(variable1.get())
    print("Home Team: ", ht)
    print("Away team: ", at)
    try:
        preds=get_probs(ht,at)[0]
        print("Preds: ", preds)
        res=ht+"'s Win Prediction: "+str(preds[0]*100)+"% \n"
        res1="Draw Prediction: "+str(preds[1]*100)+"% \n"
        res2=at+"'s Win Prediction: "+str(preds[2]*100)+"% \n"
        messagebox.showinfo("Results", res+res1+res2)

    except Exception as e:
        print("EXC: ", e)
        print("Please select valid teams.")
        messagebox.showinfo("Error","Please select valid teams.")

def list_teams():
    "returns list of all teams on button's click"
    teams=list_all_teams()
    res="All teams present are "
    for i, t in enumerate(teams):
        if i==len(teams)-1:
            res+=t
            res+="."
        else:
            res+=t
            res+=","
    res+=" Please choose any 2."
    messagebox.showinfo("All Teams",res)

sel1=""
def get_val1(selection):
    print("Sel1: ", selection)
    sel1=selection

sel2=""
def get_val2(selection):
    print("Sel2: ", selection)
    sel2=selection

def on_entry_click1(event):
    """function that gets called whenever entry1 is clicked"""        
    global firstclick1

    if firstclick1: # if this is the first time they clicked it
        firstclick1 = False
        opt.delete(0, "end") # delete all the text in the entry

def on_entry_click2(event):
    """function that gets called whenever entry1 is clicked"""        
    global firstclick2

    if firstclick2: # if this is the first time they clicked it
        firstclick2 = False
        usrIn1.delete(0, "end") # delete all the text in the entry

# make gui
root = tk.Tk(className=' Football Prediction')

root.geometry("800x400+100+100")

img = ImageTk.PhotoImage(Image.open("pl.png"))   # add PL image

panel = Label(root, image = img)

txtVar = tk.StringVar(None)

#usrIn = tk.Entry(root, width = 40)   # add home team's text box with placeholder
#usrIn.insert(0,"Home Team")
#usrIn.bind('<FocusIn>', on_entry_click1)


#usrIn1 = tk.Entry(root, width = 40)
#usrIn1.insert(0,"Away Team")
#usrIn1.bind('<FocusIn>', on_entry_click2)       # add away team's text box with placeholder

#usrIn.pack()
#usrIn1.pack()

variable = tk.StringVar(root)
variable.set("Home Team")

opt = tk.OptionMenu(root, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()


variable1 = tk.StringVar(root)
variable1.set("Away Team")

opt1 = tk.OptionMenu(root, variable1, *OptionList)
opt1.config(width=90, font=('Helvetica', 12))
opt1.pack()

#if (sel1!="" and sel2!=""):
b1=tk.Button(root, text='Get Predictions', command=get_preds)   # get prediction's button
b1.pack()

b1=tk.Button(root, text='List All Teams', command=list_teams)    # listing all team's button
b1.pack()

panel.pack()

root.mainloop()
