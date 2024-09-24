# day 3
from tkinter import *
windos=Tk()
windos.title("Day  3")
windos.geometry("500x500")
text=Label(windos,text='day 3',font=("Aribal Bold",20))# you can add any font
text.grid(row=0,column=0,padx=10,pady=10)# you can add x,y valus set text  position and row and colum position


def new_windos(windos): # create a new Windos
    new_windos=windos.destroy() # old windos  destroy

    new_windos=Tk()# another awyas to create new windos
    new_windos.title("New Windos")  
    new_windos.geometry("500x500")
    text=Label(new_windos,text='wellcome to new windo',font=("Aribal Bold",20)).grid(row=1,column=1) # adding text  to new windos

bototme=Button(windos,text='gen newWindos',command=lambda:new_windos(windos)).grid(row=1,column=1)


windos.mainloop()
