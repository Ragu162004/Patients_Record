import tkinter as tk
from tkinter import *
from tkinter import messagebox
from patient_add import DatabaseManage

class EditStudent(tk.Frame):
    
    def __init__(self, parent, id):
        global db
        global std_id
        std_id = id
        db = DatabaseManage()
        totalData = db.fetchData(id)
        global rootWindow
        rootWindow = parent
        global e1, e2, e3, e4
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        self.parent.title("Edit Patient Record")
        self.parent.geometry("400x300")
        self.parent.configure(bg="#f0f0f0")

        l = Label(parent, bg="#3E4149", fg="white", text="Edit Patient Record", font=("Helvetica", 17, "bold"))
        l.grid(row=0, column=0, columnspan=2, padx=15, pady=15, sticky="ew")

        lbl2 = Label(parent, text="Patient Name:", bg="#f0f0f0", font=("Helvetica", 12))
        lbl2.grid(row=1, column=0, sticky=E, pady=5, padx=10)
        lbl3 = Label(parent, text="Patient ID:", bg="#f0f0f0", font=("Helvetica", 12))
        lbl3.grid(row=2, column=0, sticky=E, pady=5, padx=10)
        lbl4 = Label(parent, text="Room No:", bg="#f0f0f0", font=("Helvetica", 12))
        lbl4.grid(row=3, column=0, sticky=E, pady=5, padx=10)
        lbl5 = Label(parent, text="Fees:", bg="#f0f0f0", font=("Helvetica", 12))
        lbl5.grid(row=4, column=0, sticky=E, pady=5, padx=10)

        e1 = Entry(parent, font=("Helvetica", 12))
        e2 = Entry(parent, font=("Helvetica", 12))
        e3 = Entry(parent, font=("Helvetica", 12))
        e4 = Entry(parent, font=("Helvetica", 12))

        e1.grid(row=1, column=1, pady=5, padx=10)
        e2.grid(row=2, column=1, pady=5, padx=10)
        e3.grid(row=3, column=1, pady=5, padx=10)
        e4.grid(row=4, column=1, pady=5, padx=10)

        # Check if data was returned
        if totalData:
            # Inserting the fetched data into the entry fields
            e1.insert(0, totalData[0][0])
            e2.insert(0, totalData[0][1])
            e3.insert(0, totalData[0][2])
            e4.insert(0, totalData[0][3])
        else:
            messagebox.showerror("Error", "No data found for the selected patient.")

        b1 = Button(parent, text="Update", width=10, bg="#4CAF50", fg="white", font=("Helvetica", 12), command=lambda: update_data())
        b1.grid(row=5, column=0, pady=10, padx=10, sticky=E)

        b2 = Button(parent, text="Close", width=10, bg="red", fg="white", font=("Helvetica", 12), command=lambda: deleteWindow())
        b2.grid(row=5, column=1, pady=10, padx=10, sticky=W)

def update_data():
    name = e1.get()
    pid = e2.get()
    room_no = e3.get()
    fees = e4.get()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    db.updateData(std_id, name, pid, room_no, fees)
    rootWindow.destroy()

def deleteWindow():
    rootWindow.destroy()
