import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
import mysql.connector
import cv2
import os
import pickle

# Making class
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System-- Face Detector")

        # Heading (must be inside __init__)
        title_lbl = Label(self.root, text="FACE RECOGNITION",font=("times new roman", 35, "bold"),bg="#2FEF5C", fg="#4242E4")
        title_lbl.place(x=0, y=0, width=1552, height=45)

        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Left image
        try:
            img_left_path = os.path.join(script_dir, "Images", "Bottam image Data train.jpg")
            img_left = Image.open(img_left_path)
            img_left = img_left.resize((750, 800), Image.Resampling.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_lbl = Label(self.root, image=self.photoimg_left)
            f_lbl.place(x=0, y=47, width=750, height=800)
        except FileNotFoundError:
            print(f"Warning: Left image not found at {img_left_path}")
            f_lbl = Label(self.root, bg="lightgray", text="Image Not Found")
            f_lbl.place(x=0, y=47, width=750, height=800)

        # Right Image 
        try:
            img_right_path = os.path.join(script_dir, "Images", "Right image.jpg")
            img_right = Image.open(img_right_path)
            img_right = img_right.resize((800, 800), Image.Resampling.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)

            f_lbl1 = Label(self.root, image=self.photoimg_right)
            f_lbl1.place(x=752, y=47, width=800, height=800)
        except FileNotFoundError:
            print(f"Warning: Right image not found at {img_right_path}")
            f_lbl1 = Label(self.root, bg="lightgray", text="Image Not Found")
            f_lbl1.place(x=752, y=47, width=800, height=800)

        # Button 
        self.face_recog_btn = Button(f_lbl1, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 15, "bold"), bg="#0EDF1F", fg="white")
        self.face_recog_btn.place(relx=0.5, rely=0.711, anchor='center', width=220, height=40)




        #===== Face Recognition ====== 
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                # Predict the face
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                print(f"\n🔍 Face Detected:")
                print(f"   Predicted ID: {id}")
                print(f"   Confidence: {confidence}%")
                print(f"   Raw Distance: {predict}")

                # Initialize default values
                student_name = "Unknown"
                student_reg = "Unknown"
                student_roll = "Unknown"
                student_dep = "Unknown"
                found_in_db = False

                # DB Connection - Fetch student details using registration number
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="2006",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()

                    # Search for student by registration number
                    my_cursor.execute("SELECT name, reg, roll, dep FROM students WHERE reg=%s", (str(id),))
                    result = my_cursor.fetchone()
                    
                    if result:
                        student_name = result[0]
                        student_reg = result[1]
                        student_roll = result[2]
                        student_dep = result[3]
                        found_in_db = True
                        print(f"   ✅ Found in DB: {student_name} (Reg: {student_reg})")
                    else:
                        print(f"   ⚠️ ID {id} not found in database")
                        # Show what's in database for debugging
                        my_cursor.execute("SELECT reg, name FROM students")
                        all_students = my_cursor.fetchall()
                        print(f"   📋 Students in DB: {all_students}")

                    conn.close()
                    
                except mysql.connector.Error as db_err:
                    print(f"   ❌ Database error: {db_err}")
                except Exception as e:
                    print(f"   ❌ Error: {e}")

                # FIXED: Lower confidence threshold for better matching
                # Show details if confidence is good (above 50% for testing, adjust later)
                if confidence > 50 and found_in_db:
                    # Draw GREEN rectangle for recognized face
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    
                    # Display student information
                    cv2.putText(img, f"Name: {student_name}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Reg: {student_reg}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Roll: {student_roll}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Dept: {student_dep}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Match: {confidence}%", (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)
                    print(f"   ✅ MATCH SUCCESS!")
                else:
                    # Draw RED rectangle for unknown face
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                    cv2.putText(img, f"Confidence: {confidence}%", (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)
                    if found_in_db:
                        print(f"   ⚠️ Low confidence - Need more training images")
                    else:
                        print(f"   ⚠️ ID not in database")

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        # Check if opencv-contrib-python is installed
        try:
            # Load cascade and recognizer
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            
            # Check if classifier.xml exists
            if not os.path.exists("classifier.xml"):
                messagebox.showerror("Error", "classifier.xml not found!\n\nPlease train the model first using the 'Train Data' option.")
                return
                
            clf.read("classifier.xml")  
            print("✅ Model loaded successfully from classifier.xml")
            
        except AttributeError:
            messagebox.showerror("Error", "opencv-contrib-python is not installed!\n\nPlease run:\npip uninstall opencv-python\npip install opencv-contrib-python")
            return
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load classifier.xml\n\nError: {str(e)}\n\nMake sure you have trained the model first.")
            return

        # Start video capture
        video_cap = cv2.VideoCapture(0)
        
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Cannot access camera!")
            return

        print("\n🎥 Starting face recognition...")
        print("Press ENTER or close the window to exit\n")

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition System", img)

            # Press Enter (13) to exit or window close
            if cv2.waitKey(1) == 13 or cv2.getWindowProperty("Face Recognition System", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()
        print("✅ Face recognition stopped")



if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
    