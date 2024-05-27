import OOP_FINAL_CLASS
import subprocess
import tkinter as tk
import tkinter
import sqlite3
import ast

c = OOP_FINAL_CLASS.contents()

con = sqlite3.connect("C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\Final_Project")
cursor = con.cursor()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def Open_Computation():
    # COMMAND TO OPEN GRADE COMPUTATION IF THE STUDENT NUMBER MATCH
    student_number = stud_number.get()
    print(student_number)
    cursor.execute(f"SELECT * FROM account_login WHERE student_number = '{student_number}'")
    student = cursor.fetchone()
    if student:
        c.window.destroy()
        subprocess.run(["python", "OOP_FINAL_GRADE_COMPUTATION.py"], input=t1, text=True, shell=True)
    else:
        popup = tk.Toplevel()
        popup.title("ERROR")
        popup.geometry("180x120")
        label = tk.Label(popup, text="ERROR, NO SUCH STUDENT!")
        label.pack(pady=20)

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

def View_Grade():
    # COMMAND TO SEE THE STUDENT'S GRADE
    c.window.destroy()
    subprocess.run(["python", "OOP_FINAL_VIEW_GRADE.py"], input= t1, text=True, shell = True)
def LogOut():
    # COMMAND TO GO BACK TO LOGIN WINDOW
    c.window.destroy()
    subprocess.run(["python", "OOP_FINAL_LOGIN.py"], shell=True)

def View_Info():
    student_number = stud_number.get()
    print(student_number)
    cursor.execute(f"SELECT * FROM account_login WHERE student_number = {student_number}")
    student = cursor.fetchone()
    if student:
        firstname.insert(0, student[2])
        middlename.insert(0, student[3])
        lastname.insert(0, student[4])
        yr_level.insert(0, student[6])
        program.insert(0, student[7])
        firstname.config(state='readonly')
        middlename.config(state='readonly')
        lastname.config(state='readonly')
        yr_level.config(state='readonly')
        program.config(state='readonly')
        stud_number.config(state='readonly')

        try:
            c.create_profile_pic(frame2, 150, 150, 30, 40, student[14])
        except PermissionError:
            c.create_profile_pic(frame2, 150, 150, 30, 40, 'C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\DEFAULT.jpg')
    else:
        popup = tk.Toplevel()
        popup.title("ERROR")
        popup.geometry("180x120")
        label = tk.Label(popup, text="ERROR, NO SUCH STUDENT!")
        label.pack(pady=20)

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)


    print("Data transfered...")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------

t1 = input()
t2 = ast.literal_eval(t1)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#FRAMES
main_frame = c.create_canvas(0,0)

frame0 = c.create_frames(main_frame, 0, 0, 1920, 1100, '#D8D8D8')
frame1 = c.create_frames(main_frame,  413,  160, 675, 100, 'gray')
frame2 = c.create_frames(main_frame,  413,  270, 675, 250, 'gray')

#BACKGROUND
c.create_label_pic(frame0, 0, 0, 0, 0,)

#TITLE Palitan si "USER NAME" ng First Name sa Database
title = c.create_label(frame1, "WELCOME", 'white', 'gray', 'Sitka Text', 25, 'bold',245, 0)

#FIRST NAME TO TITLE2

title2 = c.create_label(frame1, t2[2], 'white', 'gray', 'Sitka Text', 25,'bold', 250, 50)

#FRAME 2
intro = c.create_label(frame2, 'THIS IS YOUR GRADE COMPUTING SYSTEM', 'white', 'gray', 'Sitka Text', 15, 'bold', 120, 0)

#ProfilePic
profilepic = c.create_profile_pic(frame2, 150, 150, 30, 40, 'C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\DEFAULT.jpg')

#student name IMPORT FROM DATA BASE
c.create_label(frame2, 'First Name', 'white', 'gray', 'Sitka Text', 12, 'bold', 190, 40)
c.create_label(frame2, 'Middle Name', 'white', 'gray', 'Sitka Text', 12, 'bold', 350, 40)
c.create_label(frame2, 'Last Name', 'white', 'gray', 'Sitka Text', 12, 'bold', 510, 40)

c.create_label(frame2, 'Student Number', 'white', 'gray', 'Sitka Text', 12, 'bold', 190, 110)
c.create_label(frame2, 'Year Level', 'white', 'gray', 'Sitka Text', 12, 'bold', 350, 110)
c.create_label(frame2, 'Program', 'white', 'gray', 'Sitka Text', 12, 'bold', 510, 110)

#ENTRIES GAWING READONLY
firstname = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 190, 70, 130, 20)
middlename = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 350, 70, 130, 20)
lastname = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 510, 70, 130, 20)

stud_number = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 190, 140, 130, 20)
yr_level = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 350, 140, 130, 20)
program = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 510, 140, 130, 20)

#BUTTONS
compute = c.create_button(frame2, 5, 'Compute', 'gray', 'white', 'hand2', 1, 'Sitka Text', 8, 170, 200, 100, 25, Open_Computation)
viewgrade = c.create_button(frame2, 5, 'View Grade', '#D8D8D8', 'black', 'hand2', 1,'Sitka Text', 8, 280, 200, 100, 25, View_Grade)
logout = c.create_button(frame2, 5, 'Logout', '#E14040', 'black', 'hand2', 1,'Sitka Text', 8, 390, 200, 100, 25, LogOut)
#info = c.create_button(frame2, 5, 'View Info', 'white', 'black', 'hand2', 1,'Sitka Text', 8, 500, 200, 100, 25, View_Info)

stud_number.insert(0,t2[0])
View_Info()


c.window.mainloop()