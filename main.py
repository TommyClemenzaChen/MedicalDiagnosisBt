import medchatbot
from tkinter import *



 
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

#needInput = "False"

def clicked():
    #lbl2 = Label(root, text = "", font = "Inter 16", fg = 'black', bg = 'white')
    #lbl2.pack()

    
    res = txt.get()
    #if(needInput == "False"):
        #medchatbot.suggest_treatments(res)
        #return
    
    
   # temp = ""
   
    for x in medchatbot.suggest_diagnosis_and_treatments(res):
        
        #if(x == "INPUT"):
            #needInput = "True"

        #else:
            #needInput = "False"
        
        lbl2 = Label(root, text = x, font = "Inter 16", fg = 'black', bg = 'white')
        lbl2.pack()
        
    
    #lbl2 = Label(root, text = res, bg= "red", font ="none 24 bold", fg = 'purple')
    #lbl2.pack()
 
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

root.mainloop()