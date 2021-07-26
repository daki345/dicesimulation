from tkinter import *
import random
import tkinter

root = Tk()
root.title('Dice Simulator')
label = Label(root,font=('helvitiva',300,'bold'),text='',fg='green')

def rolldice():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text = f'{random.choice(dice)}')
    label.pack() 

#label.pack()

button = Button(root,font=('helvitiva',30,'bold'),text='Dice Roll',command=rolldice,bg='yellow',fg='red')
button.pack()

root.mainloop()