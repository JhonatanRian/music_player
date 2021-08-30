from os import SEEK_CUR
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import ttkthemes

class Player:
    
    def __init__(self: object) -> None:
        self.window: ThemedTk = ThemedTk(theme="black")
        self.window.title("Player")
        self.window.resizable(0, 0)
        self.window.geometry("300x400+800+300")
        self.window.config(bg="#333333")
        
        self.img_add: PhotoImage = PhotoImage(file="icons/add.png")
        self.img_next: PhotoImage = PhotoImage(file="icons/next.png")
        self.img_pause: PhotoImage = PhotoImage(file="icons/pause.png")
        self.img_play: PhotoImage = PhotoImage(file="icons/play.png")
        self.img_previus: PhotoImage = PhotoImage(file="icons/previus.png")
        self.img_remove: PhotoImage = PhotoImage(file="icons/remove.png")
        
        self.list: Listbox = Listbox(self.window, bg="#444444", height=14)
        self.list.pack(fill="x", pady=5, padx=5)
        
        self.frame1: Frame = ttk.Frame(self.window)
        self.frame1.pack(pady=10)
        
        self.remove: Button = ttk.Button(self.frame1, image=self.img_remove)
        self.remove.grid(row=0, column=0)
        
        self.add: Button = ttk.Button(self.frame1, image=self.img_add)
        self.add.grid(row=0, column=1)
        
        self.frame2: Frame = ttk.Frame(self.window)
        self.frame2.pack(pady=10)
        
        self.previus: Button = ttk.Button(self.frame2, image=self.img_previus)
        self.previus.grid(row=0, column=0)

        self.play: Button = ttk.Button(self.frame2, image=self.img_play)
        self.play.grid(row=0, column=1)
        
        self.next: Button = ttk.Button(self.frame2,image=self.img_next)
        self.next.grid(row=0, column=2)
        
        self.window.mainloop()
        
Player()