from tkinter import *
from PIL import Image,ImageTk,ImageSequence 
import time
from pygame import mixer
mixer.init()



root =Tk()
root.geometry("1380x800")


def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("c:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\Jarvis.png",)
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("c:\\xampp\\htdocs\\PythonProject\\DeskTopAi\\jarvis_intro.mp3 ")
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img = img.resize((1380,800))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(5.0)
    root.destroy()
    
play_gif()
root.mainloop()