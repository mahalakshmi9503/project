from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL.ImageTk import PhotoImage
from tkinter import messagebox

def custoreg(r):
   r.destroy()
   font1=("Times New Roman",15,"bold")
   r=Tk() 
   r.geometry("1500x700")
   topframe=Frame(r,width=1500,height=70,bg="violet")
   topframe.place(relx=0.001,rely=0.001)
   label1=Label(topframe,text="Plants of Cartening",bg="violet",font=font1)
   label1.place(relx=0.4,rely=0.1)

   topframe=Frame(r,width=300,height=50,bg="green")
   topframe.place(relx=0.4,rely=0.1)
   label2=Label(topframe,text="custoreg",bg="green",font=font1)
   label2.place(relx=0.3,rely=0.1)

   mainframe=Frame(r,width=1600,height=670,bg="yellow")
   mainframe.place(relx=0.001,rely=0.1)

   img8=PhotoImage(Image.open("anu.jpg"))
   button=Button(mainframe,image=img8,bg="white")
   button.place(relx=0.001,rely=0.001)



      
   mainframe=Frame(r,width=600,height=300,bg="violet")
   mainframe.place(relx=0.3,rely=0.3)

   label3=Label(mainframe,text="Enter the name",bg="white",font=font1)
   label3.place(relx=0.001,rely=0.1)
   entry1=Entry(mainframe,font=font1)
   entry1.place(relx=0.4,rely=0.1)

   label4=Label(mainframe,text="Enter the Aathar nom",bg="white",font=font1)
   label4.place(relx=0.001,rely=0.2)
   entry2=Entry(mainframe,font=font1)
   entry2.place(relx=0.4,rely=0.2)

   label5=Label(mainframe,text="Enter phone nom",bg="white",font=font1)
   label5.place(relx=0.001,rely=0.3)
   entry3=Entry(mainframe,font=font1)
   entry3.place(relx=0.4,rely=0.3)

   def custoreg1():
      f=open("customer.txt","a")
      f.write("\n"+entry1.get()+"\t"+entry2.get()+"\t"+entry3.get())
      f.close()
      messagebox.showinfo("DATA SUCCESSFULLY INSERTED","DATA INSERTED SUCCESSFULLY")

    

   button=Button(mainframe,text="Submit",bg="white",font=font1,command=custoreg1)
   button.place(relx=0.5,rely=0.5)

   bottomframe=Frame(r,width=1600,height=70,bg="violet")
   bottomframe.place(relx=0.001,rely=0.9)
   label6=Label(bottomframe,text="Plants.2024",bg="violet",font=font1)
   label6.place(relx=0.4,rely=0.1)
   r.mainloop()

def customer(r):
   r.destroy()
   font1=("Times New Roman",20,"bold")
   r=Tk()        
   r.geometry("1600x70")
   topframe=Frame(r,width=1600,height=70,bg="pink")
   topframe.place(relx=0.001,rely=0.001)
   label=Label(topframe,text="Plants Of Cartening",bg="pink",font=font1)
   label.place(relx=0.3,rely=0.4)

   topframe=Frame(r,width=300,height=50,bg="red")
   topframe.place(relx=0.4,rely=0.1)
   label1=Label(topframe,text="CUSTOMER LOGIN",bg="white",font=font1)
   label1.place(relx=0.001,rely=0.1)

   mainframe=Frame(r,width=1600,height=670,bg="light blue")
   mainframe.place(relx=0.001,rely=0.1)

   img1=PhotoImage(Image.open("abi3.jpg"))
   button=Button(mainframe,image=img1,bg="white")
   button.place(relx=0.001,rely=0.002)
   label3=Label(mainframe,text="Areca palm plant.Rs=240",bg="white",font=font1)
   label3.place(relx=0.002,rely=0.4)

   img2=PhotoImage(Image.open("abi4.jpg"))
   button=Button(mainframe,image=img2,bg="white")
   button.place(relx=0.002,rely=0.5)
   label3=Label(mainframe,text="Oxygen enriching.Rs=340",bg="white",font=font1)
   label3.place(relx=0.006,rely=0.9)

   img3=PhotoImage(Image.open("abi5.jpg"))
   button=Button(mainframe,image=img3,bg="white")
   button.place(relx=0.3,rely=0.001)
   label4=Label(mainframe,text="Anthurium Plant.Rs=320",bg="white",font=font1)
   label4.place(relx=0.3,rely=0.4)

   img5=PhotoImage(Image.open("abi2.jpg"))
   button=Button(mainframe,image=img5,bg="white")
   button.place(relx=0.3,rely=0.5)
   label5=Label(mainframe,text="Jasmine Plant.Rs=450",bg="white",font=font1)
   label5.place(relx=0.3,rely=0.9)

   img6=PhotoImage(Image.open("abi7.jpg"))
   button=Button(mainframe,image=img6,bg="white")
   button.place(relx=0.6,rely=0.001)
   label6=Label(mainframe,text=" Rose plant.Rs=340",bg="white",font=font1)
   label6.place(relx=0.6,rely=0.4)  


   imag7=PhotoImage(Image.open("abi9.jpg"))
   button=Button(mainframe,image=imag7,bg="white")
   button.place(relx=0.6,rely=0.5)
   label7=Label(mainframe,text="Crismase plant.Rs=370",bg="white",font=font1)
   label7.place(relx=0.6,rely=0.9) 
   r.mainloop()

def customerlogin(r):
   r.destroy()
   font1=("Times New Roman",15,"bold")
   r=Tk()
   r.geometry("1500x800")
   topframe=Frame(r,width=1600,height=70,bg="pink")
   topframe.place(relx=0.001,rely=0.001)
   label1=Label(topframe,text="Plants Of Cartening",bg="pink",font=font1)
   label1.place(relx=0.4,rely=0.4)

   topframe=Frame(r,width=300,height=50,bg="light green")
   topframe.place(relx=0.4,rely=0.1)
   label4=Label(topframe,text="Customer login",bg="white",font=font1)
   label4.place(relx=0.3,rely=0.1)

   mainframe=Frame(width=1600,height=670,bg="blue")
   mainframe.place(relx=0.001,rely=0.1)
 
   img4=PhotoImage(Image.open("abi6.jpg"))
   button=Button(mainframe,image=img4,bg="white")
   button.place(relx=0.001,rely=0.001)



   mainframe=Frame(r,width=500,height=250,bg="white")
   mainframe.place(relx=0.3,rely=0.3)
 

   label2=Label(mainframe,text="Enter the User name",bg="light green",font=font1)
   label2.place(relx=0.001,rely=0.1)
   entry1=Entry(mainframe,font=font1)
   entry1.place(relx=0.4,rely=0.1)
   label3=Label(mainframe,text="Enter the pass word",bg="light green",font=font1)
   label3.place(relx=0.001,rely=0.3)
   entry2=Entry(mainframe,font=font1)
   entry2.place(relx=0.4,rely=0.3)



   def check():
      a=entry1.get()
      b=entry2.get()
      if(a=="abi" and b=="8875"):
         customer(r)
      else:
         customerlogin(r)

      

   button=Button(mainframe,text="Submit",bg="light green",font=font1,command=check)
   button.place(relx=0.4,rely=0.5)


   bottomframe=Frame(r,width=1600,height=70,bg="pink")
   bottomframe.place(relx=0.001,rely=0.9)
   label4=Label(bottomframe,text="Plants.2024",bg="pink",font=font1)
   label4.place(relx=0.4,rely=0.4)
   r.mainloop()



   
   
font1=("Times New Roman",20,"bold")
r=Tk()
r.geometry("1600x70")
topframe=Frame(r,width=1600,height=80,bg="light blue")
topframe.place(relx=0.001,rely=0.001)
label1=Label(topframe,text="Plants Of Cartening",bg="light blue",font=font1)
label1.place(relx=0.3,rely=0.4)

mainframe=Frame(r,width=1600,height=670,bg="red")
mainframe.place(relx=0.001,rely=0.1)

img=PhotoImage(Image.open("abi1.jpg"))
button=Button(mainframe,image=img,bg="white") # type: ignore
button.place(relx=0.001,rely=0.001)


button=Button(mainframe,text="Customer Login",bg="white",font=font1,command=lambda:customerlogin(r))
button.place(relx=0.3,rely=0.4)
button1=Button(mainframe,text="Customer Registretion",bg="white",font=font1,command=lambda:custoreg(r))
button1.place(relx=0.3,rely=0.5)


bottomframe=Frame(r,width=1600,height=60,bg="light blue")
bottomframe.place(relx=0.001,rely=0.9)
label2=Label(bottomframe,text="Plants.2024",bg="light blue",font=font1)
label2.place(relx=0.3,rely=0.4)
r.mainloop()