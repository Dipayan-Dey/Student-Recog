import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
import cv2
import os

# Making class
class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System-- Train Data")

        # Heading Label
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="#F4E1A8", fg="green")
        title_lbl.place(x=0,y=0,width=1552,height=45)


        # ----- Animated GIF Top -------
        self.canvas = Canvas(self.root, width=1532, height=325)
        self.canvas.place(x=0, y=46, width=1535, height=300)

        # Load animated GIF
        self.gif = Image.open(r"D:\Student Face Recog system\Images\Top Image of Train data set.gif")
        self.frames = [ImageTk.PhotoImage(img.resize((1535, 300))) for img in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0

        # Add first frame
        self.bg_image = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])

        # Function to animate GIF
        self.animate_gif()

        #--->> GIF End <<----
        

        # Bottam image
        img_bottam=Image.open(r"D:\Student Face Recog system\Images\Bottam image Data train.jpg")
        img_bottam=img_bottam.resize((1535, 450),Image.Resampling.LANCZOS)
        self.photoimg_bottam=ImageTk.PhotoImage(img_bottam)

        f_lbl=Label(self.root,image=self.photoimg_bottam)
        f_lbl.place(x=0,y=343, width=1535, height=450)

        # Button
        b1_1 = Button(f_lbl, text="TRAIN DATA",command=self.train_classifire ,cursor="hand2",font=("times new roman", 15, "bold"),bg="#E21EE9", fg="white")

        b1_1.place(relx=0.5, rely=0.8, anchor="center", width=220, height=40)



    def train_classifire(self):
        data_dir = r"D:\Student Face Recog system\data"
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Gray scale image
            imageNp=np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])  # extract reg no

            filename = os.path.split(image)[1]
            parts = filename.split('.')

            if len(parts) >= 3 and parts[1].isdigit():
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(10)
            else:
                print(f"Skipping invalid file: {filename}")


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(10) #Press enter to close window
        ids=np.array(ids)

        # Train the clissifire and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed.")

    def animate_gif(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.canvas.itemconfig(self.bg_image, image=self.frames[self.frame_index])
        self.root.after(50, self.animate_gif)  # Adjust speed (lower = faster)

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()