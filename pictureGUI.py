import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

# Global variables
global Images, path, index
path = '/home/yucheng/Documents/montage_B_img'
Images = []
index = 0

root = tk.Tk()
root.geometry('480x460')

def initial():
    global Images, path
    for filename in os.listdir(path):
        print(filename)
        if os.path.splitext(filename)[1] == '.png':
            Images.append(filename)
    la1 = tk.Label(root, text='Image QA tool', fg='green', bg='black', font='Verdana 20 bold')
    la1.place(relx=0.05, rely=0.1, relwidth=0.75, relheight=0.7)

def nextOperation():
    global path, Images, index
    bt5.destroy()
    bt4 = tk.Button(root, text='Next', command=showNextIMG)
    bt4.place(relx=0.35, rely=0.85, relwidth=0.2, relheight=0.1)
    target = os.path.join(path, Images[index])
    img = Image.open(target)
    img_show = ImageTk.PhotoImage(img)
    la1 = tk.Label(root, image=img_show)
    la1.place(relx=0.05, rely=0.1, relwidth=0.75, relheight=0.7)
    la1.image = img_show

def showNextIMG():
    global index, path, Images
    index += 1
    if index == len(Images):
        la1 = tk.Label(root, text='Image QA tool', fg='green', font='Verdana 20 bold')
        la1.place(relx=0.05, rely=0.1, relwidth=0.75, relheight=0.7)
        bt5 = tk.Button(root, text='Finish', command=sys.exit)
        bt5.place(relx=0.35, rely=0.85, relwidth=0.2, relheight=0.1)
        return
    target = os.path.join(path, Images[index])
    img = Image.open(target)
    img_show = ImageTk.PhotoImage(img)
    la1 = tk.Label(root, image=img_show)
    la1.place(relx=0.05, rely=0.1, relwidth=0.75, relheight=0.7)
    la1.image = img_show

def saveResult(num):
    global path
    target = os.path.join(path, 'result_yt.txt')
    res = open(target, 'a+')
    res.write(Images[index] + ' ' + str(num) + '\n')
    res.close()
    showNextIMG()

bt5 = tk.Button(root, text='Start', command=nextOperation)
bt5.place(relx=0.35, rely=0.85, relwidth=0.2, relheight=0.1)
bt1 = tk.Button(root, text='0', command=lambda: saveResult(0))
bt1.place(relx=0.85, rely=0.2, relwidth=0.1, relheight=0.1)
bt2 = tk.Button(root, text='1', command=lambda: saveResult(1))
bt2.place(relx=0.85, rely=0.4, relwidth=0.1, relheight=0.1)
bt3 = tk.Button(root, text='2', command=lambda: saveResult(2))
bt3.place(relx=0.85, rely=0.6, relwidth=0.1, relheight=0.1)

initial()

root.mainloop()