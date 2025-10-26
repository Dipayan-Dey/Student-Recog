from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

# Student Management System
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System — Student Panel")

        # === Base directory setup ===
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_dir = os.path.join(self.base_dir, "Images")
        os.makedirs(os.path.join(self.base_dir, "data"), exist_ok=True)

        # === Initialize Database ===
        self.setup_database()

        # === Heading ===
        title_lbl = Label(
            self.root,
            text="STUDENT MANAGEMENT WINDOW",
            font=("times new roman", 35, "bold"),
            bg="#9216F0",
            fg="#FBFBFF"
        )
        title_lbl.place(x=0, y=0, width=1552, height=45)

        # === Variables ===
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
        self.var_radio1 = StringVar()

        # === Helper function for loading images ===
        def load_image(filename, size):
            path = os.path.join(self.image_dir, filename)
            if not os.path.exists(path):
                print(f"⚠️ WARNING: Missing image -> {path}")
                return None
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)

        # === Top 3 Images ===
        self.photoimg = load_image("top image student 1.webp", (510, 130))
        if self.photoimg:
            Label(self.root, image=self.photoimg).place(x=0, y=48, width=510, height=130)

        self.photoimg2 = load_image("Top student image 2.webp", (510, 130))
        if self.photoimg2:
            Label(self.root, image=self.photoimg2).place(x=510, y=48, width=510, height=130)

        self.photoimg3 = load_image("Top student 3.webp", (530, 130))
        if self.photoimg3:
            Label(self.root, image=self.photoimg3).place(x=1020, y=48, width=530, height=130)

        # === Background ===
        self.photoimg4 = load_image("Student window bg.jpg", (1552, 650))
        if self.photoimg4:
            bg_img4 = Label(self.root, image=self.photoimg4)
            bg_img4.place(x=0, y=175, width=1552, height=650)
        else:
            bg_img4 = Frame(self.root, bg="lightgray")
            bg_img4.place(x=0, y=175, width=1552, height=650)

        # === Secondary white background ===
        main_frame = Frame(bg_img4, bd=2)
        main_frame.place(x=5, y=5, width=1523, height=600)

        # === Left Frame ===
        Left_frame = LabelFrame(
            main_frame,
            bd=2, bg="white", relief=RIDGE,
            text="Student Details", font=("times new roman", 14, "bold")
        )
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = load_image("Student left frame.webp", (720, 130))
        if img_left:
            self.img_left_ref = img_left
            Label(Left_frame, image=img_left).place(x=3, y=0, width=720, height=130)

        # === Current Course Information ===
        current_course_frame = LabelFrame(
            Left_frame, bd=2, bg="white", relief=RIDGE,
            text="Current Course Information", font=("times new roman", 14, "bold")
        )
        current_course_frame.place(x=3, y=135, width=720, height=117)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "CST", "ETCE", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=0, column=2, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Semester
        sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=0, padx=10, sticky=W)
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="readonly", width=20)
        sem_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # === Class Student Info ===
        class_student_info = LabelFrame(
            Left_frame, bd=2, bg="white", relief=RIDGE,
            text="Class Student Information", font=("times new roman", 14, "bold")
        )
        class_student_info.place(x=3, y=252, width=720, height=300)

        # --- Form Fields ---
        Label(class_student_info, text="Reg. number:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_reg, width=20, font=("times new roman", 12)).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Full Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_name, width=30, font=("times new roman", 12)).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Roll:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_roll, width=20, font=("times new roman", 12)).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Admit No:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_admit, width=20, font=("times new roman", 12)).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Gender:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        studentGen_combo = ttk.Combobox(class_student_info, textvariable=self.var_gender, font=("times new roman", 12), state="readonly", width=15)
        studentGen_combo["values"] = ("Select Gender", "Female", "Male", "Other")
        studentGen_combo.current(0)
        studentGen_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        Label(class_student_info, text="DOB:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_dob, width=20, font=("times new roman", 12)).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Email:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_email, width=20, font=("times new roman", 12)).grid(row=3, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Phone No:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_phone, width=20, font=("times new roman", 12)).grid(row=3, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Address:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_address, width=20, font=("times new roman", 12)).grid(row=4, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_info, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_info, textvariable=self.var_teacher, width=30, font=("times new roman", 12)).grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # --- Radio buttons ---
        ttk.Radiobutton(class_student_info, text="Take Photo Sample", variable=self.var_radio1, value="Yes").grid(row=6, column=0)
        ttk.Radiobutton(class_student_info, text="No Photo Sample", variable=self.var_radio1, value="No").grid(row=6, column=1)

        # --- Buttons frame ---
        btn_frame = Frame(class_student_info, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=205, width=715, height=70)

        Button(btn_frame, text="Save", command=self.add_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Update", command=self.update_data, width=15, font=("times new roman", 12, "bold"), bg="green", fg="white").grid(row=0, column=1, padx=15)
        Button(btn_frame, text="Delete", command=self.delete_data, width=15, font=("times new roman", 12, "bold"), bg="orange", fg="white").grid(row=0, column=2, padx=15)
        Button(btn_frame, text="Reset", command=self.reset_data, width=14, font=("times new roman", 12, "bold"), bg="red", fg="white").grid(row=0, column=3, padx=15)

        Button(btn_frame, text="Take Photo Sample", width=20, font=("times new roman", 12, "bold"), bg="#891ac4", fg="white", command=self.generate_dataset).grid(row=1, column=0, padx=3)
        Button(btn_frame, text="Update Photo Sample", width=20, font=("times new roman", 12, "bold"), bg="#29bccc", fg="white").grid(row=1, column=1)

        # === Right Frame ===
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 14, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=580)

        # === Table Frame ===
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=710, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            column=("dep", "year", "sem", "reg", "name", "roll", "admit", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table["show"] = "headings"
        for col, text in zip(
            ("dep", "year", "sem", "reg", "name", "roll", "admit", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
            ("Department", "Year", "Semester", "Reg. No.", "Name", "Roll", "Admit", "Gender", "DOB", "Email", "Phone", "Address", "Teacher", "Photo Sample Status")
        ):
            self.student_table.heading(col, text=text)
            self.student_table.column(col, width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # === Database Setup ===
    def setup_database(self):
        """Create database and table if they don't exist"""
        try:
            # Connect to MySQL server (without specifying database)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2006"
            )
            my_cursor = conn.cursor()
            
            # Create database if not exists
            my_cursor.execute("CREATE DATABASE IF NOT EXISTS face_recognizer")
            print("✅ Database 'face_recognizer' created/verified successfully!")
            
            # Close and reconnect to the specific database
            conn.close()
            
            # Connect to the face_recognizer database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2006",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            
            # Create students table if not exists
            my_cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    dep VARCHAR(100),
                    year VARCHAR(50),
                    sem VARCHAR(50),
                    reg VARCHAR(50) UNIQUE,
                    name VARCHAR(200),
                    roll VARCHAR(100),
                    admit VARCHAR(100),
                    gender VARCHAR(20),
                    dob VARCHAR(50),
                    email VARCHAR(200),
                    phone VARCHAR(20),
                    address TEXT,
                    teacher VARCHAR(200),
                    photo VARCHAR(10)
                )
            """)
            conn.commit()
            print("✅ Table 'students' created/verified successfully!")
            conn.close()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}\n\nMake sure MySQL is running and password is correct!")
            print(f"❌ Database Error: {err}")

    # === Database Functions ===
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_reg.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="2006",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    INSERT INTO students (dep, year, sem, reg, name, roll, admit, gender, dob, email, phone, address, teacher, photo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_reg.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_admit.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully!", parent=self.root)
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Registration number already exists!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2006",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT dep, year, sem, reg, name, roll, admit, gender, dob, email, phone, address, teacher, photo FROM students")
            data = my_cursor.fetchall()
            
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_dep.set(data[0])
            self.var_year.set(data[1])
            self.var_sem.set(data[2])
            self.var_reg.set(data[3])
            self.var_name.set(data[4])
            self.var_roll.set(data[5])
            self.var_admit.set(data[6])
            self.var_gender.set(data[7])
            self.var_dob.set(data[8])
            self.var_email.set(data[9])
            self.var_phone.set(data[10])
            self.var_address.set(data[11])
            self.var_teacher.set(data[12])
            self.var_radio1.set(data[13])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_reg.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="2006",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    UPDATE students SET 
                    dep=%s, year=%s, sem=%s, name=%s, roll=%s, admit=%s, gender=%s, 
                    dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo=%s
                    WHERE reg=%s
                """, (
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_admit.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_reg.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student record updated successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error updating: {str(e)}", parent=self.root)

    def delete_data(self):
        if self.var_reg.get() == "":
            messagebox.showerror("Error", "Registration number is required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student record?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="2006",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM students WHERE reg=%s"
                    val = (self.var_reg.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Student record deleted successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting: {str(e)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_reg.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_admit.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_reg.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        # OpenCV face capture
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            if len(faces) == 0:
                return None
            for (x, y, w, h) in faces:
                return img[y:y+h, x:x+w]

        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, frame = cap.read()
            if face_cropped(frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(frame), (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = os.path.join(self.base_dir, "data", f"{self.var_reg.get()}.{img_id}.jpg")
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 13 or img_id == 100:  # Enter key or 100 images
                break
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Generating data set completed!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()