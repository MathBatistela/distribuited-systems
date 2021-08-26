from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as tk_msg
import Pyro4


# creates a Tk() object
master = Tk()
grades_manager = Pyro4.Proxy("PYRONAME:rmi.gradesmanager")

INTEGER_FIELDS = ("student_ra", "year", "semester", "abscenses")
FLOAT_FIELDS = "grade"
ENROLLMENT_FIELDS = (
    "student_ra",
    "subject_code",
    "year",
    "semester",
    "grade",
    "abscenses",
)
PK_ENROLLMENT_FIELDS = ("student_ra", "subject_code", "year", "semester")
ENROLLMENT_QUERY_FIELDS = ("subject_code", "year", "semester")


def get_input(entry):
    gen_entry = entry.copy()
    for key, value in list(gen_entry.items()):
        if value.get():
            if key in INTEGER_FIELDS:
                gen_entry[key] = int(value.get())
            elif key in FLOAT_FIELDS:
                gen_entry[key] = float(value.get())
            else:
                gen_entry[key] = value.get()
        else:
            del gen_entry[key]
    return gen_entry


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ")
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def add_enrollment(entries):
    data = get_input(entries)

    ok, err = grades_manager.create_enrollment(data)

    if err:
        tk_msg.showerror("Error", err)
    else:
        tk_msg.showinfo("Info", "Enrollment created successfully!")


def add_enrollment_window():

    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the Toplevel widget
    newWindow.title("Add Enrollment")

    # gen a form with all the entries
    ents = makeform(newWindow, ENROLLMENT_FIELDS)

    b1 = Button(newWindow, text="Add", command=(lambda e=ents: add_enrollment(e)))
    b1.pack(side=LEFT, padx=5, pady=5)


def update_enrollment(entries):
    data = get_input(entries)

    ok, err = grades_manager.update_enrollment(data)

    if err:
        tk_msg.showerror("Error", err)
    elif ok:
        tk_msg.showinfo("Info", "Enrollment updated successfully!")
    else:
        tk_msg.showerror("Info", "Enrollment does not exists!")


def update_enrollment_window():

    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the Toplevel widget
    newWindow.title("Update Enrollment")

    # gen a form with all the entries
    ents = makeform(newWindow, ENROLLMENT_FIELDS)

    b1 = Button(newWindow, text="Update", command=(lambda e=ents: update_enrollment(e)))
    b1.pack(side=LEFT, padx=5, pady=5)


def get_enrollment(entries):
    data = get_input(entries)

    enrollment, err = grades_manager.get_enrollment(data)

    if err:
        tk_msg.showerror("Error", err)
    elif enrollment:
        tk_msg.showinfo(
            "Info",
            f"Student RA: {enrollment['student_ra']} \n Subject code: {enrollment['subject_code']} \n Year: {enrollment['year']} \n Semester: {enrollment['semester']} \n Grade: {enrollment['grade']} \n Abscenses: {enrollment['abscenses']}",
        )
    else:
        tk_msg.showerror("Info", "Enrollment does not exists!")


def get_enrollment_window():

    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the Toplevel widget
    newWindow.title("Get Enrollment")

    # gen a form with all the entries
    ents = makeform(newWindow, PK_ENROLLMENT_FIELDS)

    b1 = Button(newWindow, text="Delete", command=(lambda e=ents: get_enrollment(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

def delete_enrollment(entries):
    data = get_input(entries)

    ok, err = grades_manager.delete_enrollment(data)

    if err:
        tk_msg.showerror("Error", err)
    elif ok:
        tk_msg.showinfo("Info", "Enrollment deleted successfully!")
    else:
        tk_msg.showerror("Info", "Enrollment does not exists!")


def delete_enrollment_window():

    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the Toplevel widdget
    newWindow.title("Delete Enrollment")

    # gen a form with all the entries
    ents = makeform(newWindow, PK_ENROLLMENT_FIELDS)

    b1 = Button(newWindow, text="Get", command=(lambda e=ents: delete_enrollment(e)))
    b1.pack(side=LEFT, padx=5, pady=5)


def abscenses_and_grades_query(entries):
    data = get_input(entries)

    query_result, err = grades_manager.get_abscenses_and_grades_by_subject(data)

    if err:
        tk_msg.showerror("Error", err)
    elif query_result:
        tk_msg.showinfo("Info", f"Abscenses: {query_result['abscenses']} \n Grades: {query_result['grades']}")
    else:
        tk_msg.showerror("Info", "No records were found!")


def abscenses_and_grades_query_window():

    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the Toplevel widdget
    newWindow.title("Abscenses and grades query")

    # gen a form with all the entries
    ents = makeform(newWindow, ENROLLMENT_QUERY_FIELDS)

    b1 = Button(newWindow, text="Search", command=(lambda e=ents: abscenses_and_grades_query(e)))
    b1.pack(side=LEFT, padx=5, pady=5)


def students_by_subject_query(entries):
    data = get_input(entries)

    query_result, err = grades_manager.get_students_by_subject(data)

    if err:
        tk_msg.showerror("Error", err)
    elif query_result:
        tk_msg.showinfo("Info", query_result)
    else:
        tk_msg.showerror("Info", "No records were found!")


def students_by_subject_query_window():

    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the Toplevel widdget
    newWindow.title("Students by subject query")

    # gen a form with all the entries
    ents = makeform(newWindow, ENROLLMENT_QUERY_FIELDS)

    b1 = Button(newWindow, text="Search", command=(lambda e=ents: students_by_subject_query(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

def gui():
    # sets the geometry of main

    master.title("Grades Manager")
    master.geometry("300x400")

    label = Label(master, text="Grades manager")

    label.pack(pady=10)

    # a button widget which will open add enrollment window
    btn = Button(master, text="Add enrollment", command=add_enrollment_window)
    btn.pack(pady=10)

    # a button widget which will open update enrollment window
    btn1 = Button(master, text="Update enrollment", command=update_enrollment_window)
    btn1.pack(pady=10)

    # a button widget which will open get enrollment window
    btn2 = Button(master, text="Get enrollment", command=get_enrollment_window)
    btn2.pack(pady=10)

    # a button widget which will open delete enrollment window
    btn3 = Button(master, text="Delete enrollment", command=delete_enrollment_window)
    btn3.pack(pady=10)

    # a button widget which will open Abscenses and grades query window
    btn4 = Button(master, text="Abscenses and grades query", command=abscenses_and_grades_query_window)
    btn4.pack(pady=10)

    # a button widget which will open delete enrollment window
    btn5 = Button(master, text="Students by subject query", command=students_by_subject_query_window)
    btn5.pack(pady=10)
    while True:
        master.update_idletasks()
        master.update()


if __name__ == "__main__":
    gui()
