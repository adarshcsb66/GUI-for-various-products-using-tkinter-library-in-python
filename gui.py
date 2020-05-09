from tkinter import *
import math
from tkinter import messagebox
from PIL import Image,ImageTk
global root
root=Tk()
root.iconbitmap("D:\Screenshot_24_.ico")

# def click(num):
#     global a,b,op
#     if(num==-2):
#         e.delete(0,END)
#         return
#     if(num==-1):
#         op="+"
#         if(a==False):
#             a=e.get()
#             a=int(a)
#             e.delete(0,END)
#             print("h1")
#             return
#         if(a!=False and b==False):
#             b=e.get()
#             b=int(b)
#             a=int(a)+int(b)
#             b=False
#             e.delete(0,END)
#             print("h2")
#             return
#     if(num==-4):
#         op="-"
#         if(a==False):
#             a=e.get()
#             a=int(a)
#             e.delete(0,END)
#             print("h1")
#             return
#         if(a!=False and b==False):
#             b=e.get()
#             b=int(b)
#             a=int(a)-int(b)
#             b=False
#             e.delete(0,END)
#             print("h2")
#             return   
#     if(num==-5):
#         op="*"
#         if(a==False):
#             a=e.get()
#             a=int(a)
#             e.delete(0,END)
#             print("h1")
#             return
#         if(a!=False and b==False):
#             b=e.get()
#             b=int(b)
#             a=int(a)*int(b)
#             b=False
#             e.delete(0,END)
#             print("h2")
#             return
#     if(num==-6):
#         op="/"
#         if(a==False):
#             a=e.get()
#             a=float(a)
#             e.delete(0,END)
#             print("h1")
#             return
#         if(a!=False and b==False):
#             b=e.get()
#             b=int(b)
#             a=int(a)/int(b)
#             b=False
#             e.delete(0,END)
#             print("h2")
#             return     
#     if(num==-7):
#         a=e.get()
#         b=int(a)
#         b*=math.pi
#         b/=180
#         e.insert(0,math.tan(b))
#         return
#     if(num==-8):
#         a=e.get()
#         b=int(a)
#         b*=math.pi
#         b/=180
#         e.insert(0,math.sin(b))
#         return
#     if(num==-9):
#         a=e.get()
#         b=int(a)
#         b*=math.pi
#         b/=180
#         e.insert(0,math.cos(b))
#         return     
#     if(num==-3):
#         print(a)
#         print(b)
#         b=e.get()
#         print(int(b))
#         e.delete(0,END)
#         if(op=="+"):
#             e.insert(0,int(a)+int(b))
#         if(op=="-"):
#             e.insert(0,int(a)-int(b))
#         if(op=="*"):
#             e.insert(0,int(a)*int(b))
#         if(op=="/"):
#             e.insert(0,int(a)/int(b))
#         a=False
#         b=False
#         return
#     curr=e.get()
#     e.delete(0,END)
#     e.insert(0,str(curr)+str(num))

# e=Entry(root,text="",width=27)
# e.grid(row=0,column=0,columnspan=3)
# button1=Button(root,text="1",padx=20,pady=10,command=lambda:click(1)) 
# button2=Button(root,text="2",padx=20,pady=10,command=lambda:click(2))
# button3=Button(root,text="3",padx=20,pady=10,command=lambda:click(3))
# button4=Button(root,text="4",padx=20,pady=10,command=lambda:click(4))
# button5=Button(root,text="5",padx=20,pady=10,command=lambda:click(5))
# button6=Button(root,text="6",padx=20,pady=10,command=lambda:click(6))
# button7=Button(root,text="7",padx=20,pady=10,command=lambda:click(7))
# button8=Button(root,text="8",padx=20,pady=10,command=lambda:click(8))
# button9=Button(root,text="9",padx=20,pady=10,command=lambda:click(9))
# button0=Button(root,text="0",padx=20,pady=10,command=lambda:click(0))
# buttonp=Button(root,text="+",padx=19,pady=10,command=lambda:click(-1))
# buttonc=Button(root,text="clear",padx=37,pady=10,command=lambda:click(-2))
# buttond=Button(root,text="=",padx=46,pady=10,command=lambda:click(-3))
# buttonm=Button(root,text="-",padx=21,pady=10,command=lambda:click(-4))
# buttoni=Button(root,text="*",padx=20,pady=10,command=lambda:click(-5))
# buttonk=Button(root,text="/",padx=20,pady=10,command=lambda:click(-6))
# buttont=Button(root,text="tan",padx=15,pady=10,command=lambda:click(-7))
# buttons=Button(root,text="sin",padx=15,pady=10,command=lambda:click(-8))
# buttong=Button(root,text="cos",padx=15,pady=10,command=lambda:click(-9))
# quit_b=Button(root,text="Exit",padx=70,pady=10,command=root.quit)
# button1.grid(row=1,column=0)
# button2.grid(row=1,column=1)
# button3.grid(row=1,column=2)

# button4.grid(row=2,column=0)
# button5.grid(row=2,column=1)
# button6.grid(row=2,column=2)

# button7.grid(row=3,column=0)
# button8.grid(row=3,column=1)
# button9.grid(row=3,column=2)

# button0.grid(row=4,column=0)
# buttonc.grid(row=4,column=1,columnspan=2)
# buttonp.grid(row=5,column=0)
# buttond.grid(row=5,column=1,columnspan=2)
# buttonm.grid(row=6,column=0)
# buttoni.grid(row=6,column=1)
# buttonk.grid(row=6,column=2)

# buttont.grid(row=7,column=0)
# buttons.grid(row=7,column=1)
# buttong.grid(row=7,column=2)
# quit_b.grid(row=8,column=0,columnspan=3)

# global img_no
# global status
# img_no=1
# status=Label(root,text="Image "+str(img_no)+" of 7",relief=SUNKEN)
# global img
# img=ImageTk.PhotoImage(Image.open("1.jpg"))
# global img_lbl
# img_lbl=Label(root,image=img)
# img_lbl.grid(row=0,column=0,columnspan=3)
# def prev():
#     global status,img_no,root,img
#     img_no-=1
#     print("here")
#     global img_lbl
#     img_lbl.grid_forget()
#     if(img_no==0):
#         img_no+=7
#     print(img_no)
#     img=ImageTk.PhotoImage(Image.open(str(img_no)+".jpg"))
#     img_lbl=Label(root,image=img)
#     img_lbl.grid(row=0,column=0,columnspan=3)
#     status=Label(root,text="Image "+str(img_no)+" of 7",relief=SUNKEN)
#     status.grid(row=2,column=0,columnspan=3,sticky=W+E)


# def next():
#     global img_no,root,img,status
#     img_no+=1
#     print("here")
#     global img_lbl
#     img_lbl.grid_forget()
#     if(img_no==8):
#         img_no=1
#     img=ImageTk.PhotoImage(Image.open(str(img_no)+".jpg"))
#     img_lbl=Label(root,image=img)
#     img_lbl.grid(row=0,column=0,columnspan=3)
#     status=Label(root,text="Image "+str(img_no)+" of 7",relief=SUNKEN)
#     status.grid(row=2,column=0,columnspan=3,sticky=W+E)


# prev=Button(root,text="<<",command=prev)
# exit=Button(root,text="exit",command=root.quit)
# next=Button(root,text=">>",command=next)
# prev.grid(row=1,column=0)
# exit.grid(row=1,column=1)
# next.grid(row=1,column=2)
# status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def popup_f():
    messagebox.showinfo("Name of pop up","Content of pop up")

popup=Button(root,text="Click Me!",command=popup_f)
popup.pack()

root.mainloop()

