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
        self.root = root
        self.root.geometry("1552x790+0+0")
        self.root.title("Face Recognition System-- Train Data")

        # Heading Label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="#F4E1A8", fg="green")
        title_lbl.place(x=0, y=0, width=1552, height=45)

        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # ----- Animated GIF Top -------
        self.canvas = Canvas(self.root, width=1532, height=325)
        self.canvas.place(x=0, y=46, width=1535, height=300)

        # Load animated GIF with error handling
        try:
            gif_path = os.path.join(script_dir, "Images", "Top Image of Train data set.gif")
            self.gif = Image.open(gif_path)
            self.frames = [ImageTk.PhotoImage(img.resize((1535, 300))) for img in ImageSequence.Iterator(self.gif)]
            self.frame_index = 0

            # Add first frame
            self.bg_image = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])

            # Function to animate GIF
            self.animate_gif()
        except FileNotFoundError:
            print(f"Warning: GIF not found at {gif_path}")
            self.canvas.create_text(767, 150, text="GIF Image Not Found", font=("Arial", 20), fill="red")

        # --->> GIF End <<----

        # Bottom image
        try:
            img_bottam_path = os.path.join(script_dir, "Images", "Bottam image Data train.jpg")
            img_bottam = Image.open(img_bottam_path)
            img_bottam = img_bottam.resize((1535, 450), Image.Resampling.LANCZOS)
            self.photoimg_bottam = ImageTk.PhotoImage(img_bottam)

            f_lbl = Label(self.root, image=self.photoimg_bottam)
            f_lbl.place(x=0, y=343, width=1535, height=450)
        except FileNotFoundError:
            print(f"Warning: Bottom image not found at {img_bottam_path}")
            f_lbl = Label(self.root, bg="lightgray", text="Image Not Found")
            f_lbl.place(x=0, y=343, width=1535, height=450)

        # Button
        b1_1 = Button(f_lbl, text="TRAIN DATA", command=self.train_classifire, cursor="hand2", font=("times new roman", 15, "bold"), bg="#E21EE9", fg="white")
        b1_1.place(relx=0.5, rely=0.8, anchor="center", width=220, height=40)

    def train_classifire(self):
        # Use relative path for data directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(script_dir, "data")
        
        # Check if data directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory not found!\n\nExpected path: {data_dir}\n\nPlease create the 'data' folder and add training images.")
            return
        
        # Get all files in data directory
        files = os.listdir(data_dir)
        if not files:
            messagebox.showwarning("Warning", "No training images found in data folder!")
            return
        
        path = [os.path.join(data_dir, file) for file in files]

        faces = []
        ids = []
        
        print("\n" + "="*60)
        print("🎓 STARTING TRAINING PROCESS")
        print("="*60)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
        for image_path in path:
            try:
                # Skip non-image files
                if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                    print(f"⚠️  Skipping non-image file: {os.path.basename(image_path)}")
                    continue
                
                filename = os.path.basename(image_path)
                parts = filename.split('.')

                # Validate filename format (e.g., User.1.1.jpg)
                if len(parts) < 3 or not parts[1].isdigit():
                    print(f"❌ Invalid filename format: {filename}")
                    print(f"   Expected format: User.REG_NUMBER.IMAGE_NUMBER.jpg")
                    print(f"   Example: User.1.1.jpg, User.1.2.jpg, etc.")
                    continue
                
                id = int(parts[1])  # extract reg number
                
                # Read and process image
                img = cv2.imread(image_path)
                if img is None:
                    print(f"❌ Could not read image: {filename}")
                    continue
                
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                # Detect faces in the image
                detected_faces = face_cascade.detectMultiScale(gray, 1.1, 5)
                
                if len(detected_faces) == 0:
                    print(f"⚠️  No face detected in: {filename}")
                    continue
                
                # Use the first detected face
                for (x, y, w, h) in detected_faces:
                    face_roi = gray[y:y+h, x:x+w]
                    
                    # Resize to standard size for better recognition
                    face_roi = cv2.resize(face_roi, (200, 200))
                    
                    faces.append(face_roi)
                    ids.append(id)
                    
                    print(f"✅ Processed: {filename} -> ID: {id}")
                    
                    cv2.imshow("Training", face_roi)
                    cv2.waitKey(1)
                    break  # Only use first face in image
                    
            except Exception as e:
                print(f"❌ Error processing {image_path}: {e}")
                continue

        cv2.destroyAllWindows()

        # Check if any faces were found
        if len(faces) == 0:
            messagebox.showerror("Error", 
                "No valid faces detected in training images!\n\n"
                "Possible issues:\n"
                "1. Images don't contain clear faces\n"
                "2. Filename format incorrect (use: User.REG.NUM.jpg)\n"
                "3. Images are corrupted\n\n"
                "Please check your images and try again.")
            return

        ids = np.array(ids)
        
        print("\n" + "="*60)
        print(f"📊 TRAINING SUMMARY")
        print("="*60)
        print(f"Total images processed: {len(faces)}")
        print(f"Unique IDs found: {len(set(ids))}")
        print(f"IDs: {sorted(set(ids))}")
        print("="*60 + "\n")

        # Train the classifier and save
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            
            print("✅ Training completed successfully!")
            print(f"📁 Model saved as: classifier.xml\n")
            
            messagebox.showinfo("Success", 
                f"Training completed successfully!\n\n"
                f"📊 Statistics:\n"
                f"  • Images trained: {len(faces)}\n"
                f"  • Unique persons: {len(set(ids))}\n"
                f"  • Registration IDs: {sorted(set(ids))}\n\n"
                f"Model saved as classifier.xml")
                
        except AttributeError:
            messagebox.showerror("Error", 
                "opencv-contrib-python is not installed!\n\n"
                "Please run:\n"
                "pip uninstall opencv-python\n"
                "pip install opencv-contrib-python")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed!\n\nError: {str(e)}")

    def animate_gif(self):
        if hasattr(self, 'frames') and len(self.frames) > 0:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.canvas.itemconfig(self.bg_image, image=self.frames[self.frame_index])
            self.root.after(50, self.animate_gif)  # Adjust speed (lower = faster)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()