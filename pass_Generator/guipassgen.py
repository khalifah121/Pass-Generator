from tkinter import *
import string
import random

#function
def clicked():
        
    letters=string.ascii_lowercase

    li_letter=list(letters)

    numbers=["1" ,"2","3","4","5","6","7","8","9","0"]
    symbols=["!","@","#","$","%","^","&","(",")"]

    gen=[]
    for letter in range(2):
        gen_letter=random.choice(li_letter)
        gen_symbols=random.choice(symbols)
        gen.append(gen_letter)
        gen.append(gen_symbols)


    for i in range(4):
        gen_number=random.choice(numbers)
        gen.append(gen_number)
        
    random.shuffle(gen)    

    char=""
    for f in gen:
        char+=f
    # print(char)   if you want to print d password on your terminal
    show_text.delete(1.0,"end")#text widgets index starts from 1.0 while entry starts from 0
    show_text.insert(1.0, char)


def request():
    gotten=int(input.get())
    num2=gotten*1000
    output.delete(1.0,"end")
    output.insert(1.0,num2)   
    
def switch():
    frame1.forget()
    frame2.place(x=20,y=30)    

def switchs():
    frame2.place_forget()
    frame1.place(x=0,y=0)
    
# MY Gui Screen-----
screen=Tk()

screen.title("my app")
screen.geometry("350x300")
screen.resizable(False,False)

# frame1----

frame1=Frame(screen,background="#2B547E",width=350,height=300)
frame1.place(x=0,y=0)

show_text=Text(frame1,width=20,height=1,border=0, font=("Arial",10,"bold"))
show_text.place(x=90,y=80)

btn=Button(frame1,text="Generate",bd=0,command=clicked)
btn.place(x=140,y=150)

btn2=Button(frame1,text="switch",bd=0,bg="yellow",command=switch)
btn2.place(x=280,y=30)

# frame 2------

frame2=Frame(screen,background="green",width=200,height=200,padx=50,pady=30)

input=Entry(frame2,width=20,bd=0,font=("Arial",10,"bold"))
input.grid(row=0,column=3,pady=20)

label1=Label(frame2,text="KM",fg="red",font=("Arial",10,"bold"),padx=10)
label1.grid(row=0,column=4,padx=10)

output=Text(frame2,width=20,height=1,bd=0,font=("Arial",10,"bold"))
output.grid(row=1,column=3,padx=5,pady=15)

label2=Label(frame2,text="M",fg="red",font=("Arial",10,"bold"),padx=10)
label2.grid(row=1,column=4)

btn=Button(frame2,text="Convert",fg="white",bd=0,padx=10,font=("Arial",10,"bold"),bg="#A70D2A",command=request)
btn.grid(row=2,column=3)

btn=Button(frame2,text="switch",bd=0,bg="yellow",command=switchs)
btn.place(x=150,y=103)


screen.mainloop()