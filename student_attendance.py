import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence

class Student_Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System-- Student Attendance")

if __name__=="__main__":
    root = Tk()
    obj = Student_Attendance(root)
    root.mainloop()
