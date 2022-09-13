from base64 import b16decode
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter.font import BOLD 
from PIL import Image,ImageTk
from Students import Student
from train import Train
from faces_recognition import Faces_recognition
from attendance import Attendance
import os

class Face_Recognition_System:
    def __init__(self,root):
       self.root = root 
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")

       img = Image.open(r"Images\frs.jpg")
       img =img.resize((1530,800),Image.Resampling.LANCZOS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl =Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=1530,height=800)

       title_lbl =Label(f_lbl ,text = "Face Recognition System", font = ("times new roman",35,"bold"),bg ="white" ,fg ="red")
       title_lbl.place(x=0,y=0,width=1530,height=45)

       img1 = Image.open(r"Images\SD.jpg")
       img1 = img1.resize((220,220),Image.Resampling.LANCZOS)
       self.photoimg1 = ImageTk.PhotoImage(img1)
       
       b1 =Button(f_lbl , image=self.photoimg1,command=self.student_details,cursor="hand2")
       b1.place(x=200,y=100,width=220,height=220)

       b1_1 = Button(f_lbl,text="Student Details", cursor="hand2",command=self.student_details ,font=("times new roman",15,"bold"),bg = "skyblue" , fg ="blue")
       b1_1.place(x=200,y=300,width=220,height=35)

       img2 = Image.open(r"Images\facerecognition.jpg")
       img2 = img2.resize((220,220),Image.Resampling.LANCZOS)
       self.photoimg2 = ImageTk.PhotoImage(img2)

       b2 =Button(f_lbl , image=self.photoimg2,command=self.face_data,cursor="hand2")
       b2.place(x=700,y=100,width=220,height=220)

       b2_1 = Button(f_lbl,text="Face Recognition",command=self.face_data, cursor="hand2",font=("times new roman",15,"bold"),bg = "skyblue" , fg ="blue")
       b2_1.place(x=700,y=300,width=220,height=35)

       img3 = Image.open(r"Images\attendance.jpg")
       img3 = img3.resize((220,220),Image.Resampling.LANCZOS)
       self.photoimg3 = ImageTk.PhotoImage(img3)
       
       b3 =Button(f_lbl ,command=self.attendace_p, image=self.photoimg3,cursor="hand2")
       b3.place(x=1200,y=100,width=220,height=220)

       b3_1 = Button(f_lbl,text="Attendance",cursor="hand2",command=self.attendace_p ,font=("times new roman",15,"bold"),bg = "skyblue" , fg ="blue")
       b3_1.place(x=1200,y=300,width=220,height=35)

       img4 = Image.open(r"Images\dataset.jpg")
       img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
       self.photoimg4 = ImageTk.PhotoImage(img4)
       
       b4 =Button(f_lbl , image=self.photoimg4,command=self.train_data,cursor="hand2")
       b4.place(x=200,y=400,width=220,height=220)

       b4_1 = Button(f_lbl,text="TrainData",command=self.train_data, cursor="hand2" ,font=("times new roman",15,"bold"),bg = "skyblue" , fg ="blue")
       b4_1.place(x=200,y=600,width=220,height=35)

       img5 = Image.open(r"Images\localimage.jpg")
       img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
       self.photoimg5 = ImageTk.PhotoImage(img5)
       
       b5 =Button(f_lbl , image=self.photoimg5,cursor="hand2",command=self.open_img)
       b5.place(x=700,y=400,width=220,height=220)

       b5_1 = Button(f_lbl,text="Photos", cursor="hand2",command=self.open_img ,font=("times new roman",15,"bold"),bg = "skyblue" , fg ="blue")
       b5_1.place(x=700,y=600,width=220,height=35)

       img6 = Image.open(r"Images\exit.jpg")
       img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
       self.photoimg6 = ImageTk.PhotoImage(img6)
       
       b6 =Button(f_lbl ,command=self.iExit, image=self.photoimg6,cursor="hand2")
       b6.place(x=1200,y=400,width=220,height=220)

       b6_1 = Button(f_lbl,text="Exit", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg = "skyblue" , fg ="blue")
       b6_1.place(x=1200,y=600,width=220,height=35)

    def open_img(self):
         os.startfile("datas")     #Data is the folder nameof image 

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    




       #functions buttons

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Faces_recognition(self.new_window)

    def attendace_p(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    


if __name__ == "__main__" :
    root = Tk() 
    obj = Face_Recognition_System(root)
    root.mainloop()

