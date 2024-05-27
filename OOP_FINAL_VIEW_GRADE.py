import OOP_FINAL_CLASS
import tkinter as tk
import sqlite3
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import ast
import subprocess


c = OOP_FINAL_CLASS.contents()
con = sqlite3.connect("C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\Final_Project")
cursor = con.cursor()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
t1 = input()
t2 = ast.literal_eval(t1)

def Get_grades():
    # GET EMPLOYEE DATA
    student_number = student_number_entry.get()
    print(student_number)
    cursor.execute(f"SELECT * FROM student_grades WHERE student_number = {student_number}")
    student = cursor.fetchone()
    if student:
        prelim_entry.insert(0, student[13])
        midterm_entry.insert(0, student[14])
        final_entry.insert(0, student[15])



    else:
        popup = tk.Toplevel()
        popup.title("ERROR")
        popup.geometry("180x120")
        label = tk.Label(popup, text="ERROR, NO GRADES YET")
        label.pack(pady=20)

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)


    print("Data transfered...")

def Convert():
    float(prelim_entry.get())
    float(midterm_entry.get())
    float(final_entry.get())

    if float(prelim_entry.get()) < 70:
        numerical_grade = 5.0
        letter_grade = "F"
        status = "FAILED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 70 and float(prelim_entry.get()) <= 72:
        numerical_grade = 3.0
        letter_grade = "D"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 73 and float(prelim_entry.get()) <= 75:
        numerical_grade = 2.75
        letter_grade = "C-"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 76 and float(prelim_entry.get()) <= 78:
        numerical_grade = 2.50
        letter_grade = "C"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 79 and float(prelim_entry.get()) <= 81:
        numerical_grade = 2.25
        letter_grade = "C+"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 82 and float(prelim_entry.get()) <= 84:
        numerical_grade = 2.0
        letter_grade = "B-"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 85 and float(prelim_entry.get()) <= 88:
        numerical_grade = 1.75
        letter_grade = "B"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 89 and float(prelim_entry.get()) <= 92:
        numerical_grade = 1.50
        letter_grade = "B+"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 93 and float(prelim_entry.get()) <= 96:
        numerical_grade = 1.25
        letter_grade = "A-"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)
    elif float(prelim_entry.get()) >= 97 and float(prelim_entry.get()) <= 100:
        numerical_grade = 1.0
        letter_grade = "A"
        status = "PASSED"
        prelim_numerical_entry.insert(0, numerical_grade)
        prelim_letter_entry.insert(0, letter_grade)
        status1_entry.insert(0, status)

    if float(midterm_entry.get()) < 70:
        numerical_grade = 5.0
        letter_grade = "F"
        status = "FAILED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 70 and float(midterm_entry.get()) <= 72:
        numerical_grade = 3.0
        letter_grade = "D"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 73 and float(midterm_entry.get()) <= 75:
        numerical_grade = 2.75
        letter_grade = "C-"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 76 and float(midterm_entry.get()) <= 78:
        numerical_grade = 2.50
        letter_grade = "C"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 79 and float(midterm_entry.get()) <= 81:
        numerical_grade = 2.25
        letter_grade = "C+"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 82 and float(midterm_entry.get()) <= 84:
        numerical_grade = 2.0
        letter_grade = "B-"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 85 and float(midterm_entry.get()) <= 88:
        numerical_grade = 1.75
        letter_grade = "B"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 89 and float(midterm_entry.get()) <= 92:
        numerical_grade = 1.50
        letter_grade = "B+"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 93 and float(midterm_entry.get()) <= 96:
        numerical_grade = 1.25
        letter_grade = "A-"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)
    elif float(midterm_entry.get()) >= 97 and float(midterm_entry.get()) <= 100:
        numerical_grade = 1.0
        letter_grade = "A"
        status = "PASSED"
        midterm_numerical_entry.insert(0, numerical_grade)
        midterm_letter_entry.insert(0, letter_grade)
        status2_entry.insert(0, status)

    if float(final_entry.get()) < 70:
        numerical_grade = 5.0
        letter_grade = "F"
        status = "FAILED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 70 and float(final_entry.get()) <= 72:
        numerical_grade = 3.0
        letter_grade = "D"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 73 and float(final_entry.get()) <= 75:
        numerical_grade = 2.75
        letter_grade = "C-"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 76 and float(final_entry.get()) <= 78:
        numerical_grade = 2.50
        letter_grade = "C"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 79 and float(final_entry.get()) <= 81:
        numerical_grade = 2.25
        letter_grade = "C+"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 82 and float(final_entry.get()) <= 84:
        numerical_grade = 2.0
        letter_grade = "B-"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 85 and float(final_entry.get()) <= 88:
        numerical_grade = 1.75
        letter_grade = "B"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 89 and float(final_entry.get()) <= 92:
        numerical_grade = 1.50
        letter_grade = "B+"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 93 and float(final_entry.get()) <= 96:
        numerical_grade = 1.25
        letter_grade = "A-"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)
    elif float(final_entry.get()) >= 97 and float(final_entry.get()) <= 100:
        numerical_grade = 1.0
        letter_grade = "A"
        status = "PASSED"
        final_numerical_entry.insert(0, numerical_grade)
        final_letter_entry.insert(0, letter_grade)
        status3_entry.insert(0, status)

    prelim_entry.config(state='readonly')
    midterm_entry.config(state='readonly')
    final_entry.config(state='readonly')

    prelim_numerical_entry.config(state='readonly')
    midterm_numerical_entry.config(state='readonly')
    final_numerical_entry.config(state='readonly')

    prelim_letter_entry.config(state='readonly')
    midterm_letter_entry.config(state='readonly')
    final_letter_entry.config(state='readonly')

    status1_entry.config(state='readonly')
    status2_entry.config(state='readonly')
    status3_entry.config(state='readonly')

def Go_Compute():
    c.window.destroy()
    subprocess.run(["python", "OOP_FINAL_MAIN_MENU.py"], input= t1, text=True, shell = True)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Make main frame
main_frame = c.create_canvas(0,0)

#Make Frames
frame0 = c.create_frames(main_frame, 0, 0, 1920, 1100, '#D8D8D8')
frame1 = c.create_frames(main_frame, 350, 120, 850, 530, 'gray')


#Frame 0 inputs
c.create_label_pic2(frame0, 760, 1200, 0, 0, 1, 1)

#Header
header = c.create_label(frame0, 'View Grades', 'black', 'light gray', 'Sitka Text', 30, 'bold', 650, 10)



#Terms
prelim = c.create_label(frame1, "Prelim Grade:", 'white', 'gray', 'Sitka Text', 20, 'bold', 25,150)
midterm = c.create_label(frame1, "Midterm Grade:", 'white', 'gray', 'Sitka Text', 20, 'bold', 25, 250)
finals = c.create_label(frame1, "Final term Grade:", 'white', 'gray', 'Sitka Text', 20, 'bold', 25, 350)

#Grades
prelim_label = c.create_label(frame1, "Grade", 'white', 'gray', 'Sitka Text', 12, 'bold', 285, 120)

prelim_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 275, 150, 75, 50)
midterm_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 275, 250, 75, 50)
final_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 275, 350, 75, 50)

#Equal signs
equal_sign1 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 355, 150)
equal_sign2 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 355, 250)
equal_sign3 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 355, 350)
equal_sign4 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 470, 150)
equal_sign5 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 470, 250)
equal_sign6 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 470, 350)
equal_sign7 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 585, 150)
equal_sign8 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 585, 250)
equal_sign9 = c.create_label(frame1, "=", 'white', 'gray', 'Sitka Text', 20, 'bold', 585, 350)

#Numberical Grade
prelim_numerical_label = c.create_label(frame1, "Numerical\n Grade", 'white', 'gray', 'Sitka Text', 12, 'bold', 380, 100)

prelim_numerical_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 385, 150, 75, 50)
midterm_numerical_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 385, 250, 75, 50)
final_numerical_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 385, 350, 75, 50)

#Letter Equivalent
prelim_letter_label = c.create_label(frame1, "Letter Grade", 'white', 'gray', 'Sitka Text', 12, 'bold', 485, 120)

prelim_letter_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 500, 150, 75, 50)
midterm_letter_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 500, 250, 75, 50)
final_letter_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 500, 350, 75, 50)

#Status
status_label = c.create_label(frame1, "Status", 'white', 'gray', 'Sitka Text', 12, 'bold', 670, 120)

status1_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 24, 625, 150, 150, 50)
status2_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 24, 625, 250, 150, 50)
status3_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 24, 625, 350, 150, 50)

#Student number
student_number_label = c.create_label(frame1, "Student Number:", 'white', 'gray', 'Sitka Text', 20, 'bold', 200, 40)
student_number_entry = c.create_entry(frame1, 'black', 'light gray', '1', 'Sitka Text', 20, 445, 40, 220, 50)

#buttons
insert_button = c.create_button(frame1, 0.5, "Get grades", 'light blue', 'black', 'arrow', '1', "Sitka text", 12, 180, 470, 150, 50, Get_grades)
convert_button = c.create_button(frame1, 0.5, "Convert grades", 'light blue', 'black', 'arrow', '1', "Sitka text", 12, 345, 470, 150, 50, Convert)
home_button = c.create_button(frame1, 0.5, "Home", 'light blue', 'black', 'arrow', '1', "Sitka text", 12, 510, 470, 150, 50, Go_Compute)

student_number_entry.insert(0, t2[0])
student_number_entry.config(state='readonly')



c.window.mainloop()