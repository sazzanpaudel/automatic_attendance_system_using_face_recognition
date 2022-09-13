from base64 import b16decode
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD 
from PIL import Image,ImageTk
from email import message
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
class Train:
    def __init__(self,root):
       self.root = root 
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")
       title_lbl =Label(self.root ,text = "Train DataSet", font = ("times new roman",35,"bold"),bg ="white" ,fg ="red")
       title_lbl.place(x=0,y=0,width=1530,height=45)


       img = Image.open(r"C:\Users\Dell\OneDrive\Desktop\Main Project\Images\frs.jpg")
       img =img.resize((1530,900),Image.Resampling.LANCZOS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl =Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=50,width=1530,height=900)

       img9 = Image.open("Images\clicks_here.jpg")
       img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
       self.photoimg9 = ImageTk.PhotoImage(img9)
       
       b9 =Button(f_lbl , image=self.photoimg9,command=self.train_classifier,cursor="hand2")
       b9.place(x=610,y=100,width=300,height=300)

       b9_1 = Button(f_lbl,text="Train Data", command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg = "skyblue" , fg ="blue")
       b9_1.place(x=610,y=400,width=300,height=35)



    def train_classifier(self):
            data_dir=("mydata/")
            path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L')  #Gray Scale image 
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

            #=========Train the classifier And save =========
            clf=cv2.face_LBPHFaceRecognizer.create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training datasets completed!!")


       
    






if __name__ == "__main__" :
    root = Tk() 
    obj = Train(root)
    root.mainloop()