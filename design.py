# Bonus
import tkinter
gui = tkinter.Tk()
from tkinter import messagebox
gui.configure(bg = "black")
gui.geometry("1200x600")
gui.resizable(False, False)
gui.title("Minesweeper")

def about_the_game():
    messagebox.showinfo(title="Minesweeper by ECOLE-IT", message="This version of minesweeper was developed by ECOLE-IT, a company highly recognized and specialized in retro and optimized games. ECOLE-IT is the creator many other games that you may find and try for free on the website https//:ecole-it.com")


def show_rules():
    messagebox.showinfo(title="Game rules", message="The purpose of this game is to open all the cells without openning one single mined cell. You have a counter that gives you details about the number of mines surrounding each non-mined cell you click on. when you open a mined cell, then you lost the game!")

def settings():
    messagebox.showerror(title="Error", message="The settings are temporarily not available")

Top = tkinter.Frame(gui, bg = "brown", width = 1200, height = 150)
Top.place(x = 0, y = 0)
menubar = tkinter.Menu(Top)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="About", command=about_the_game)
filemenu.add_command(label="Rules", command=show_rules)
filemenu.add_command(label="Settings", command=settings)
menubar.add_cascade(label="File", menu=filemenu)
gui.config(menu=menubar)

Left = tkinter.Frame(gui, bg = "red", width = 180, height = 450)
Left.place(x = 0, y = 150)

Center = tkinter.Frame(gui, bg = "gray", width = 1020, height = 450)
Center.place(x = 180, y = 150)