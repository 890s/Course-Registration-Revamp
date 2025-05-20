import tkinter as tk
from tkinter import ttk
import random
from Teacher import *
from Student import *
from ClassSchedule import *
from Course import *

root = tk.Tk()
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
currentStudent = Student("0", "13", [])
currentTeacher = Teacher("PLACEHOLDER", "", [[], [], [], [], [], [], []])
currentPeriod = 1


def initializeTeachers(filepath, teacherList):
    teachers = open(filepath, "rt").read().split("\n")

    teachers = [i.split(". ") for i in teachers]

    for i in teachers:
        teacherList.append(Teacher(i[0], i[1], [[], [], [], [], [], [], []]))

    return teacherList
def initializeStudents(filepath, studentList, courses, teacherList):
    data = open(filepath, "rt").read().split("\n")
    data = [i.split(",") for i in data]
    for i in data:
        # (course, teacher) format
        currentCourses = [
            (findCourse(j.split(".- ")[1], courses), findTeacher(j.split(".- ")[0], teacherList)) if j != "" else ("",Teacher("PLACEHOLDER","",[[],[],[],[],[],[],[]]))
            for j in i[2:]]
        studentList.append(Student(i[0], i[1], currentCourses))
    return studentList
def initializeCourses(filepath, courses):
    data = open(filepath, "rt").read().split("\n")

    data = [i.split(",") for i in data]

    for i in data:
        a = []
        b = ['9', '10', '11', '12']
        if i[6] != '':
            a = [j.split("=") for j in i[6].split(" ")]
        if i[4] != '':
            b = i[4].split()
        courses.append(Course(i[3], i[2], i[0], i[7], prereqs=a, gradereq=b))
    return courses

def findCourse(internal, courses):
    for i in courses:
        if i.internal == internal:
            return i
    return Course("PLACEHOLDER", "", 0, "Elective")
def findTeacher(name, teacherList):
    for i in teacherList:
        if i.name == name:
            return i
    return Teacher("PLACEHOLDER", "", [[], [], [], [], [], [], []])
def findStudent(id, studentList):
    for i in studentList:
        if i.id == id:
            return i
    return Student("0", "13", [])

def showScreen(page, period=1):
    if page == 1:
        frame2.grid_forget()
        frame3.grid_forget()
        frame4.grid_forget()
        frame5.grid_forget()
        frame1.grid(row=0, column=0)
    elif page == 2:
        frame1.grid_forget()
        frame3.grid_forget()
        frame4.grid_forget()
        frame5.grid_forget()
        frame2.grid(row=0, column=0)
        print(validCourses)
    elif page == 3:
        frame1.grid_forget()
        frame2.grid_forget()
        frame4.grid_forget()
        frame5.grid_forget()
        frame3.grid(row=0, column=0)
    elif page == 4:
        frame1.grid_forget()
        frame2.grid_forget()
        frame3.grid_forget()
        frame5.grid_forget()
        setUpPeriodScreen(period)
        frame4.grid(row=0, column=0)
    elif page==5:
        frame1.grid_forget()
        frame2.grid_forget()
        frame3.grid_forget()
        frame4.grid_forget()
        setUpCounterScreen()
        frame5.grid(row=0, column=0)
def clear_grid(container):
    for widget in container.winfo_children():
        widget.destroy()

def loginButtonAction():
    global currentTeacher
    global currentStudent
    if len(username_entry.get()) > 0 and username_entry.get()[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        currentTeacher = findTeacher(username_entry.get(), teacherList)
        print(currentTeacher.name)
        showScreen(3)
    else:
        currentStudent = findStudent(username_entry.get(), studentList)
        print(currentStudent.id)
        validCourses = getValidCourses(currentStudent, courses)
        print(validCourses)
        setUpRegistrationScreen(courses, validCourses)
        showScreen(2)

def setUpLoginScreen():
    frame1.rowconfigure(0, weight=2)
    frame1.rowconfigure(1, weight=1)
    frame1.rowconfigure(2, weight=1)
    frame1.rowconfigure(3, weight=1)
    frame1.rowconfigure(4, weight=2)
    frame1.columnconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=1)
    frame1.columnconfigure(2, weight=3)
    frame1.columnconfigure(3, weight=1)

    username_label = ttk.Label(frame1, text="Username:")
    username_label.grid(column=1, row=1)

    global username_entry
    username_entry = ttk.Entry(frame1)
    username_entry.grid(column=2, row=1)

    password_label = ttk.Label(frame1, text="Password:")
    password_label.grid(column=1, row=2)

    password_entry = ttk.Entry(frame1, show="*")
    password_entry.grid(column=2, row=2)

    login_button = ttk.Button(frame1, text="Login", command=loginButtonAction)
    login_button.grid(column=2, row=3)
def setUpRegistrationScreen(courses, validCourses):
    clear_grid(frame2)

    frame2.rowconfigure(0, weight=1)
    frame2.rowconfigure(1, weight=1)
    frame2.rowconfigure(2, weight=1)
    frame2.rowconfigure(3, weight=1)
    frame2.rowconfigure(4, weight=1)
    frame2.rowconfigure(5, weight=1)
    frame2.rowconfigure(6, weight=1)
    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=3)

    def setSchedule(student):
        student.setSchedule(
            ClassSchedule((mathEntry.get(), False), (sciEntry.get(), False), (englEntry.get(), False), (ssEntry.get(), False), (elec1Entry.get(), False),(elec2Entry.get(), False)))
        print(student.schedule)

    def getSubjectCourses(subject):
        subjectCourses = []
        for i in validCourses:
            if i.subject == subject:
                subjectCourses.append(i)
        return subjectCourses

    mathLabel = tk.Label(frame2, text='Math')
    mathLabel.grid(row=0, column=0)
    mathEntry = ttk.Combobox(frame2, width=20)
    mathEntry["values"] = getSubjectCourses("Math")
    mathEntry.state(["readonly"])
    mathEntry.grid(column=1, row=0)

    sciLabel = tk.Label(frame2, text='Science')
    sciLabel.grid(row=1, column=0)
    sciEntry = ttk.Combobox(frame2, width=20)
    sciEntry["values"] = getSubjectCourses("Science")
    sciEntry.state(["readonly"])
    sciEntry.grid(column=1, row=1)

    englLabel = tk.Label(frame2, text='ELA')
    englLabel.grid(row=2, column=0)
    englEntry = ttk.Combobox(frame2, width=20)
    englEntry["values"] = getSubjectCourses("ELA")
    englEntry.state(["readonly"])
    englEntry.grid(column=1, row=2)

    ssLabel = tk.Label(frame2, text='Social Studies')
    ssLabel.grid(row=3, column=0)
    ssEntry = ttk.Combobox(frame2, width=20)
    ssEntry["values"] = getSubjectCourses("Social Studies")
    ssEntry.state(["readonly"])
    ssEntry.grid(column=1, row=3)

    elec1Label = tk.Label(frame2, text='Elective')
    elec1Label.grid(row=4, column=0)
    elec1Entry = ttk.Combobox(frame2, width=20)
    elec1Entry["values"] = validCourses
    elec1Entry.state(["readonly"])
    elec1Entry.grid(column=1, row=4)

    elec2Label = tk.Label(frame2, text='Elective')
    elec2Label.grid(row=5, column=0)
    elec2Entry = ttk.Combobox(frame2, width=20)
    elec2Entry["values"] = validCourses
    elec2Entry.state(["readonly"])
    elec2Entry.grid(column=1, row=5)

    backButton = ttk.Button(frame2, text="Return Home", command=lambda: showScreen(1))
    backButton.grid(column=0, row=6)
    submitButton = ttk.Button(frame2, width=20, text="Submit Courses", command=lambda: setSchedule(currentStudent))
    submitButton.grid(column=1, row=6)
def setUpVerificationScreen():
    frame3.rowconfigure(0, weight=1)
    frame3.rowconfigure(1, weight=1)
    frame3.rowconfigure(2, weight=1)
    frame3.rowconfigure(3, weight=1)
    frame3.rowconfigure(4, weight=1)
    frame3.rowconfigure(5, weight=1)
    frame3.rowconfigure(6, weight=1)
    frame3.rowconfigure(7, weight=1)
    frame3.columnconfigure(0, weight=1)

    period1 = tk.Button(frame3, text="1st Period", width=20, command=lambda: showScreen(4, 1))
    period1.grid(row=0, column=0)

    period2 = tk.Button(frame3, text="2nd Period", width=20, command=lambda: showScreen(4, 2))
    period2.grid(row=1, column=0)

    period3 = tk.Button(frame3, text="3rd Period", width=20, command=lambda: showScreen(4, 3))
    period3.grid(row=2, column=0)

    period4 = tk.Button(frame3, text="4th Period", width=20, command=lambda: showScreen(4, 4))
    period4.grid(row=3, column=0)

    period5 = tk.Button(frame3, text="5th Period", width=20, command=lambda: showScreen(4, 5))
    period5.grid(row=4, column=0)

    period6 = tk.Button(frame3, text="6th Period", width=20, command=lambda: showScreen(4, 6))
    period6.grid(row=5, column=0)

    period7 = tk.Button(frame3, text="7th Period", width=20, command=lambda: showScreen(4, 7))
    period7.grid(row=6, column=0)

    returnButton = tk.Button(frame3, text='Return Home', command=lambda: showScreen(1))
    returnButton.grid(row=7, column=0)
def setUpPeriodScreen(period):
    clear_grid(frame4)
    global currentPeriod
    currentPeriod = period
    frame4.rowconfigure(0, weight=1)
    frame4.rowconfigure(1, weight=1)
    frame4.rowconfigure(2, weight=3)
    frame4.rowconfigure(3, weight=1)
    frame4.columnconfigure(0, weight=1)

    def checkSchedule(student):
        global currentStudent
        currentStudent=student
        scheduleOutput.config(text=str(student.getSchedule()))

    selectedStudent = tk.StringVar()
    studentDropdown = ttk.Combobox(frame4, width=20, textvariable=selectedStudent)
    vals = [i.id for i in currentTeacher.periods[period - 1]]
    studentDropdown["values"] = vals
    studentDropdown.state(["readonly"])
    studentDropdown.grid(row=0, column=0)

    checkScheduleButton = tk.Button(frame4, text='Check Schedule', command=lambda: scheduleOutput.config(text=checkSchedule(findStudent(selectedStudent.get(),studentList))))
    checkScheduleButton.grid(row=1, column=0)

    scheduleOutput = tk.Label(frame4, text="Math:\nScience:\nELA:\nSS:\nElective 1:\nElective 2")
    scheduleOutput.grid(row=2, column=0)

    verifyRejectFrame = tk.Frame(frame4)
    verifyRejectFrame.rowconfigure(0, weight=1)
    verifyRejectFrame.columnconfigure(0, weight=1)
    verifyRejectFrame.columnconfigure(1, weight=1)
    verifyButton = tk.Button(verifyRejectFrame, text='Approve', command=lambda: showScreen(3))
    verifyButton.grid(row=0, column=0)
    rejectButton = tk.Button(verifyRejectFrame, text='Reject', command=lambda:showScreen(5))
    rejectButton.grid(row=0, column=1)
    verifyRejectFrame.grid(row=3, column=0)
def setUpCounterScreen():
    clear_grid(frame5)

    frame5.rowconfigure(0, weight=1)
    frame5.rowconfigure(1, weight=1)
    frame5.rowconfigure(2, weight=1)
    frame5.rowconfigure(3, weight=1)
    frame5.rowconfigure(4, weight=1)
    frame5.rowconfigure(5, weight=1)
    frame5.rowconfigure(6, weight=1)
    frame5.columnconfigure(0, weight=1)
    frame5.columnconfigure(1, weight=1)

    global currentStudent
    def getSubjectCourses(subject, student):
        subjectCourses = []
        for i in getValidCourses(student, courses):
            if i.subject == subject:
                subjectCourses.append(i)
        return subjectCourses

    mathCounter = ttk.Combobox(frame5, values=getSubjectCourses("Math", currentStudent))
    mathCounter.state(["readonly"])
    submitMath = tk.Button(frame5, text="Submit", command=lambda: currentStudent.schedule.setSchedule(math=(mathCounter.get(), True)))
    mathCounter.grid(row=0,column=0)
    submitMath.grid(row=0,column=1)

    sciCounter = ttk.Combobox(frame5, values=getSubjectCourses("Science", currentStudent))
    sciCounter.state(["readonly"])
    submitSci = tk.Button(frame5, text="Submit",command=lambda: currentStudent.schedule.setSchedule(sci=(sciCounter.get(), True)))
    sciCounter.grid(row=1, column=0)
    submitSci.grid(row=1, column=1)

    englCounter = ttk.Combobox(frame5, values=getSubjectCourses("ELA", currentStudent))
    englCounter.state(["readonly"])
    submitEngl = tk.Button(frame5, text="Submit",command=lambda: currentStudent.schedule.setSchedule(engl=(englCounter.get(), True)))
    englCounter.grid(row=2, column=0)
    submitEngl.grid(row=2, column=1)

    ssCounter = ttk.Combobox(frame5, values=getSubjectCourses("Social Studies", currentStudent))
    ssCounter.state(["readonly"])
    submitSS = tk.Button(frame5, text="Submit",command=lambda: currentStudent.schedule.setSchedule(ss=(ssCounter.get(), True)))
    ssCounter.grid(row=3, column=0)
    submitSS.grid(row=3, column=1)

    elec1Counter = ttk.Combobox(frame5, values=getSubjectCourses("Elective", currentStudent))
    elec1Counter.state(["readonly"])
    submitElec1 = tk.Button(frame5, text="Submit",command=lambda: currentStudent.schedule.setSchedule(elec1=(elec1Counter.get(), True)))
    elec1Counter.grid(row=4, column=0)
    submitElec1.grid(row=4, column=1)

    elec2Counter = ttk.Combobox(frame5, values=getSubjectCourses("Elective", currentStudent))
    elec2Counter.state(["readonly"])
    submitElec2 = tk.Button(frame5, text="Submit",command=lambda: currentStudent.schedule.setSchedule(elec2=(elec2Counter.get(), True)))
    elec2Counter.grid(row=5, column=0)
    submitElec2.grid(row=5, column=1)
    
    returnButton = tk.Button(frame5, text="Return", command=lambda: showScreen(4, currentPeriod))
    returnButton.grid(row=6, column=0, columnspan=2)

def getValidCourses(student, courses):
    grade = str(int(student.grade) + 1)
    validCourses = []
    for i in courses:
        if grade in i.gradereq and meetsPreReqs(student, i) and i not in [i[0] for i in student.courses]:
            print(i)
            validCourses.append(i)
    return validCourses
def meetsPreReqs(student, course):
    studentCourses = [i[0].id for i in student.courses]
    for i in course.prereqs:
        if len(set(studentCourses) & set(i)) == 0:
            return False
    return True
def sortBySubject(valid, subject):
    output = []
    for course in valid:
        if course.subject == subject:
            output.append(course.name)
    return output

def main():
    global teacherList
    teacherList = []
    global studentList
    studentList = []
    global courses
    courses = []
    global validCourses
    validCourses = []
    teacherList = initializeTeachers("xteachers.txt", teacherList)
    courses = initializeCourses("xcourses.txt", courses)
    studentList = initializeStudents("xstudents.txt", studentList, courses, teacherList)

    for i in studentList:
        for j in range(7):
            i.courses[j][1].periods[j].append(i)

    for i in findTeacher("Michael C", teacherList).periods:
        for j in i:
            print(j, end=" ")
        print("")

    ttk.Style().theme_use('clam')
    root.geometry('500x300')

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # login screen
    setUpLoginScreen()

    # registration screen
    setUpRegistrationScreen(courses, validCourses)

    # verification screen
    setUpVerificationScreen()

    # period screen
    setUpPeriodScreen(1)

    setUpCounterScreen()

    showScreen(1)

    root.mainloop()


main()
