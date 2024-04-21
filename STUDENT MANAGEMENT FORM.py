import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("STUDENT FORM") 

connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

appLabel = tk.Label(root, text="STUDENT DATABE ENTRY FORM", fg="white",bg="green", width=35)
appLabel.config(font=("Times New roman Bold", 15 ))
appLabel.grid(row=0, columnspan=2, padx=(5,5), pady=(30, 0))

class Student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""

    def __init__(self, studentName, collegeName, phoneNumber, address):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address = address

nameLabel = tk.Label(root, text="Enter Your Full Name", fg="RED", width=40, anchor='w',
                     font=("Times New roman Bold", 15)).grid(row=1, column=0, padx=(10,0))
                                               
collegeLabel = tk.Label(root, text="Enter Your University", fg="red", width=40, anchor='w',
                        font=("Times New roman Bold", 15)).grid(row=2, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter Your phone number", fg="blue", width=40, anchor='w',
                      font=("Times New roman Bold", 15)).grid(row=3, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter physical address", fg="blue", width=40, anchor='w',
                        font=("Times New roman Bold", 15)).grid(row=4, column=0, padx=(10,0))

nameEntry = tk.Entry(root, bg="red",font=("Times New roman Bold", 15,), width = 50)

collegeEntry = tk.Entry(root, bg="red",font=("Times New roman Bold", 15,), width = 50)
phoneEntry = tk.Entry(root, bg="blue",font=("Times New roman Bold", 15,), width = 50)
addressEntry = tk.Entry(root,bg="blue",font=("Times New roman Bold", 15,), width = 50)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    # global username, collegeName, phone, address
    global list
    global TABLE_NAME, Student_ID, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data insercted Successfully.")


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("OUTPUT")

    appLabel = tk.Label(secondWindow, text="STUDENT DATABASE SYSTEM",
                        fg="blue", width=40)
    appLabel.config(font=("Times New roman Bold", 15))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Full Name")
    tree.heading("two", text="Student University")
    tree.heading("three", text="Physical Address")
    tree.heading("four", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


# def printDetails():
#     for singleItem in list:
#         print("Student name is: %s\nCollege name is: %s\nPhone number is: %d\nAddress is: %s" %
#               (singleItem.studentName, singleItem.collegeName, singleItem.phoneNumber, singleItem.address))
#         print("****************************************")

button = tk.Button(root, text="ACCEPT  DATA", font=("Times New Roman", 15, "bold"), bg="green", fg="white", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, text="SHOW DATABASE", font=("Times New Roman", 15, "bold"), bg="green", fg="white", command=lambda :destroyRootWindow())
displayButton.grid(row=5, column=1)

root.mainloop()












 

