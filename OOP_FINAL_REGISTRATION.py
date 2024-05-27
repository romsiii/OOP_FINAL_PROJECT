import OOP_FINAL_CLASS
import tkinter as tk
import sqlite3
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import subprocess

con = sqlite3.connect("C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\Final_Project")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------

#SAVE USERNAME AND PASSWORD
def Register():
    #GET
    student_password = passwordtxt.get()
    first_name = firstnametxt.get()
    middle_name = middlenametxt.get()
    last_name = lastnametxt.get()
    suffix = suffixtxt.get()
    year_lvl = yr_leveltxt.get()
    program = programtxt.get()
    date_of_birth = date_of_birthtxt.get()
    address = addresstxt.get()
    city = citytxt.get()
    country = countrytxt.get()
    contact_no = contacttxt.get()
    social_media = socmedacc_idtxt.get()
    picture_path = pictureptxt.get()
    student_number = stud_numbertxt.get()

    if passwordtxt.get() == confirmtxt.get():
        query1 = """INSERT INTO account_login (student_number, student_password, first_name, middle_name, last_name, suffix, year_lvl, program, date_of_birth, Address, 
                        City, Country, Contact_No, Social_media_account, Picture_path) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

        query1inp = (student_number, student_password, first_name, middle_name, last_name, suffix, year_lvl,
                     program, date_of_birth, address, city, country, contact_no, social_media, picture_path)

        con.execute(query1, query1inp)

        con.commit()
        con.close()

        stud_numbertxt.delete(0, 'end')
        passwordtxt.delete(0, 'end')
        firstnametxt.delete(0, 'end')
        middlenametxt.delete(0, 'end')
        lastnametxt.delete(0, 'end')
        suffixtxt.delete(0, 'end')
        yr_leveltxt.delete(0, 'end')
        programtxt.delete(0, 'end')
        date_of_birthtxt.delete(0, 'end')
        addresstxt.delete(0, 'end')
        citytxt.delete(0, 'end')
        countrytxt.delete(0, 'end')
        contacttxt.delete(0, 'end')
        socmedacctxt.delete(0, 'end')
        socmedacc_idtxt.delete(0, 'end')
        pictureptxt.delete(0, 'end')
        confirmtxt.delete(0, 'end')
        stateptxt.delete(0, 'end')
        ziptxt.delete(0, 'end')
        emailtxt.delete(0, 'end')
        c.create_profile_pic(frame1, 150, 150, 50, 70, 'C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\DEFAULT.jpg')
    else:
        popup = tk.Toplevel()
        popup.title("ERROR")
        popup.geometry("240x120")
        label = tk.Label(popup, text="PASSWORD DOES NOT MATCH")
        label.pack(pady=20)

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

#CLEAR
def Clear():
    stud_numbertxt.delete(0, 'end')
    passwordtxt.delete(0, 'end')
    firstnametxt.delete(0, 'end')
    middlenametxt.delete(0, 'end')
    lastnametxt.delete(0, 'end')
    suffixtxt.delete(0, 'end')
    yr_leveltxt.delete(0, 'end')
    programtxt.delete(0, 'end')
    date_of_birthtxt.delete(0, 'end')
    addresstxt.delete(0, 'end')
    citytxt.delete(0, 'end')
    countrytxt.delete(0, 'end')
    contacttxt.delete(0, 'end')
    socmedacc_idtxt.delete(0, 'end')
    pictureptxt.delete(0, 'end')
    confirmtxt.delete(0, 'end')
    stateptxt.delete(0, 'end')
    ziptxt.delete(0, 'end')
    emailtxt.delete(0, 'end')

def Open_LogIn():
    c.window.destroy()
    subprocess.run(["python", "OOP_FINAL_LOGIN.py"], shell = True)

def choose_file():
    filetypes = (('JPG', '.jpg'), ('PNG', '.png'), ('All Files', '.'))
    filepath = tkinter.filedialog.askopenfilename(title="Search Picture Path", initialdir="/", filetypes=filetypes)
    c.create_profile_pic(frame1, 150, 150, 50, 70, filepath)
    pictureptxt.delete(0, 'end')
    pictureptxt.insert(0, filepath)





# -----------------------------------------------------------------------------------------------------------------------------------------------------------


c = OOP_FINAL_CLASS.contents()

#Make main frame
main_frame = c.create_canvas(0,0)

#Make Frames
frame0 = c.create_frames(main_frame, 0, 0, 1920, 1100, '#D8D8D8')
frame1 = c.create_frames(main_frame, 170, 90, 1095, 285, 'gray')
frame2 = c.create_frames(main_frame, 170, 400, 1095, 275, 'gray')
frame3 = c.create_frames(main_frame, 170, 710, 1095, 275, 'gray')


#insert profile pic
profilepic = c.create_profile_pic(frame1, 150, 150, 50, 70, 'C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\DEFAULT.jpg')

#Frame 0 inputs
c.create_label_pic2(frame0, 760, 1200, 0, 0, 1, 1)

#TITLE OF WINDOW
c.create_label(frame1, "REGISTER STUDENT INFORMATION", 'white', 'gray', 'Sitka Text', 25, 'bold',330, 10)


#STUDNET INFO LABELS
c.create_label(frame1, 'Choose File', 'white', 'gray', 'Sitka Text', 8, 'bold', 135, 225)

c.create_label(frame1, 'First Name', 'white', 'gray', 'Sitka Text', 12, 'bold', 230, 70)
c.create_label(frame1, 'Middle Name', 'white', 'gray', 'Sitka Text', 12, 'bold', 430, 70)
c.create_label(frame1, 'Last Name', 'white', 'gray', 'Sitka Text', 12, 'bold', 630, 70)
c.create_label(frame1, 'Suffix', 'white', 'gray', 'Sitka Text', 12, 'bold', 830, 70)

c.create_label(frame1, 'Student Number', 'white', 'gray', 'Sitka Text', 12, 'bold', 230, 140)
c.create_label(frame1, 'Year Level', 'white', 'gray', 'Sitka Text', 12, 'bold', 430, 140)
c.create_label(frame1, 'Program', 'white', 'gray', 'Sitka Text', 12, 'bold', 630, 140)
c.create_label(frame1, 'Date of Birth', 'white', 'gray', 'Sitka Text', 12, 'bold', 830, 140)

c.create_label(frame1, 'Create Password', 'white', 'gray', 'Sitka Text', 12, 'bold', 280, 210)
c.create_label(frame1, 'Confirm Password', 'white', 'gray', 'Sitka Text', 12, 'bold', 680, 210)

#Entry Combobox Date
firstnametxt = c.create_entry(frame1, 'black', 'white',1, 'Sitka Text', 11, 230, 100, 130, 20)
middlenametxt = c.create_entry(frame1, 'black', 'white',1, 'Sitka Text', 11, 430, 100, 130, 20)
lastnametxt = c.create_entry(frame1, 'black', 'white',1, 'Sitka Text', 11, 630, 100, 130, 20)
suffixtxt = c.create_entry(frame1, 'black', 'white',1, 'Sitka Text', 11, 830, 100, 130, 20)

stud_numbertxt = c.create_entry(frame1, 'black', 'white',1, 'Sitka Text', 11, 230, 170, 130, 20)
yr_leveltxt = c.create_entry(frame1, 'black', 'white',1, 'Sitka Text', 11, 430, 170, 130, 20)
programtxt = c.create_entry(frame1, 'black', 'white',1, 'Sitka Text', 11, 630, 170, 130, 20)
date_of_birthtxt = c.create_date_entry(frame1, 19, 'white', 1, 'white', 'Courier New', 8, 0, 'end', 0, 'mm/dd/yyyy', 830, 170, 25)

passwordtxt = c.create_entry_hidden(frame1, 'black', 'white',1, 'Sitka Text', 11, 280, 240, 230, 20, "*")
confirmtxt = c.create_entry_hidden(frame1, 'black', 'white',1, 'Sitka Text', 11, 680, 240, 230, 20, '*')

#ADDRESS LABELS
c.create_label(frame0, "ADDRESS", 'gray', '#cdcdcd', 'Sitka Text', 15, 'bold',170, 370)

c.create_label(frame2, 'Address Line', 'white', 'gray', 'Sitka Text', 12, 'bold', 15, 20)

c.create_label(frame2, 'City', 'white', 'gray', 'Sitka Text', 12, 'bold', 15, 100)
c.create_label(frame2, 'State/Province', 'white', 'gray', 'Sitka Text', 12, 'bold', 563, 100)

c.create_label(frame2, 'Country', 'white', 'gray', 'Sitka Text', 12, 'bold', 15, 180)
c.create_label(frame2, 'ZIP Code', 'white', 'gray', 'Sitka Text', 12, 'bold', 563, 180)

#ADDRESS ENTRY COMBOBOX
addresstxt = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 15, 50, 970, 20)

citytxt = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 15, 130, 485, 20)
stateptxt = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 563, 130, 425, 20)

countrytxt = c.create_combobox(frame2, 'Philippines', 'Pilipinas', 'Pinas', 'Pinoy Country', 'Ph', 'Sitka Text', 11, 0, 'end', 0, '--select one--', 15, 210, 485, 25)
ziptxt = c.create_entry(frame2, 'black', 'white',1, 'Sitka Text', 11, 563, 210, 425, 25)

#CONTACT INFORMATION
c.create_label(frame0, "CONTACT INFORMATION", 'gray', '#cdcdcd', 'Sitka Text', 14, 'bold',170, 680)

c.create_label(frame3, 'Contact No.', 'white', 'gray', 'Sitka Text', 12, 'bold', 15, 20)
c.create_label(frame3, 'Email', 'white', 'gray', 'Sitka Text', 12, 'bold', 563, 20)

c.create_label(frame3, 'Social Media Account', 'white', 'gray', 'Sitka Text', 12, 'bold', 15, 100)
c.create_label(frame3, 'Social Media Account ID/No', 'white', 'gray', 'Sitka Text', 12, 'bold', 563, 100)

c.create_label(frame3, 'Picture Path', 'white', 'gray', 'Sitka Text', 12, 'bold', 15, 180)

#CONTACT INFO ENTRY COMBOBOX

contacttxt = c.create_entry(frame3, 'black', 'white',1, 'Sitka Text', 11, 15, 50, 485, 20)
emailtxt = c.create_entry(frame3, 'black', 'white',1, 'Sitka Text', 11, 563, 50, 425, 20)

socmedacctxt = c.create_combobox(frame3, 'Facebook', 'Instagram', 'Twitter', 'Tiktok', 'Reddit', 'Sitka Text', 11, 0, 'end', 0, '--select one--', 15, 130, 485, 25)
socmedacc_idtxt = c.create_entry(frame3, 'black', 'white',1, 'Sitka Text', 11, 563, 130, 425, 25)

pictureptxt = c.create_entry(frame3, 'black', 'white',1, 'Sitka Text', 11, 15, 210, 970, 20)

#BUTTON
pic_select = c.create_button(frame1, 12, 'Click Here', 'white', 'black', 'hand2', 1, 'Sitka Text', 8, 50, 225, 80, 25, choose_file)
save = c.create_button(frame0, 5, 'Save', 'gray', 'white', 'hand2', 1, 'Sitka Text', 8, 170, 995, 100, 25,Register)
clear = c.create_button(frame0, 5, 'Clear', '#D8D8D8', 'black', 'hand2', 1,'Sitka Text', 8, 280, 995, 100, 25,Clear)
login = c.create_button(frame0, 5, 'Login', 'white', 'black', 'hand2', 1,'Sitka Text', 8, 390, 995, 100, 25,Open_LogIn)

c.window.mainloop()
