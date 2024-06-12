import tkinter as tk
from window import MainWindow

def main():

    root = tk.Tk()
    
    root.title("Student Database")
    root.resizable(False,False)

    fm = MainWindow(root)

    fm.grid()
    
    root.mainloop()

if __name__ == "__main__":
	main()
