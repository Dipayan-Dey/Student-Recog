import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
import mysql.connector
import cv2
import os

# Making class
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System-- Face Detector")

        # Heading (must be inside __init__)
        title_lbl = Label(self.root, text="FACE RECOGNITION",font=("times new roman", 35, "bold"),bg="#2FEF5C", fg="#4242E4")
        title_lbl.place(x=0, y=0, width=1552, height=45)

    # Laft image
        img_left=Image.open(r"D:\Student Face Recog system\Images\Bottam image Data train.jpg")
        img_left=img_left.resize((750, 800),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=47, width=750, height=800)


    # Right Image 
        img_right=Image.open(r"D:\Student Face Recog system\Images\Right image.jpg")
        img_right=img_right.resize((800, 800),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl1=Label(self.root,image=self.photoimg_right)
        f_lbl1.place(x=752,y=47, width=800, height=800)

    # Button 
        self.face_recog = Button(f_lbl1, text="Face Recogination", cursor="hand2",command=self.face_recog,font=("times new roman", 15, "bold"), bg="#0EDF1F", fg="white")
        self.face_recog.place(relx=0.5, rely=0.711, anchor='center', width=220, height=40)




        #===== Face Recognition ====== 
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                # DB Connection
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Ayan@123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()

                # Fetch details from DB
                my_cursor.execute("SELECT name FROM students WHERE reg=%s", (id,))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                my_cursor.execute("SELECT roll FROM students WHERE reg=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT dep FROM students WHERE reg=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                conn.close()

                # Show details if confidence good
                if confidence > 77:
                    cv2.putText(img, f"Reg.no: {r}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {i}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        # Load cascade and recognizer
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  
        print("Training completed and model saved as classifier.xml")

        # Start video capture
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13 or cv2.getWindowProperty("Welcome to Face Recognition", cv2.WND_PROP_VISIBLE) < 1:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
