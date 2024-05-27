import sqlite3
from OOP_FINAL_CLASS import contents
import subprocess
import ast

con = sqlite3.connect("C:\\Users\\Romer\\Desktop\\OneDrive_2024-05-27\\FINAL PROJECT\\Final_Project")

d = contents()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
t1 = input()
t2 = ast.literal_eval(t1)

def compute():
    print("")
def Prelim():
    total_score_quiz = (float(prelim_quiz1.get()) + float(prelim_quiz2.get()) + float(prelim_quiz3.get()))
    total_score_activity = (float(prelim_act1.get()) + float(prelim_act2.get()) + float(prelim_act3.get()))

    activity_prelim = (((float(prelim_act1.get()) + float(prelim_act2.get()) + float(prelim_act3.get()))/60) * 100) * .25
    quiz_prelim = (((float(prelim_quiz1.get()) + float(prelim_quiz2.get()) + float(prelim_quiz3.get()))/150) * 100) * .30
    attendance_prelim = ((float(prelim_attendance_total.get()) / 100) * 100) * .05
    exam_prelim = ((float(prelim_exam.get()) / 100) * 100) * .40
    grade_prelim = activity_prelim + quiz_prelim + attendance_prelim + exam_prelim

    prelim_total_activity.insert(0, total_score_activity)
    prelim_total_Quiz.insert(0, total_score_quiz)
    prelim_grade.insert(0, '%.2f'% grade_prelim)

def Midterm():
    total_score_quiz = (float(midterm_quiz1.get()) + float(midterm_quiz2.get()) + float(midterm_quiz3.get()))
    total_score_activity = (float(midterm_act1.get()) + float(midterm_act2.get()) + float(midterm_act3.get()))

    activity_midterm = (((float(midterm_act1.get()) + float(midterm_act2.get()) + float(
        midterm_act3.get())) / 60) * 100) * .25
    quiz_midterm = (((float(midterm_quiz1.get()) + float(midterm_quiz2.get()) + float(
        midterm_quiz3.get())) / 150) * 100) * .30
    attendance_midterm = ((float(midterm_attendance_total.get()) / 100) * 100) * .05
    exam_midterm = ((float(midterm_exam.get()) / 100) * 100) * .40
    grade_midterm = activity_midterm + quiz_midterm + attendance_midterm + exam_midterm

    midterm_total_activity.insert(0, total_score_activity)
    midterm_total_Quiz.insert(0, total_score_quiz)
    midterm_grade.insert(0, '%.2f'% grade_midterm)

def Final():
    total_score_quiz = (float(final_quiz1.get()) + float(final_quiz2.get()) + float(final_quiz3.get()))
    total_score_activity = (float(final_act1.get()) + float(final_act2.get()) + float(final_act3.get()))

    activity_final = (((float(final_act1.get()) + float(final_act2.get()) + float(
        final_act3.get())) / 60) * 100) * .20
    quiz_final = (((float(final_quiz1.get()) + float(final_quiz2.get()) + float(
        final_quiz3.get())) / 150) * 100) * .25
    attendance_final = ((float(final_attendance_total.get()) / 100) * 100) * .05
    exam_final = ((float(final_exam.get()) / 100) * 100) * .50
    grade_final = activity_final + quiz_final + attendance_final + exam_final

    final_total_activity.insert(0, total_score_activity)
    final_total_Quiz.insert(0, total_score_quiz)
    final_grade.insert(0, '%.2f'% grade_final)

def Save():
    student_number = student_numbertxt.get()
    attendance_prelim = prelim_attendance_total.get()
    attendance_midterm = midterm_attendance_total.get()
    attendance_final = final_attendance_total.get()
    activity_prelim = prelim_total_activity.get()
    activity_midterm = midterm_total_activity.get()
    activity_final = final_total_activity.get()
    quiz_prelim = prelim_total_Quiz.get()
    quiz_midterm = midterm_total_Quiz.get()
    quiz_final = final_total_Quiz.get()
    exam_prelim = prelim_exam.get()
    exam_midterm = midterm_exam.get()
    exam_final = final_exam.get()
    prelim_gradetotal = prelim_grade.get()
    midterm_gradetotal = midterm_grade.get()
    final_gradetotal = final_grade.get()

    # INSERT
    query1 = """INSERT INTO student_grades (student_number, attendance_prelim, activity_prelim, quiz_prelim, exam_prelim, attendance_midterm, 
    activity_midterm, quiz_midterm, exam_midterm, attendance_final, activity_final, quiz_final, exam_final, prelim_grade, midterm_grade, final_grade) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

    query1inp = (student_number, attendance_prelim, activity_prelim, quiz_prelim, exam_prelim, attendance_midterm, activity_midterm,
                 quiz_midterm, exam_midterm, attendance_final, activity_final, quiz_final, exam_final, prelim_gradetotal, midterm_gradetotal, final_gradetotal)

    con.execute(query1, query1inp)

    con.commit()
    con.close()

    prelim_attendance_total.delete(0, 'end')
    midterm_attendance_total.delete(0, 'end')
    final_attendance_total.delete(0, 'end')
    prelim_total_activity.delete(0, 'end')
    midterm_total_activity.delete(0, 'end')
    final_total_activity.delete(0, 'end')
    prelim_total_Quiz.delete(0, 'end')
    midterm_total_Quiz.delete(0, 'end')
    final_total_Quiz.delete(0, 'end')
    prelim_exam.delete(0, 'end')
    midterm_exam.delete(0, 'end')
    final_exam.delete(0, 'end')
    prelim_grade.delete(0, 'end')
    midterm_grade.delete(0, 'end')
    final_grade.delete(0, 'end')
    prelim_act1.delete(0, 'end')
    prelim_act2.delete(0, 'end')
    prelim_act3.delete(0, 'end')
    prelim_quiz1.delete(0, 'end')
    prelim_quiz2.delete(0, 'end')
    prelim_quiz3.delete(0, 'end')
    midterm_act1.delete(0, 'end')
    midterm_act2.delete(0, 'end')
    midterm_act3.delete(0, 'end')
    midterm_quiz1.delete(0, 'end')
    midterm_quiz2.delete(0, 'end')
    midterm_quiz3.delete(0, 'end')
    final_act1.delete(0, 'end')
    final_act2.delete(0, 'end')
    final_act3.delete(0, 'end')
    final_quiz1.delete(0, 'end')
    final_quiz2.delete(0, 'end')
    final_quiz3.delete(0, 'end')

def Home():
    d.window.destroy()
    subprocess.run(["python", "OOP_FINAL_MAIN_MENU.py"], input= t1, text=True, shell = True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

main_frame = d.create_canvas(0, 0)
frame0 = d.create_frames(main_frame, 0, 0, 1920, 1100, '#D8D8D8')
frame1 = d.create_frames(main_frame, 100, 90, 250, 600, 'gray')
frame2 = d.create_frames(main_frame, 550, 90, 250, 600, 'gray')
frame3 = d.create_frames(main_frame, 1000, 90, 250, 600, 'gray')

pic = d.create_label_pic(frame0,  0,0, 0, 0)

students_grades_computation = d.create_label(frame0, 'GRADES COMPUTATION', 'black', 'gray', 'Sitka Text', 20, 'bold', 540, 6)
prelim_gradelbl = d.create_label(frame0, 'Prelim', 'black', '#c3c3c3', 'Sitka Text', 15, 'bold', 100, 50)
midterm_gradelbl = d.create_label(frame0, 'Midterm', 'black', '#d2d2d2', 'Sitka Text', 15, 'bold', 550, 50)
final_gradelbl = d.create_label(frame0, 'Finals', 'black', '#e8e8e8', 'Sitka Text', 15, 'bold', 1000, 50)
view_grade = d.create_button(frame0, 1, 'Home', 'sky blue', 'black', 'hand2', 1, 'Sitka Text', 10,
                              1193, 735, 125, 30, Home)
save = d.create_button(frame0, 1, 'Save', 'sky blue', 'black', 'hand2', 1, 'Sitka Text', 10,
                              1050, 735, 125, 30, Save)
# first column ==============================================================================================================================
#activity label
activity = d.create_label(frame1, 'ACTIVITY', 'black', 'grey', 'Sitka Text', 20, 'bold', 55, 10)
activity1 = d.create_label(frame1, 'Activity 1: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 70)
activity2 = d.create_label(frame1, 'Activity 2: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 100)
activity3 = d.create_label(frame1, 'Activity 3: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 130)
total_activity = d.create_label(frame1, 'Total Score :', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 160)

# activity entries
prelim_act1 = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 75, 80, 20)
prelim_act2 = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 105, 80, 20)
prelim_act3 = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 135, 80, 20)
prelim_total_activity = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 165, 80, 20)
# quizes label
Quiz = d.create_label(frame1, 'QUIZZES', 'black', 'grey', 'Sitka Text', 20, 'bold', 55, 200)
Quiz1 = d.create_label(frame1, 'Quiz 1: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 250)
Quiz2 = d.create_label(frame1, 'Quiz 2: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 280)
Quiz3 = d.create_label(frame1, 'Quiz 3: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 310)
total_quiz = d.create_label(frame1, 'Total Score :', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 340)

# Quiz entries
prelim_quiz1 = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 255, 80, 20)
prelim_quiz2 = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 285, 80, 20)
prelim_quiz3 = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 315, 80, 20)
prelim_total_Quiz = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 345, 80, 20)

# exam
prelim = d.create_label(frame1, 'Prelim exam: ', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 390)
prelim_exam = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 395, 80, 20)

# attendance
attendance = d.create_label(frame1, 'Attendance: ', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 430)
prelim_attendance_total = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 435, 80, 20)

#button
compute = d.create_button(frame1, 1, 'Compute Prelim', 'sky blue', 'black', 'hand2', 1, 'Sitka Text', 10,
                          20, 550, 125, 30, Prelim)

grade = d.create_label(frame1, 'Prelim Grade:', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 470)
prelim_grade = d.create_entry(frame1, 'black', 'white', 1, 'Sitka Text', 12, 155, 475, 80, 20)

# second column ==============================================================================================================================

#activity label
activity = d.create_label(frame2, 'ACTIVITY', 'black', 'grey', 'Sitka Text', 20, 'bold', 55, 10)
activity1 = d.create_label(frame2, 'Activity 1: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 70)
activity2 = d.create_label(frame2, 'Activity 2: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 100)
activity3 = d.create_label(frame2, 'Activity 3: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 130)
total_activity = d.create_label(frame2, 'Total Score :', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 160)

# activity entries
midterm_act1 = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 75, 80, 20)
midterm_act2 = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 105, 80, 20)
midterm_act3 = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 135, 80, 20)
midterm_total_activity = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 165, 80, 20)
# quizes label
Quiz = d.create_label(frame2, 'QUIZZES', 'black', 'grey', 'Sitka Text', 20, 'bold', 55, 200)
Quiz1 = d.create_label(frame2, 'Quiz 1: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 250)
Quiz2 = d.create_label(frame2, 'Quiz 2: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 280)
Quiz3 = d.create_label(frame2, 'Quiz 3: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 310)
total_quiz = d.create_label(frame2, 'Total Score :', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 340)

# Quiz entries
midterm_quiz1 = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 255, 80, 20)
midterm_quiz2 = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 285, 80, 20)
midterm_quiz3 = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 315, 80, 20)
midterm_total_Quiz = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 345, 80, 20)

# exam
prelim = d.create_label(frame2, 'Midterm exam: ', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 390)
midterm_exam = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155,395, 80, 20)

# attendance
attendance = d.create_label(frame2, 'Attendance: ', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 430)
midterm_attendance_total = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 435, 80, 20)

#button
compute = d.create_button(frame2, 1, 'Compute Midterm', 'sky blue', 'black', 'hand2', 1, 'Sitka Text', 10,
                          20, 550, 125, 30, Midterm)

grade = d.create_label(frame2, 'Midterm Grade:', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 470)
midterm_grade = d.create_entry(frame2, 'black', 'white', 1, 'Sitka Text', 12, 155, 475, 80, 20)

# third column ==============================================================================================================================

#activity label
activity = d.create_label(frame3, 'ACTIVITY', 'black', 'grey', 'Sitka Text', 20, 'bold', 55, 10)
activity1 = d.create_label(frame3, 'Activity 1: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 70)
activity2 = d.create_label(frame3, 'Activity 2: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 100)
activity3 = d.create_label(frame3, 'Activity 3: /20', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 130)
total_activity = d.create_label(frame3, 'Total Score :', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 160)

# activity entries
final_act1 = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 75, 80, 20)
final_act2 = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 105, 80, 20)
final_act3 = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 135, 80, 20)
final_total_activity = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 165, 80, 20)
# quizes label
Quiz = d.create_label(frame3, 'QUIZZES', 'black', 'grey', 'Sitka Text', 20, 'bold', 55, 200)
Quiz1 = d.create_label(frame3, 'Quiz 1: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 250)
Quiz2 = d.create_label(frame3, 'Quiz 2: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 280)
Quiz3 = d.create_label(frame3, 'Quiz 3: /50', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 310)
total_quiz = d.create_label(frame3, 'Total Score :', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 340)

# Quiz entries
final_quiz1 = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 255, 80, 20)
final_quiz2 = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 285, 80, 20)
final_quiz3 = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 315, 80, 20)
final_total_Quiz = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 345, 80, 20)

# exam
prelim = d.create_label(frame3, 'Final exam: ', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 390)
final_exam = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 395, 80, 20)

# attendance
attendance = d.create_label(frame3, 'Attendance:  ', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 430)
final_attendance_total = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 435, 80, 20)

#button
compute = d.create_button(frame3, 1, 'Compute Finals', 'sky blue', 'black', 'hand2', 1, 'Sitka Text', 10,
                          20, 550, 125, 30, Final)

grade = d.create_label(frame3, 'Final Grade:', 'black', 'grey', 'Sitka Text', 12, 'bold', 20, 470)
final_grade = d.create_entry(frame3, 'black', 'white', 1, 'Sitka Text', 12, 155, 475, 80, 20)

student_numberlbl = d.create_label(frame0, 'Student Number:', 'black', 'grey', 'Sitka Text', 12, 'bold', 650, 735)
student_numbertxt = d.create_entry(frame0, 'black', 'white', 1, 'Sitka Text', 12, 800, 735, 200, 30)

student_numbertxt.insert(0, t2[0])
student_numbertxt.config(state='readonly')

d.window.mainloop()
