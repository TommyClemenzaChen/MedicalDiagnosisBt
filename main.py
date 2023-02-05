import medchatbot
from tkinter import *

from PIL import ImageTk, Image

 
# create root window
root = Tk()

# root window title and dimension
root.title("SymCheck")
# Set geometry (widthxheight)
root.geometry('1500x1000')
root.configure(background='white')

# all widgets will be here
# Execute Tkinter

lbl1 = Label(root, text="Enter your symptoms", bg="black", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()
lbl3 = Label(root, text = "Put a comma between each symptom", fg="black", bg="white", font = "Satoshi 12")
lbl3.pack()

txt = Entry(root, width=30)
txt.pack()
 
 
# function to display user text when
# button is clicked



def clicked():
    
    #lbl2 = Label(root, text = "", font = "Inter 16", fg = 'black', bg = 'white')
    #lbl2.pack()

    
    res = txt.get()
   
    
    
   # temp = ""
   
    for x in medchatbot.suggest_diagnosis_and_treatments(res):
        
       
        
        lbl2 = Label(root, text = x, font = "Inter 16", fg = 'black', bg = 'white')
        lbl2.pack()
        
    
    
 
# button widget with red color text inside
btn = Button(root, text = "Enter" , fg = "white", command= clicked, bg = 'black')
# Set Button Grid
btn.pack()

symtomList = "Symptoms List:\n "
i = 0
for symptom in medchatbot.symptoms_diagnosis.keys():

    symtomList += symptom + ", "
    if(i % 4 == 0 and i != 0):
        symtomList+= '\n'
    i+=1

symList = Label(root, text = symtomList, fg="black", bg="white", font = "Satoshi 12")
symList.pack()

#Load an image in the script
img= (Image.open("panda.jpg"))

#Resize the Image using resize method
resized_image= img.resize((300,300), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

label = Label(root, image = new_image)
label.pack(side="bottom")


root.mainloop()