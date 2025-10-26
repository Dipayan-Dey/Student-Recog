from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from tkcalendar import DateEntry

# Making class
class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System-- Student Pannel")

        # Heading 
        title_lbl=Label(text="STUDENT MANAGEMENT WINDOW",font=("times new roman",35,"bold"),bg="#000080", fg="#FBFBFF")
        title_lbl.place(x=0,y=0,width=1552,height=45)


        # Setting top 3 images 
        # 1st Image 
        img=Image.open(r"D:\Student Face Recog system\Images\top image student 1.webp")
        img=img.resize((510, 130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=48, width=510, height=130)

        # 2nd Image
        img2=Image.open(r"D:\Student Face Recog system\Images\Top student image 2.webp")
        img2=img2.resize((510, 130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=48, width=510, height=130)

        # 3rd Image
        img3=Image.open(r"D:\Student Face Recog system\Images\Top student 3.webp")
        img3=img3.resize((530, 130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=48, width=530, height=130)

        # Studnt Window background
        img4 = Image.open(r"D:\Student Face Recog system\Images\Student window bg.jpg")
        img4=img4.resize((1552, 650),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img4=Label(self.root, image=self.photoimg4)
        bg_img4.place(x=0,y=175, width=1552, height=650)

        # Secondary white background
        main_frame=Frame(bg_img4,bd=2)
        main_frame.place(x=5,y=5,width=1523,height=600)

        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"D:\Student Face Recog system\Images\Student left frame.webp")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=720,height=130)

        
        # Current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=3,y=135,width=720,height=117)

        # Department
        dep_label=Label(current_course_frame,text="Depertment",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CST","ETCE","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","First Year","Secound Year","Third Year")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Class Student Information
        class_student_info=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Informations",font=("times new roman",14,"bold"))
        class_student_info.place(x=3,y=252,width=720,height=300)

        # StudentID/reg. no
        studentID_label=Label(class_student_info,text="Reg. namber",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_info,width=20,font=("times new roman",12))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student name
        studentName_label=Label(class_student_info,text="Full Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_info,width=30,font=("times new roman",12))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Student Roll
        studentRoll_label=Label(class_student_info,text="Roll",font=("times new roman",12,"bold"),bg="white")
        studentRoll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentRoll_entry=ttk.Entry(class_student_info,width=20,font=("times new roman",12))
        studentRoll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Student Admit number
        studentAdmit_label=Label(class_student_info,text="Admit no.",font=("times new roman",12,"bold"),bg="white")
        studentAdmit_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentAdmit_entry=ttk.Entry(class_student_info,width=20,font=("times new roman",12))
        studentAdmit_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Student gender
        studentGen_label=Label(class_student_info,text="Gender",font=("times new roman",12,"bold"),bg="white")
        studentGen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studentGen_combo=ttk.Combobox(class_student_info,font=("times new roman",12),state="readonly",width=20)
        studentGen_combo["values"]=("<---Select Gender--->","Female","Male","Other")
        studentGen_combo.current(0)
        studentGen_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # Student DOB
        studentDob_label=Label(class_student_info,text="Admit no.",font=("times new roman",12,"bold"),bg="white")
        studentDob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        

        # Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=730,height=580)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()