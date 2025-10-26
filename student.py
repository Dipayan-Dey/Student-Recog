from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


# Making class
class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System-- Student Pannel")

        # Heading 
        title_lbl=Label(self.root,text="STUDENT MANAGEMENT WINDOW",font=("times new roman",35,"bold"),bg="#9216F0", fg="#FBFBFF")
        title_lbl.place(x=0,y=0,width=1552,height=45)
        # Variables
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_reg=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_admit=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        


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

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CST","ETCE","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Class Student Information
        class_student_info=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Informations",font=("times new roman",14,"bold"))
        class_student_info.place(x=3,y=252,width=720,height=300)

        # StudentID/reg. no
        studentID_label=Label(class_student_info,text="Reg. namber:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_info,textvariable=self.var_reg,width=20,font=("times new roman",12))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student name
        studentName_label=Label(class_student_info,text="Full Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_info,textvariable=self.var_name,width=30,font=("times new roman",12))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Student Roll
        studentRoll_label=Label(class_student_info,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        studentRoll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentRoll_entry=ttk.Entry(class_student_info,textvariable=self.var_roll,width=20,font=("times new roman",12))
        studentRoll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Student Admit number
        studentAdmit_label=Label(class_student_info,text="Admit no:",font=("times new roman",12,"bold"),bg="white")
        studentAdmit_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentAdmit_entry=ttk.Entry(class_student_info,textvariable=self.var_admit,width=20,font=("times new roman",12))
        studentAdmit_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Student gender
        studentGen_label=Label(class_student_info,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        studentGen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studentGen_combo=ttk.Combobox(class_student_info,textvariable=self.var_gender,font=("times new roman",12),state="readonly",width=15)
        studentGen_combo["values"]=("Select Gender","Female","Male","Other")
        studentGen_combo.current(0)
        studentGen_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # Student DOB
        studentDob_label=Label(class_student_info,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        studentDob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentDob_entry=ttk.Entry(class_student_info,textvariable=self.var_dob,width=20,font=("times new roman",12))
        studentDob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Student Email
        studentMail_label=Label(class_student_info,text="email:",font=("times new roman",12,"bold"),bg="white")
        studentMail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentMail_entry=ttk.Entry(class_student_info,textvariable=self.var_email,width=20,font=("times new roman",12))
        studentMail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Student Phone no.
        studentPhone_label=Label(class_student_info,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        studentPhone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentPhone_entry=ttk.Entry(class_student_info,textvariable=self.var_phone,width=20,font=("times new roman",12))
        studentPhone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Student Address
        studentAddress_label=Label(class_student_info,text="Address:",font=("times new roman",12,"bold"),bg="white")
        studentAddress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentAddress_entry=ttk.Entry(class_student_info,textvariable=self.var_address,width=20,font=("times new roman",12))
        studentAddress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        TeaName_label=Label(class_student_info,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        TeaName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        TeaName_entry=ttk.Entry(class_student_info,textvariable=self.var_teacher,width=30,font=("times new roman",12))
        TeaName_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio Buttons
        self.var_radio1=StringVar()
        radioButton1=ttk.Radiobutton(class_student_info,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radioButton1.grid(row=6,column=0)

        radioButton2=ttk.Radiobutton(class_student_info,text="No Photo Sample",variable=self.var_radio1,value="No")
        radioButton2.grid(row=6,column=1)

        #Buttons frame
        btn_frame=Frame(class_student_info,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=205, width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=0,pady=1,sticky=W)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1,padx=15,pady=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="orange",fg="white")
        delete_btn.grid(row=0,column=2,padx=15,pady=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3,padx=15,pady=1)

        # on the next row
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=20,font=("times new roman",12,"bold"),bg="#891ac4",fg="white")
        take_photo_btn.grid(row=1,column=0,padx=3)

        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=20,font=("times new roman",12,"bold"),bg="#29bccc",fg="white")
        update_photo_btn.grid(row=1,column=1)
        

        # Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        Right_frame.place(x=750,y=10,width=730,height=580)

        img_right=Image.open(r"D:\Student Face Recog system\Images\Right Window.jpg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=720,height=130)

        # Simple search system
        # Search Frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",14,"bold"))
        search_frame.place(x=5,y=132,width=710,height=70)

        # Search by
        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12),state="readonly",width=15)
        search_combo["values"]=("Select","Regestration","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # Search entry value box
        search_entry=ttk.Entry(search_frame,width=25,font=("times new roman",12))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        # Search and Show all button
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="#891ac4",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="#ee149a",fg="white")
        showAll_btn.grid(row=0,column=4)

        # Table frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=205,width=710,height=350)

        #Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","year","sem","reg","name","roll","admit","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Increase scroll place
        self.student_table.configure(xscrollcommand=500, yscrollcommand=100)

        # Heading Showing
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("reg",text="Regstration No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll no.")
        self.student_table.heading("admit",text="Admit No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("reg",width=120)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("admit",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # Function Decleration
    def add_data(self):
        print("DEBUG - Registration Number:", self.var_reg.get())

        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_reg.get()=="":
            messagebox.showerror("Error","All feilds are required !",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                host="localhost",
                username="root",   # your MySQL username
                password="Ayan@123",   # your MySQL password
                database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
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
                self.var_radio1.get() if self.var_radio1.get() else "No"))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}", parent=self.root)


    # Data Fatch
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root", password="Ayan@123",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM students")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Get cursou
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

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

    # Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_reg.get()=="":
            messagebox.showerror("Error","All feilds are required !",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update student details?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Ayan@123",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update students SET dep=%s, year=%s,sem=%s,name=%s,roll=%s,admit=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s WHERE reg=%s",(
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
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated Sucessfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
                
    # Delete Function
    def delete_data(self):
        if self.var_reg.get()=="":
            messagebox.showinfo("Error","Student Regestration Number must be required!!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Data","Do you want to delete student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Ayan@123",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="DELETE FROM students WHERE reg=%s"
                    val=(self.var_reg.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

    # Reset button working
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

    # Generate Data Set & Photo sample
    def generate_dataset(self):
        print("DEBUG - Registration Number:", self.var_reg.get())

        student_id = self.var_reg.get().strip()
        if student_id == "":
            messagebox.showerror("Error","Valid reg no is required !",parent=self.root)
            return

        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Ayan@123",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM students")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update students SET dep=%s, year=%s,sem=%s,name=%s,roll=%s,admit=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s WHERE reg=%s",(
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
                self.reset_data()
                conn.close()


                # Load predifined data on face frontals form opencv

                face_classifire=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifire.detectMultiScale(gray,1.3,5)

                    # Scalling factor=1.3
                    #Minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                # Open camera
                cap=cv2.VideoCapture(0)
                img_id=0
                print("DEBUG - Registration Number:", self.var_reg.get())
                student_id=self.var_reg.get().strip()
                if student_id == "":
                    messagebox.showerror("Error", "Valid Registration Number is required!", parent=self.root)
                    return
                
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"

                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50, 50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or img_id==100:
                        break

                cap.release()
                self.reset_data()    # reset only at the very end
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!")
                self.reset_data()    # reset only at the very end


            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)



    # Run 
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()