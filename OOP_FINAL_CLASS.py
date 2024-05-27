import tkinter as tk
import sqlite3
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkcalendar import DateEntry
from PIL import Image, ImageTk



class contents:
    def __init__(self):
        self.canvas = ''
        self.image = ''
        self.pfpic1 = ''
        self.image_tk = ''
        self.scrollbar = ''
        self.container = ''
        self.frame0 = ''
        self.frame1 = ''
        self.container = ''
        self.label = ''
        self.background = ''
        self.pfpic2 = ''
        self.label_pic = ''
        self.label_pic1 = ''
        self.entry = ''
        self.button = ''
        self.combobox = ''
        self.date_entry = ''
        self.window = ''

        self.window = tk.Tk()
        self.window.title("Student Grade Calculator")
        self.window.geometry('1366x768')

# creating layouts
    def create_canvas(self, x, y):
        self.canvas = Canvas(self.window)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.window, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.container = Frame(self.canvas)

        self.frame0 = Frame(self.container, width=1920, height=1080, bg='black')
        self.frame0.pack()

        self.container.update_idletasks()
        self.canvas.create_window(0, 0, window=self.container, anchor='nw')
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        return self.container

    def create_frames(self, container, x, y, width, height, bg):
        self.frame1 = Frame(container, width=width, height=height, bg=bg)
        self.frame1.place(x=x, y=y)
        return self.frame1

    def create_label(self, container, text, fg, bg, font, size, style, x, y):
        self.label = Label(container, text=text, fg=fg, bg=bg, font=(font, size, style))
        self.label.place(x=x, y=y)
        return self.label

    def create_label_pic(self, container, width, height, x, y):
        self.image = Image.open('C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\BACKGROUND.jpg')
        self.image = self.image.resize((1366, 768))
        self.background = ImageTk.PhotoImage(self.image)
        self.label_pic = Label(container, image=self.background, width=width, height=height)
        self.label_pic.place(x=x, y=y)

    def create_label_pic2(self, container, width, height, x, y, relw, relh):
        self.image = Image.open('C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\BACKGROUND2.jpg')
        self.image = self.image.resize((1920, 1280))
        self.background = ImageTk.PhotoImage(self.image)
        self.label_pic = Label(container, image=self.background, width=width, height=height)
        self.label_pic.place(x=x, y=y, relw=relw, relh=relh)

    def create_profile_pic(self, container, width, height, x, y, picturepath):
        self.pfpic1 = Image.open(picturepath)
        self.pfpic1 = self.pfpic1.resize((140, 140))
        self.pfpic2 = ImageTk.PhotoImage(self.pfpic1)
        self.label_pic1 = Label(container, image=self.pfpic2, width=width, height=height)
        self.label_pic1.place(x=x, y=y)

    def create_entry(self, container, fg, bg, border, font, size, x, y, width, height):
        self.entry = Entry(container, fg=fg, bg=bg, border=border, font=(font, size))
        self.entry.place(x=x, y=y, width=width, height=height)
        return self.entry

    def create_entry_hidden(self, container, fg, bg, border, font, size, x, y, width, height,show):
        self.entry = Entry(container, fg=fg, bg=bg, border=border, font=(font, size), show=show)
        self.entry.place(x=x, y=y, width=width, height=height)
        return self.entry

    def create_button(self, container, pady, text, bg, fg, cursor, border, font, size, x, y, width, height, command):
        self.button = Button(container, pady=pady, text=text, bg=bg, fg=fg, cursor=cursor, border=border, font=(font,size), command=command)
        self.button.place(x=x, y=y, width=width, height=height)
        return self.button

    def create_button2(self, container, pady, text, bg, fg, cursor, border, font, size, x, y, width, height):
        self.button = Button(container, pady=pady, text=text, bg=bg, fg=fg, cursor=cursor, border=border, font=(font,size))
        self.button.place(x=x, y=y, width=width, height=height)
        return self.button

    def create_combobox(self, container, values, values2, values3, values4, values5, font, size, first, last, index, string, x,y, width, height):
        self.combobox = ttk.Combobox(container, values=[values, values2, values3, values4, values5], font=(font, size))
        self.combobox.delete(0,'end')
        self.combobox.insert(0, '-SELECT-')
        self.combobox.place(x=x, y=y, width= width, height=height)
        return self.combobox

    def create_date_entry(self, container, width, fg, bg, border, font, size, first, last, index, string, x, y, height):
        self.date_entry = DateEntry(container, width=width, fg=fg, bg=bg, border=border, font=(font, size))
        self.date_entry.delete(0,'end')
        self.date_entry.insert(0, 'mm/dd/yyyy')
        self.date_entry.place(x=x, y=y, height=height)
        return self.date_entry