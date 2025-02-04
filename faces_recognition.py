from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import string
import numpy as np
from time import strftime
from datetime import datetime

class Faces_recognition:
    def __init__(self,root):
            self.root = root 
            self.root.geometry("1530x790+0+0")
            self.root.title("face recognition system")
            title_lbl =Label(self.root ,text = "Face Recognizer", font = ("times new roman",35,"bold"),bg ="white" ,fg ="red")
            title_lbl.place(x=0,y=0,width=1530,height=45)


            img = Image.open(r"Images\frs.jpg")
            img =img.resize((1530,900),Image.Resampling.LANCZOS)
            self.photoimg=ImageTk.PhotoImage(img)

            f_lbl =Label(self.root,image=self.photoimg)
            f_lbl.place(x=0,y=50,width=1530,height=900)

            img10 = Image.open(r"Images\faces_recognition.webp")
            img10 = img10.resize((580,600),Image.Resampling.LANCZOS)
            self.photoimg10 = ImageTk.PhotoImage(img10)
            
            b10 =Button(f_lbl , image=self.photoimg10,cursor="hand2")
            b10.place(x=450,y=100,width=580,height=500)

            b10_1 = Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",25,"bold"),bg = "skyblue" , fg ="green")
            b10_1.place(x=450,y=520,width=580,height=80)



    #...................attendance...................
    def mark_attendance(self,i,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list)  and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{n} ")


    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                

                conn=mysql.connector.connect(host="localhost",username="rooting",password="Test@1234",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
               # i= "+".join(i)



                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
               # n="+".join(n)


                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
               # d="+".join(d)


                if confidence>80:
                    cv2.putText(img,f"ID:{i}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord
        

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break
        video_cap.release()
        cv2.destroyAllWindows()





        

if __name__=="__main__":
   root= Tk()
   obj=Faces_recognition(root)
   root.mainloop()        