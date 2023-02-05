from tkinter import *
 
# create root window
root = Tk()

# root window title and dimension
root.title("SymCheck")
# Set geometry (widthxheight)
root.geometry('500x500')
root.configure(background='black')

# all widgets will be here
# Execute Tkinter

lbl1 = Label(root, text="Enter your symptoms", bg="orange red", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.grid()

txt = Entry(root, width=20)
txt.grid(column =150, row =250)
 
 
# function to display user text when
# button is clicked
def clicked():
 
    res = "You wrote" + txt.get()
    lbl2 = Label(root, text = res, bg= "black", font ="none 24 bold")
    lbl2.grid()
 
# button widget with red color text inside
btn = Button(root, text = "Enter" , fg = "red", command=clicked, bg = 'black')
# Set Button Grid
btn.grid(column=250, row=250)
root.mainloop()
    