import tkinter as tk
from tkinter import *
from tkinter import ttk
from create_window import AddStudent as astd
from edit_window import EditStudent as edtstd
from patient_add import DatabaseManage

class MainWindow(tk.Frame):
    def __init__(self, parent):
        global rootWindow
        global lstt
        global db
        global tree

        db = DatabaseManage()
        lstt = db.viewData()
        rootWindow = parent

        tk.Frame.__init__(self, parent, bg="#f0f0f0")

        self.parent = parent
        self.parent.title("Patients Record")
        self.parent.geometry("1024x768")
        self.parent.state('zoomed')  

        bg_color = "#f0f0f0"
        button_bg_color = "#4CAF50"
        button_fg_color = "white"
        label_bg_color = "#3E4149"
        label_fg_color = "white"

        self.parent.configure(bg=bg_color)

        l = Label(parent, bg=label_bg_color, fg=label_fg_color, text="Patients Record", font=("Helvetica", 24, "bold"))
        l.grid(row=0, column=0, columnspan=4, padx=15, pady=15, sticky="ew")

        b = Button(parent, text="Add New Patient", bg=button_bg_color, fg=button_fg_color, font=("Helvetica", 14), command=lambda: create())
        b.grid(row=1, column=0, sticky=W, padx=15, pady=5)

        b2 = Button(parent, text="Reload", bg=button_bg_color, fg=button_fg_color, font=("Helvetica", 14), command=lambda: refresh())
        b2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        b3 = Button(parent, text="Edit", bg=button_bg_color, fg=button_fg_color, font=("Helvetica", 14), command=lambda: editData())
        b3.grid(row=1, column=2, sticky=W, padx=5, pady=5)

        b4 = Button(parent, text="Delete", bg=button_bg_color, fg=button_fg_color, font=("Helvetica", 14), command=lambda: deleteData())
        b4.grid(row=1, column=3, sticky=E, padx=15, pady=5)

        columns = ("ID", "Name", "Patient_id", "Room_No", "Fees")
        tree = ttk.Treeview(parent, columns=columns, show="headings", height=20)
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Patient_id", text="Patient_id")
        tree.heading("Room_No", text="Room_No")
        tree.heading("Fees", text="Fees")
        tree.grid(row=4, column=0, columnspan=4, sticky='nsew', padx=15, pady=5)

        for col in columns:
            tree.column(col, anchor='center')

        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)
        self.parent.grid_columnconfigure(2, weight=1)
        self.parent.grid_columnconfigure(3, weight=1)
        self.parent.grid_rowconfigure(4, weight=1)

        scrollbar = ttk.Scrollbar(parent, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=4, sticky='ns', pady=5)

        refresh()

def create():
    root = tk.Toplevel(rootWindow)
    root.title("Add Patient")
    root.resizable(False, False)
    root.geometry("400x300")

    def on_close():
        root.destroy()
        refresh()

    root.protocol("WM_DELETE_WINDOW", on_close)
    astd(root).grid()
    root.mainloop()

def refresh():
    global lstt, tree
    lstt = db.viewData()
    for row in tree.get_children():
        tree.delete(row)
    for item in lstt:
        data = item.split(" - ")
        id = data[0]
        name_patient_room_fees = data[1].split(", ")
        name = name_patient_room_fees[0].replace("Name : ", "")
        patient_id = name_patient_room_fees[1].replace("Patient_id : ", "")
        room_no = name_patient_room_fees[2].replace("Room_No : ", "")
        fees = name_patient_room_fees[3].replace("Fees : ", "")
        tree.insert("", "end", values=(id, name, patient_id, room_no, fees))

def deleteData():
    selected_item = tree.selection()[0]
    id = tree.item(selected_item)["values"][0]
    db.delData(id)
    refresh()

def editData():
    selected_item = tree.selection()
    if not selected_item:
        print("At least select an item to edit")
    else:
        id = tree.item(selected_item[0])["values"][0]
        root = tk.Toplevel(rootWindow)
        root.title("Edit Record")
        root.resizable(False, False)
        root.geometry("400x300")

        def on_close():
            root.destroy()
            refresh()

        root.protocol("WM_DELETE_WINDOW", on_close)
        edtstd(root, id).grid()
        root.mainloop()

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    app.grid(sticky="nsew")
    root.mainloop()
