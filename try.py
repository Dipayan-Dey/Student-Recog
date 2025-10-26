from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System - Student Panel")

        # ===== Variables =====
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_reg = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_admit = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # ===== Title =====
        title_lbl = Label(self.root,
                          text="STUDENT MANAGEMENT WINDOW",
                          font=("times new roman", 20, "bold"),
                          bg="navy", fg="white")
        title_lbl.pack(side=TOP, fill=X)

        # ===== Frame for form =====
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=10, y=50, width=500, height=720)

        class_student_info = LabelFrame(main_frame, bd=2,
                                        text="Class Student Information",
                                        font=("times new roman", 15, "bold"))
        class_student_info.place(x=10, y=10, width=480, height=680)

        # ===== Form fields =====
        Label(class_student_info, text="Department:",
              font=("times new roman", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_dep,
                  width=20, font=("times new roman", 12)).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Year:",
              font=("times new roman", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_year,
                  width=20, font=("times new roman", 12)).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Semester:",
              font=("times new roman", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_sem,
                  width=20, font=("times new roman", 12)).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Reg. No:",
              font=("times new roman", 12)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.studentID_entry = ttk.Entry(class_student_info,
                                         textvariable=self.var_reg,
                                         width=20, font=("times new roman", 12))
        self.studentID_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Name:",
              font=("times new roman", 12)).grid(row=4, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_name,
                  width=20, font=("times new roman", 12)).grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # ... add the rest of your entry fields similarly (roll, gender, etc.)

        # ===== Buttons =====
        btn_frame = Frame(class_student_info, bd=2)
        btn_frame.place(x=0, y=600, width=470, height=50)

        Button(btn_frame, text="Save", command=self.add_data, width=12).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Update", command=self.update_data, width=12).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Delete", command=self.delete_data, width=12).grid(row=0, column=2, padx=5)
        Button(btn_frame, text="Reset", command=self.reset_data, width=12).grid(row=0, column=3, padx=5)
        Button(btn_frame, text="Take Photo Sample", command=self.generate_dataset, width=18).grid(row=0, column=4, padx=5)

        # ===== Table for students =====
        table_frame = Frame(self.root, bd=2)
        table_frame.place(x=520, y=50, width=1000, height=720)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                          columns=("dep","year","sem","reg","name"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("reg", text="Reg. No")
        self.student_table.heading("name", text="Name")
        self.student_table["show"] = "headings"

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # ===== Functions =====
    def add_data(self):
        if self.var_reg.get().strip() == "" or self.var_name.get().strip() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("INSERT INTO students(dep,year,sem,reg,name) VALUES(%s,%s,%s,%s,%s)",
                          (self.var_dep.get(),
                           self.var_year.get(),
                           self.var_sem.get(),
                           self.var_reg.get(),
                           self.var_name.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT dep,year,sem,reg,name FROM students")
        data = my_cursor.fetchall()
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
            self.student_table.insert("", END, values=i)
        conn.close()

    def get_cursor(self, event=""):
        focus = self.student_table.focus()
        content = self.student_table.item(focus)
        data = content['values']
        if data:
            self.var_dep.set(data[0])
            self.var_year.set(data[1])
            self.var_sem.set(data[2])
            self.var_reg.set(data[3])
            self.var_name.set(data[4])

    def reset_data(self):
        self.var_dep.set("")
        self.var_year.set("")
        self.var_sem.set("")
        self.var_reg.set("")
        self.var_name.set("")

    def update_data(self):
        if self.var_reg.get().strip() == "":
            messagebox.showerror("Error", "Reg No required", parent=self.root)
            return
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE students SET dep=%s, year=%s, sem=%s, name=%s WHERE reg=%s",
                          (self.var_dep.get(),
                           self.var_year.get(),
                           self.var_sem.get(),
                           self.var_name.get(),
                           self.var_reg.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Student updated successfully", parent=self.root)

    def delete_data(self):
        if self.var_reg.get().strip() == "":
            messagebox.showerror("Error", "Reg No required", parent=self.root)
            return
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("DELETE FROM students WHERE reg=%s", (self.var_reg.get(),))
        conn.commit()
        self.fetch_data()
        conn.close()
        self.reset_data()
        messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)

    def generate_dataset(self):
        reg_no = self.var_reg.get().strip()
        print("DEBUG - Reg No entered:", reg_no)   # for debugging
        if reg_no == "":
            messagebox.showerror("Error", "Valid Registration Number is required!", parent=self.root)
            return

        # open webcam and capture faces
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                return img[y:y+h, x:x+w]
            return None

        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, frame = cap.read()
            if face_cropped(frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(frame), (450,450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_path = f"data/user.{reg_no}.{img_id}.jpg"
                cv2.imwrite(file_path, face)
                cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 13 or img_id == 50:
                break

        cap.release()
        cv2.destroyAllWindows()

        messagebox.showinfo("Result", "Dataset generated successfully!", parent=self.root)
        self.reset_data()

# ===== Run App =====
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
