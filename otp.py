import random
from tkinter import *
from tkinter import ttk

class otp:
    def __init__(self,window):
        self.window = window
        self.window.title("One Time Password login system")
        self.window.geometry("1920x1080+0+0")
        
        title = Label(self.window,text="OTP login system",bd=0,font=("times new roman",30,"bold"),bg="white",fg="purple")
        title.pack(side=TOP,fill=X)

        def generate_OTP():

            list1 = []

            a = random.randint(0,9)
            b = random.randint(0,9)
            c = random.randint(0,9)
            d = random.randint(0,9)
            list1.append(a)
            list1.append(b)
            list1.append(c)
            list1.append(d)
            otp = list1
            

            label2 = Label(frame1,text=otp,bg="white",fg="black",font=("times new roman",20,"bold"))
            label2.grid(row=6,column=2,padx=600,pady=50,sticky=W)

         


        frame1 = Frame(self.window,bd=1,relief=RIDGE,bg="skyblue")
        frame1.place(x=20,y=70,height=660,width=1300)

        label1 = Label(frame1,text="Click on button to generate OTP ",bg="white",fg="black",font=(20))
        label1.grid(row=4,column=2,padx=450,pady=50,sticky=W)

        generate_button = Button(frame1,text="Generate OTP",height=2,width=11, command=generate_OTP)
        generate_button.grid(row=5, column=2,pady=20,padx=10)


window = Tk()
ob = otp(window)
window.mainloop()

