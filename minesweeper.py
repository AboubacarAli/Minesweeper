import random
from design import *
import tkinter
from tkinter import messagebox

buttons = []
buttonList = []

# Action to execute when we left-click on a mined cell
def left_click_actions(button):
    button.configure(bg = "red")
    messagebox.showinfo("Game over", message="You lost the game")
    gui.destroy()

# Returning the number of surrounding mined cells in case of a non-mined-cell
def count_neighbors(button):
    neighbors = 0
    row, col = button.grid_info()["row"], button.grid_info()["column"]
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            try:
                if buttons[r*8 + c] in buttonList:
                    neighbors += 1
            except IndexError:
                    pass
    button.configure(text = str(neighbors))

# Generating the board
for r in range(8):
    for c in range(8):
        button = tkinter.Button(Center, width = 17, height = 3, bg="gray")
        button.grid(row = r, column = c)
        buttons.append(button)

# Defining the mines in the board
minned_cells = random.sample(buttons, 15)

# Assigning the method left_click_actions to the layout manager of the mouse left button
for button in minned_cells:
    buttonList.append(button)
    button.bind("<Button-1>", lambda event, button = button: left_click_actions(button))

# Assigning the method count_neighbors to the layout manager of the mouse left button. Its task is to return the number of mined cells surronding the non-mined-cell we clicked on
for button in buttons:
    if button not in buttonList:
        button.bind("<Button-1>", lambda event, button = button: count_neighbors(button))



# Running the window
gui.mainloop()