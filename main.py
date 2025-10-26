# GUI FILE

import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from student import Student
from train import Train
from face_recognization import Face_Recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System")

        # === Base directory (auto-detect project location)
        self.base_dir = os.path.dirname(__file__)
        self.img_dir = os.path.join(self.base_dir, "Images")

        # Heading 
        title_lbl = Label(
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="#001f3f", fg="cyan"
        )
        title_lbl.place(x=0, y=0, width=1552, height=45)

        # ---- Top 3 Images ----
        img = Image.open(os.path.join(self.img_dir, "main1.webp"))
        img = img.resize((510, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=48, width=510, height=130)

        img2 = Image.open(os.path.join(self.img_dir, "Main2.png"))
        img2 = img2.resize((510, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=510, y=48, width=510, height=130)

        img3 = Image.open(os.path.join(self.img_dir, "main3.png"))
        img3 = img3.resize((530, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3).place(x=1020, y=48, width=530, height=130)

        # ---- Animated GIF Background ----
        self.canvas = Canvas(self.root, width=1552, height=650)
        self.canvas.place(x=0, y=175, width=1552, height=650)

        self.gif = Image.open(os.path.join(self.img_dir, "Animated Background.gif"))
        self.frames = [ImageTk.PhotoImage(img.resize((1552, 650))) for img in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0
        self.bg_image = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])
        self.animate_gif()

        # ---- Student Button ----
        img4 = Image.open(os.path.join(self.img_dir, "Students_button.jpeg"))
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.canvas, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=50, width=220, height=220)
        Button(self.canvas, text="Student Details", command=self.student_details,
               cursor="hand2", font=("times new roman", 15, "bold"),
               bg="#E21EE9", fg="white").place(x=200, y=250, width=220, height=40)

        # ---- Face Detection Animated Button ----
        self.face_gif = Image.open(os.path.join(self.img_dir, "Face detact button gif.gif"))
        self.face_frames = [ImageTk.PhotoImage(img.resize((220, 220))) for img in ImageSequence.Iterator(self.face_gif)]
        self.face_index = 0

        self.face_btn = Button(self.canvas, image=self.face_frames[0], cursor="hand2", command=self.face_data)
        self.face_btn.place(x=500, y=50, width=220, height=220)
        Button(self.canvas, text="Face Detector", cursor="hand2", command=self.face_data,
               font=("times new roman", 15, "bold"), bg="#39B49B", fg="white").place(x=500, y=250, width=220, height=40)
        self.animate_face_btn()

        # ---- Attendance Button ----
        img5 = Image.open(os.path.join(self.img_dir, "Attendance button.jpg"))
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        Button(self.canvas, image=self.photoimg5, cursor="hand2").place(x=800, y=50, width=220, height=220)
        Button(self.canvas, text="Student Attendance", cursor="hand2",
               font=("times new roman", 15, "bold"), bg="#EEBB21", fg="white").place(x=800, y=250, width=220, height=40)

        # ---- Help Desk ----
        img6 = Image.open(os.path.join(self.img_dir, "Help desk button.webp"))
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        Button(self.canvas, image=self.photoimg6, cursor="hand2").place(x=1100, y=50, width=220, height=220)
        Button(self.canvas, text="Help Desk", cursor="hand2",
               font=("times new roman", 15, "bold"), bg="#0FF93E", fg="white").place(x=1100, y=250, width=220, height=40)

        # ---- Model Training Button ----
        self.model_gif = Image.open(os.path.join(self.img_dir, "Model train button gif.gif"))
        self.model_frames = [ImageTk.PhotoImage(img.resize((220, 220))) for img in ImageSequence.Iterator(self.model_gif)]
        self.model_index = 0
        self.model_btn = Button(self.canvas, command=self.train_data, image=self.model_frames[0], cursor="hand2")
        self.model_btn.place(x=200, y=325, width=220, height=220)
        Button(self.canvas, text="Train Data", cursor="hand2", command=self.train_data,
               font=("times new roman", 15, "bold"), bg="#7E3AF4", fg="white").place(x=200, y=530, width=220, height=40)
        self.animate_model_btn()

        # ---- Photos Button ----
        img7 = Image.open(os.path.join(self.img_dir, "Face Button.jpg"))
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        Button(self.canvas, image=self.photoimg7, command=self.open_mig, cursor="hand2").place(x=500, y=325, width=220, height=220)
        Button(self.canvas, text="Photos", cursor="hand2", command=self.open_mig,
               font=("times new roman", 15, "bold"), bg="#F16711", fg="white").place(x=500, y=530, width=220, height=40)

        # ---- Developer Button ----
        self.developer_gif = Image.open(os.path.join(self.img_dir, "Developer gif.gif"))
        self.developer_frames = [ImageTk.PhotoImage(img.resize((220, 220))) for img in ImageSequence.Iterator(self.developer_gif)]
        self.developer_index = 0
        self.developer_btn = Button(self.canvas, image=self.developer_frames[0], cursor="hand2")
        self.developer_btn.place(x=800, y=325, width=220, height=220)
        Button(self.canvas, text="Developer", cursor="hand2",
               font=("times new roman", 15, "bold"), bg="#21BFEF", fg="white").place(x=800, y=530, width=220, height=40)
        self.animate_developer_btn()

        # ---- Exit Button ----
        img9 = Image.open(os.path.join(self.img_dir, "Wxit button logo.png"))
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        Button(self.canvas, image=self.photoimg9, cursor="hand2").place(x=1100, y=325, width=220, height=220)
        Button(self.canvas, text="Exit", cursor="hand2",
               font=("times new roman", 15, "bold"), bg="#F30D0D", fg="white").place(x=1100, y=530, width=220, height=40)

    def open_mig(self):
        os.startfile("data")

    # ===== Functions buttons =====
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def animate_gif(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.canvas.itemconfig(self.bg_image, image=self.frames[self.frame_index])
        self.root.after(30, self.animate_gif)

    def animate_face_btn(self):
        self.face_index = (self.face_index + 1) % len(self.face_frames)
        self.face_btn.config(image=self.face_frames[self.face_index])
        self.root.after(50, self.animate_face_btn)

    def animate_model_btn(self):
        self.model_index = (self.model_index + 1) % len(self.model_frames)
        self.model_btn.config(image=self.model_frames[self.model_index])
        self.root.after(70, self.animate_model_btn)

    def animate_developer_btn(self):
        self.developer_index = (self.developer_index + 1) % len(self.developer_frames)
        self.developer_btn.config(image=self.developer_frames[self.developer_index])
        self.root.after(40, self.animate_developer_btn)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
