import OOP_FINAL_CLASS
import sqlite3
import tkinter as tk
from tkinter import messagebox
import subprocess

con = sqlite3.connect("C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\Final_Project")
cursor = con.cursor()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def LogIn():
    #COMMAND TO LOGIN AND TRANSFER TO ANOTHER WINDOW
    stud_number = stud_numbertxt.get()
    password = password_entrytxt.get()
    print(stud_number)
    print(password)
    cursor.execute(f"SELECT * FROM account_login WHERE student_number = '{stud_number}' AND student_password = '{password}' ")
    student = cursor.fetchone()
    if student:
        c.window.destroy()
        subprocess.run(["python", "OOP_FINAL_MAIN_MENU.py"], input= str(student), text=True, shell=True)
    else:
        popup = tk.Toplevel()
        popup.title("ERROR")
        popup.geometry("240x120")
        label = tk.Label(popup, text="INCORRECT USERNAME OR PASSWORD!")
        label.pack(pady=20)

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)


def Open_register():
    # COMMAND TO GO TO A REGISTRATION WINDOW
    c.window.destroy()
    subprocess.run(["python", "OOP_FINAL_REGISTRATION.py"], shell = True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------



c = OOP_FINAL_CLASS.contents()

#FRAMES
main_frame = c.create_canvas(0,0)

frame0 = c.create_frames(main_frame, 0, 0, 1920, 1100, '#D8D8D8')
frame1 = c.create_frames(main_frame,  563,  213, 350, 350, 'gray')

#BACKGROUND
c.create_label_pic(frame0, 0, 0, 0, 0)

#LABEL
c.create_label(frame1, "WELCOME", 'white', 'gray', 'Sitka Text', 25, 'bold',90, 30)

stud_numberlbl = c.create_label(frame1, 'Student Number', 'white', 'gray', 'Sitka Text', 12, 'bold', 103, 90)
passwordlbl = c.create_label(frame1, 'Password', 'white', 'gray', 'Sitka Text', 12, 'bold', 130, 165)

#ENTRY
stud_numbertxt = c.create_entry(frame1,'black', 'white',1, 'Sitka Text', 11, 50, 120, 250, 40)
password_entrytxt = c.create_entry_hidden(frame1,'black', 'white',1, 'Sitka Text', 11, 50, 190, 250, 40, '*')

#BUTTONS
login_button = c.create_button(frame1, 12, 'Login', 'sky blue', 'black', 'hand2', 1, 'Sitka Text', 8, 65, 250, 100, 40, LogIn)
register_button = c.create_button(frame1, 12, 'Register', '#D8D8D8', 'black', 'hand2', 1, 'Sitka Text', 8, 185, 250, 100, 40, Open_register)


c.window.mainloop()
