# Class Room project
import time
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import os
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
import datetime

global ls,ls1,i,var,jj,bl,mm
global ls,ls1,i,var,jj,bl,mm
def java():
    def stream():
        lab15.config(text="_" * 110)
        lab15.place(x=488, y=55)

        base4.place(x=0, y=80)
        base_people.place(x=-22222, y=9999)
        classwork_label.place(x=-87860, y=-99200)

    def classwork():
        classwork_label.place(x=0, y=200)

        my_label1.place(x=240, y=0)
        lab15.config(text="_" * 150)
        lab15.place(x=600, y=55)
        base4.place(x=-9300, y=500)
        base_people.place(x=-22222, y=9999)

    def people():
        lab15.config(text="_" * 100)
        lab15.place(x=757, y=55)

        base4.place(x=-9300, y=500)
        base_people.place(x=200, y=100)
        classwork_label.place(x=-9980, y=-98200)
        # bo.place(x=30, y=200)

    def getback():
        base3.destroy()

    base3 = LabelFrame(base, width=1365, height=675, bg="white", bd=0)
    base3.place(x=100, y=70)
    base4 = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)
    base4.place(x=0, y=80)
    l11 = Button(base3, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                 fg="black", command=getback, cursor="hand2", bd=0)
    l11.place(x=10, y=0)

    # ------------------------------------------------------people -----------------------------------------------------------
    people_list = ["Vasudev Raut", "Keshav Jaiwal", "Prathmesh Rane", "Pranav Sangave", "Rahul Shinde",
                   "Chandrakant Shelke", "Shubham Wyavhare"]
    base_people = LabelFrame(base3, height=670, width=1365, bg="white", bd=0)

    lab5 = Label(base_people, text="Teacher", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=0)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=40)

    lab6 = Label(base_people, text="Hivale Sir", font=("verdana", 10), bg="white", bd=0, fg="black")
    lab6.place(x=30, y=80)

    lab5 = Label(base_people, text="Classmates", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=120)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=160)

    bo = LabelFrame(base_people, height=110, width=100, bg="gray", bd=0)
    scroll = Scrollbar(bo)
    scroll.pack(side=RIGHT, fill=Y)
    ans = Listbox(bo, width=140, height=7, yscrollcommand=scroll.set, font=("verdana", 10), exportselection=0, bd=0)
    for i in people_list:
        ans.insert(END, i)
    scroll.config(command=ans.yview)
    ans.pack()
    bo.place(x=30, y=200)
    # -------------------------------------------------------------------------------------------------------------------------

    classwork_label = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)

    my_label1 = Label(classwork_label, image=my_image32, width=902, height=300, bg="white")
    my_label1.place(x=0, y=0)

    # -------------------------------------------------------------------------------------------------------------------------

    lab14 = Label(base3, text="_" * 3000, font=("monotype corsiva", 10, 'bold'), bg="white", fg="black", bd=0)
    lab14.place(x=0, y=45)

    lab15 = Label(base3, text="_" * 110, font=("arial", 1), bg="#8f00ff", fg="black", bd=0)
    lab15.place(x=488, y=55)

    lab11 = Button(base3, text="Stream ", font=("monotype corsiva", 20, 'bold'), bg="white", fg="#8f00ff", width=7,
                   cursor="hand2", bd=0, command=stream)
    lab11.place(x=488, y=0)

    lab12 = Button(base3, text="Class Work  ", font=("monotype corsiva", 20, 'bold'), bg="white", width=10,
                   cursor="hand2", fg="#8f00ff", bd=0, command=classwork)
    lab12.place(x=600, y=0)

    lab13 = Button(base3, text="People ", font=("monotype corsiva", 20, 'bold'), bg="white", width=7, fg="#8f00ff",
                   bd=0, command=people, cursor="hand2")
    lab13.place(x=757, y=0)

    my_label0 = Label(base4, image=my_image23, width=902, height=300, bg="white")
    my_label0.place(x=240, y=0)
    my_label0 = Label(base4, image=my_image33, width=220, height=300, bg="white")
    my_label0.place(x=550, y=305)


def os():
    def stream():
        lab15.config(text="_" * 110)
        lab15.place(x=488, y=55)

        base4.place(x=0, y=80)
        base_people.place(x=-22222, y=9999)
        classwork_label.place(x=-87860, y=-99200)

    def classwork():
        classwork_label.place(x=0, y=200)

        my_label1.place(x=240, y=0)
        lab15.config(text="_" * 150)
        lab15.place(x=600, y=55)
        base4.place(x=-9300, y=500)
        base_people.place(x=-22222, y=9999)

    def people():
        lab15.config(text="_" * 100)
        lab15.place(x=757, y=55)

        base4.place(x=-9300, y=500)
        base_people.place(x=200, y=100)
        classwork_label.place(x=-9980, y=-98200)
        # bo.place(x=30, y=200)

    def getback():
        base3.destroy()

    base3 = LabelFrame(base, width=1365, height=675, bg="white", bd=0)
    base3.place(x=100, y=70)
    base4 = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)
    base4.place(x=0, y=80)
    l11 = Button(base3, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                 fg="black", command=getback, cursor="hand2", bd=0)
    l11.place(x=10, y=0)

    # ------------------------------------------------------people -----------------------------------------------------------
    people_list = ["Vasudev Raut", "Keshav Jaiwal", "Prathmesh Rane", "Pranav Sangave", "Rahul Shinde",
                   "Chandrakant Shelke", "Shubham Wyavhare"]
    base_people = LabelFrame(base3, height=670, width=1365, bg="white", bd=0)

    lab5 = Label(base_people, text="Teacher", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=0)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=40)

    lab6 = Label(base_people, text="Dhaygude sir", font=("verdana", 10), bg="white", bd=0, fg="black")
    lab6.place(x=30, y=80)

    lab5 = Label(base_people, text="Classmates", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=120)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=160)

    bo = LabelFrame(base_people, height=110, width=100, bg="gray", bd=0)
    scroll = Scrollbar(bo)
    scroll.pack(side=RIGHT, fill=Y)
    ans = Listbox(bo, width=140, height=7, yscrollcommand=scroll.set, font=("verdana", 10), exportselection=0, bd=0)
    for i in people_list:
        ans.insert(END, i)
    scroll.config(command=ans.yview)
    ans.pack()
    bo.place(x=30, y=200)
    # -------------------------------------------------------------------------------------------------------------------------

    classwork_label = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)



    my_label1 = Label(classwork_label, image=my_image32, width=902, height=300, bg="white")
    my_label1.place(x=0, y=100)

    # -------------------------------------------------------------------------------------------------------------------------

    lab14 = Label(base3, text="_" * 3000, font=("monotype corsiva", 10, 'bold'), bg="white", fg="black", bd=0)
    lab14.place(x=0, y=45)

    lab15 = Label(base3, text="_" * 110, font=("arial", 1), bg="#8f00ff", fg="black", bd=0)
    lab15.place(x=488, y=55)

    lab11 = Button(base3, text="Stream ", font=("monotype corsiva", 20, 'bold'), bg="white", fg="#8f00ff", width=7,
                   cursor="hand2", bd=0, command=stream)
    lab11.place(x=488, y=0)

    lab12 = Button(base3, text="Class Work  ", font=("monotype corsiva", 20, 'bold'), bg="white", width=10,
                   cursor="hand2", fg="#8f00ff", bd=0, command=classwork)
    lab12.place(x=600, y=0)

    lab13 = Button(base3, text="People ", font=("monotype corsiva", 20, 'bold'), bg="white", width=7, fg="#8f00ff",
                   bd=0, command=people, cursor="hand2")
    lab13.place(x=757, y=0)

    my_label0 = Label(base4, image=my_image22, width=902, height=300, bg="white")
    my_label0.place(x=240, y=0)
    my_label0 = Label(base4, image=my_image33, width=220, height=300, bg="white")
    my_label0.place(x=550, y=305)


def py():
    def stream():
        lab15.config(text="_" * 110)
        lab15.place(x=488, y=55)

        base4.place(x=0, y=80)
        base_people.place(x=-22222, y=9999)
        classwork_label.place(x=-87860, y=-99200)




    def classwork():
        classwork_label.place(x=0, y=100)

        my_label1.place(x=240, y=200)
        lab15.config(text="_" * 150)
        lab15.place(x=600, y=55)
        base4.place(x=-9300, y=500)
        base_people.place(x=-22222, y=9999)



    def people():
        lab15.config(text="_" * 100)
        lab15.place(x=757, y=55)

        base4.place(x=-9300,y=500)
        base_people.place(x=200, y=100)
        classwork_label.place(x=-9980, y=-98200)
        #bo.place(x=30, y=200)
    def getback():
        base3.destroy()



    base3 = LabelFrame(base, width=1365, height=675, bg="white",bd=0)
    base3.place(x=100, y=70)
    base4 = LabelFrame(base3,width=1365,height=675,bg="white",bd=0)
    base4.place(x=0,y=80)
    l11 = Button(base3, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                 fg="black", command=getback, cursor="hand2",bd=0)
    l11.place(x=10, y=0)

    #------------------------------------------------------people -----------------------------------------------------------
    people_list = ["Vasudev Raut","Keshav Jaiwal", "Prathmesh Rane","Pranav Sangave","Rahul Shinde","Chandrakant Shelke","Shubham Wyavhare"]


    base_people = LabelFrame(base3,height=670,width=1365,bg="white",bd=0)

    lab5 = Label(base_people, text="Teacher", font=("verdana", 20),bg="white",fg="blue")
    lab5.place(x=0,y=0)

    lab5 = Label(base_people, text="_"*130, font=("monotype corsiva", 10), bg="white",bd=0,fg="blue")
    lab5.place(x=0, y=40)

    lab6 = Label(base_people, text="Dahiwal Sir" , font=("verdana", 10), bg="white", bd=0, fg="black")
    lab6.place(x=30, y=80)

    lab5 = Label(base_people, text="Classmates", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=120)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=160)

    bo = LabelFrame(base_people, height=110, width=100, bg="gray", bd=0)
    scroll = Scrollbar(bo)
    scroll.pack(side=RIGHT, fill=Y)
    ans = Listbox(bo, width=140, height=7, yscrollcommand=scroll.set, font=("verdana", 10), exportselection=0, bd=0)
    for i in people_list:
        ans.insert(END,i)
    scroll.config(command=ans.yview)
    ans.pack()
    bo.place(x=30,y=200)
    #-------------------------------------------------------------------------------------------------------------------------

    def openbook():
        def getback1():
            lll.destroy()

        from tkPDFViewer import tkPDFViewer as pdf
        lll = LabelFrame(base, width=100, height=300)

        v1 = pdf.ShowPdf()

        v2 = v1.pdf_view(lll,
                         pdf_location=r"C:\Users\draut\PycharmProjects\ClassRoom_Mini_Project\Text Book\PY.pdf",
                         width=70, height=35)

        v2.pack()
        lll.place(x=500, y=150)
        l111 = Button(lll, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="white",
                      fg="black", command=getback1, cursor="hand2", bd=0)
        l111.place(x=10, y=0)

    classwork_label = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)

    labb = Button(classwork_label, text="See Text Book",bg="white", font=("monotype corsiva", 25, 'bold'),cursor="hand2",command=openbook,bd=0)
    labb.place(x=550, y=0)

    my_label1 = Label(classwork_label, image=my_image32, width=902, height=300, bg="black")
    my_label1.place(x=889,y=10000)

    #-------------------------------------------------------------------------------------------------------------------------

    lab14 = Label(base3, text="_" * 3000, font=("monotype corsiva", 10, 'bold'), bg="white", fg="black", bd=0)
    lab14.place(x=0, y=45)

    lab15 = Label(base3, text="_" * 110, font=("arial", 1), bg="#8f00ff", fg="black", bd=0)
    lab15.place(x=488, y=55)

    lab11 = Button(base3, text="Stream ", font=("monotype corsiva", 20, 'bold'), bg="white", fg="#8f00ff", width=7,cursor="hand2",bd=0, command=stream)
    lab11.place(x=488, y=0)

    lab12 = Button(base3, text="Class Work  ", font=("monotype corsiva", 20, 'bold'), bg="white", width=10,cursor="hand2",fg="#8f00ff", bd=0, command=classwork)
    lab12.place(x=600, y=0)

    lab13 = Button(base3, text="People ", font=("monotype corsiva", 20, 'bold'), bg="white", width=7, fg="#8f00ff",
                   bd=0, command=people,cursor="hand2")
    lab13.place(x=757, y=0)


    my_label0 = Label(base4, image=my_image21, width=902, height=300, bg="white")
    my_label0.place(x=240, y=0)
    my_label0 = Label(base4, image=my_image33, width=220, height=300, bg="white")
    my_label0.place(x=550, y=305)


def mpp():
    def stream():
        lab15.config(text="_" * 110)
        lab15.place(x=488, y=55)

        base4.place(x=0, y=80)
        base_people.place(x=-22222, y=9999)
        classwork_label.place(x=-87860, y=-99200)

    def classwork():
        classwork_label.place(x=0, y=200)

        my_label1.place(x=240, y=0)
        lab15.config(text="_" * 150)
        lab15.place(x=600, y=55)
        base4.place(x=-9300, y=500)
        base_people.place(x=-22222, y=9999)

    def people():
        lab15.config(text="_" * 100)
        lab15.place(x=757, y=55)

        base4.place(x=-9300, y=500)
        base_people.place(x=200, y=100)
        classwork_label.place(x=-9980, y=-98200)
        # bo.place(x=30, y=200)

    def getback():
        base3.destroy()

    base3 = LabelFrame(base, width=1365, height=675, bg="white", bd=0)
    base3.place(x=100, y=70)
    base4 = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)
    base4.place(x=0, y=80)
    l11 = Button(base3, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                 fg="black", command=getback, cursor="hand2", bd=0)
    l11.place(x=10, y=0)

    # ------------------------------------------------------people -----------------------------------------------------------
    people_list = ["Vasudev Raut","Keshav Jaiwal", "Prathmesh Rane","Pranav Sangave","Rahul Shinde","Chandrakant Shelke","Shubham Wyavhare"]

    base_people = LabelFrame(base3, height=670, width=1365, bg="white", bd=0)

    lab5 = Label(base_people, text="Teacher", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=0)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=40)

    lab6 = Label(base_people, text="Hivale Sir", font=("verdana", 10), bg="white", bd=0, fg="black")
    lab6.place(x=30, y=80)

    lab5 = Label(base_people, text="Classmates", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=120)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=160)

    bo = LabelFrame(base_people, height=110, width=100, bg="gray", bd=0)
    scroll = Scrollbar(bo)
    scroll.pack(side=RIGHT, fill=Y)
    ans = Listbox(bo, width=140, height=7, yscrollcommand=scroll.set, font=("verdana", 10), exportselection=0, bd=0)
    for i in people_list:
        ans.insert(END, i)
    scroll.config(command=ans.yview)
    ans.pack()
    bo.place(x=30, y=200)
    # -------------------------------------------------------------------------------------------------------------------------

    classwork_label = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)

    my_label1 = Label(classwork_label, image=my_image32, width=902, height=300, bg="white")
    my_label1.place(x=0, y=0)

    # -------------------------------------------------------------------------------------------------------------------------

    lab14 = Label(base3, text="_" * 3000, font=("monotype corsiva", 10, 'bold'), bg="white", fg="black", bd=0)
    lab14.place(x=0, y=45)

    lab15 = Label(base3, text="_" * 110, font=("arial", 1), bg="#8f00ff", fg="black", bd=0)
    lab15.place(x=488, y=55)

    lab11 = Button(base3, text="Stream ", font=("monotype corsiva", 20, 'bold'), bg="white", fg="#8f00ff", width=7,
                   cursor="hand2", bd=0, command=stream)
    lab11.place(x=488, y=0)

    lab12 = Button(base3, text="Class Work  ", font=("monotype corsiva", 20, 'bold'), bg="white", width=10,
                   cursor="hand2", fg="#8f00ff", bd=0, command=classwork)
    lab12.place(x=600, y=0)

    lab13 = Button(base3, text="People ", font=("monotype corsiva", 20, 'bold'), bg="white", width=7, fg="#8f00ff",
                   bd=0, command=people, cursor="hand2")
    lab13.place(x=757, y=0)

    my_label0 = Label(base4, image=my_image24, width=902, height=300, bg="white")
    my_label0.place(x=240, y=0)
    my_label0 = Label(base4, image=my_image33, width=220, height=300, bg="white")
    my_label0.place(x=550, y=305)


def ds():
    def stream():
        lab15.config(text="_" * 110)
        lab15.place(x=488, y=55)

        base4.place(x=0, y=80)
        base_people.place(x=-22222, y=9999)
        classwork_label.place(x=-87860, y=-99200)

    def classwork():
        classwork_label.place(x=0, y=200)

        my_label1.place(x=240, y=0)
        lab15.config(text="_" * 150)
        lab15.place(x=600, y=55)
        base4.place(x=-9300, y=500)
        base_people.place(x=-22222, y=9999)

    def people():
        lab15.config(text="_" * 100)
        lab15.place(x=757, y=55)

        base4.place(x=-9300, y=500)
        base_people.place(x=200, y=100)
        classwork_label.place(x=-9980, y=-98200)
        # bo.place(x=30, y=200)

    def getback():
        base3.destroy()

    base3 = LabelFrame(base, width=1365, height=675, bg="white", bd=0)
    base3.place(x=100, y=70)
    base4 = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)
    base4.place(x=0, y=80)
    l11 = Button(base3, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                 fg="black", command=getback, cursor="hand2", bd=0)
    l11.place(x=10, y=0)

    # ------------------------------------------------------people -----------------------------------------------------------
    people_list = ["Vasudev Raut", "Keshav Jaiwal", "Prathmesh Rane", "Pranav Sangave", "Rahul Shinde",
                   "Chandrakant Shelke", "Shubham Wyavhare"]
    base_people = LabelFrame(base3, height=670, width=1365, bg="white", bd=0)

    lab5 = Label(base_people, text="Teacher", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=0)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=40)

    lab6 = Label(base_people, text="Patil Sir", font=("verdana", 10), bg="white", bd=0, fg="black")
    lab6.place(x=30, y=80)

    lab5 = Label(base_people, text="Classmates", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=120)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=160)

    bo = LabelFrame(base_people, height=110, width=100, bg="gray", bd=0)
    scroll = Scrollbar(bo)
    scroll.pack(side=RIGHT, fill=Y)
    ans = Listbox(bo, width=140, height=7, yscrollcommand=scroll.set, font=("verdana", 10), exportselection=0, bd=0)
    for i in people_list:
        ans.insert(END, i)
    scroll.config(command=ans.yview)
    ans.pack()
    bo.place(x=30, y=200)
    # -------------------------------------------------------------------------------------------------------------------------

    classwork_label = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)

    my_label1 = Label(classwork_label, image=my_image32, width=902, height=300, bg="white")
    my_label1.place(x=0, y=0)

    # -------------------------------------------------------------------------------------------------------------------------

    lab14 = Label(base3, text="_" * 3000, font=("monotype corsiva", 10, 'bold'), bg="white", fg="black", bd=0)
    lab14.place(x=0, y=45)

    lab15 = Label(base3, text="_" * 110, font=("arial", 1), bg="#8f00ff", fg="black", bd=0)
    lab15.place(x=488, y=55)

    lab11 = Button(base3, text="Stream ", font=("monotype corsiva", 20, 'bold'), bg="white", fg="#8f00ff", width=7,
                   cursor="hand2", bd=0, command=stream)
    lab11.place(x=488, y=0)

    lab12 = Button(base3, text="Class Work  ", font=("monotype corsiva", 20, 'bold'), bg="white", width=10,
                   cursor="hand2", fg="#8f00ff", bd=0, command=classwork)
    lab12.place(x=600, y=0)

    lab13 = Button(base3, text="People ", font=("monotype corsiva", 20, 'bold'), bg="white", width=7, fg="#8f00ff",
                   bd=0, command=people, cursor="hand2")
    lab13.place(x=757, y=0)

    my_label0 = Label(base4, image=my_image25, width=902, height=300, bg="white")
    my_label0.place(x=240, y=0)
    my_label0 = Label(base4, image=my_image33, width=220, height=300, bg="white")
    my_label0.place(x=550, y=305)


def sdt():
    def stream():
        lab15.config(text="_" * 110)
        lab15.place(x=488, y=55)

        base4.place(x=0, y=80)
        base_people.place(x=-22222, y=9999)
        classwork_label.place(x=-87860, y=-99200)

    def classwork():
        classwork_label.place(x=0, y=200)

        my_label1.place(x=240, y=0)
        lab15.config(text="_" * 150)
        lab15.place(x=600, y=55)
        base4.place(x=-9300, y=500)
        base_people.place(x=-22222, y=9999)

    def people():
        lab15.config(text="_" * 100)
        lab15.place(x=757, y=55)

        base4.place(x=-9300, y=500)
        base_people.place(x=200, y=100)
        classwork_label.place(x=-9980, y=-98200)
        # bo.place(x=30, y=200)

    def getback():
        base3.destroy()

    base3 = LabelFrame(base, width=1365, height=675, bg="white", bd=0)
    base3.place(x=100, y=70)
    base4 = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)
    base4.place(x=0, y=80)
    l11 = Button(base3, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                 fg="black", command=getback, cursor="hand2", bd=0)
    l11.place(x=10, y=0)

    # ------------------------------------------------------people -----------------------------------------------------------
    people_list = ["Vasudev Raut", "Keshav Jaiwal", "Prathmesh Rane", "Pranav Sangave", "Rahul Shinde",
                   "Chandrakant Shelke", "Shubham Wyavhare"]
    base_people = LabelFrame(base3, height=670, width=1365, bg="white", bd=0)

    lab5 = Label(base_people, text="Teacher", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=0)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=40)

    lab6 = Label(base_people, text="Deshpande Mam", font=("verdana", 10), bg="white", bd=0, fg="black")
    lab6.place(x=30, y=80)

    lab5 = Label(base_people, text="Classmates", font=("verdana", 20), bg="white", fg="blue")
    lab5.place(x=0, y=120)

    lab5 = Label(base_people, text="_" * 130, font=("monotype corsiva", 10), bg="white", bd=0, fg="blue")
    lab5.place(x=0, y=160)

    bo = LabelFrame(base_people, height=110, width=100, bg="gray", bd=0)
    scroll = Scrollbar(bo)
    scroll.pack(side=RIGHT, fill=Y)
    ans = Listbox(bo, width=140, height=7, yscrollcommand=scroll.set, font=("verdana", 10), exportselection=0, bd=0)
    for i in people_list:
        ans.insert(END, i)
    scroll.config(command=ans.yview)
    ans.pack()
    bo.place(x=30, y=200)
    # -------------------------------------------------------------------------------------------------------------------------

    classwork_label = LabelFrame(base3, width=1365, height=675, bg="white", bd=0)

    my_label1 = Label(classwork_label, image=my_image32, width=902, height=300, bg="white")
    my_label1.place(x=0, y=0)

    # -------------------------------------------------------------------------------------------------------------------------

    lab14 = Label(base3, text="_" * 3000, font=("monotype corsiva", 10, 'bold'), bg="white", fg="black", bd=0)
    lab14.place(x=0, y=45)

    lab15 = Label(base3, text="_" * 110, font=("arial", 1), bg="#8f00ff", fg="black", bd=0)
    lab15.place(x=488, y=55)

    lab11 = Button(base3, text="Stream ", font=("monotype corsiva", 20, 'bold'), bg="white", fg="#8f00ff", width=7,
                   cursor="hand2", bd=0, command=stream)
    lab11.place(x=488, y=0)

    lab12 = Button(base3, text="Class Work  ", font=("monotype corsiva", 20, 'bold'), bg="white", width=10,
                   cursor="hand2", fg="#8f00ff", bd=0, command=classwork)
    lab12.place(x=600, y=0)

    lab13 = Button(base3, text="People ", font=("monotype corsiva", 20, 'bold'), bg="white", width=7, fg="#8f00ff",
                   bd=0, command=people, cursor="hand2")
    lab13.place(x=757, y=0)

    my_label0 = Label(base4, image=my_image26, width=902, height=300, bg="white")
    my_label0.place(x=240, y=0)
    my_label0 = Label(base4, image=my_image33, width=220, height=300, bg="white")
    my_label0.place(x=550, y=305)


def main_page():

    global f,mm
    #------------------------------------------------------------------main Page-------------------------------
    my_label0.place(x=100, y=70)  #main  page  label
    #------------------------------------------------------------------------------------------------------------

    #--------------------------------------notice box--------------------------------------------------

    lab3 = Label(base, text="Virtual Classroom", font=("monotype corsiva", 30, 'bold'), bg="#264c71",fg="white")
    lab3.place(x=680, y=80)

    lab4 = Label(base,text="Notice...", font=("monotype corsiva", 25),bg="white")
    lab4.place(x=180,y=180)

    lab5 = LabelFrame(base, bg="white",bd=0,width=370,height=105)
    lab5.place(x=160, y=220)

    lb=Label(lab5,text=".> Pay your Exam Fees",bg="white",bd=0, font=("monotype corsiva", 15))
    lb.place(x=20,y=10)

    lb1 = Label(lab5, text=".> Apply for Implant traning", bg="white", bd=0, font=("monotype corsiva", 15))
    lb1.place(x=20, y=40)

    lb2 = Label(lab5, text=".> ....", bg="white", bd=0, font=("monotype corsiva", 15))
    lb2.place(x=20, y=70)

    #----------------------------------------------
    lab6 = Label(base, text="Events...", font=("monotype corsiva", 25), bg="white")
    lab6.place(x=600, y=183)

    lab7 = LabelFrame(base, bg="white", width=370, bd=0, height=105)
    lab7.place(x=580, y=220)

    lb11 = Label(lab7, text=".> Enroll Implant Traning", bg="white", bd=0, font=("monotype corsiva", 15))
    lb11.place(x=20, y=10)

    lb111 = Label(lab7, text=".> Online Chess Touranament", bg="white", bd=0, font=("monotype corsiva", 15))
    lb111.place(x=20, y=40)

    lb211 = Label(lab7, text=".> ....", bg="white", bd=0, font=("monotype corsiva", 15))
    lb211.place(x=20, y=70)


    #-------------------------------------------------------------------------------------------------


    lab8 = LabelFrame(base, bg="white", width=340, height=120,bd=0)
    import calendar
    year = 2021
    month = 6
    calendar.month(year, month)

    te= Text(lab8,width=39,height=8,bd=0,fg="black")

    te.place(x=70,y=0)
    lab8.place(x=1025, y=190)
    te.insert(END,calendar.month(year,month))







    #------------------------------------------Class Section--------------------------------------------------------

    def clearbt():
        ls[0].place(x=44820, y=360)
        ls[1].place(x=92445, y=360)
        ls[2].place(x=144035, y=360)
        ls[3].place(x=114435, y=360)
        ls[4].place(x=144035, y=360)
        ls[5].place(x=114435, y=360)
        lsname[1].place(x=3953, y=2343)
        lsname[2].place(x=3453, y=2353)
        lsname[3].place(x=3453, y=2353)
        lsname[4].place(x=3353, y=2353)
        lsname[5].place(x=3453, y=2343)
        lsname[0].place(x=3453, y=2343)

    def leftshift():

        global f

        i = f

        if f <= 1:
            clearbt()
            ls[i + 1].place(x=920, y=430)
            ls[i + 2].place(x=1025, y=430)
            ls[i + 3].place(x=1135, y=430)
            ls[i + 4].place(x=1235, y=430)

            lsname[i + 1].place(x=915, y=490)
            lsname[i + 2].place(x=1020, y=490)
            lsname[i + 3].place(x=1130, y=490)
            lsname[i + 4].place(x=1230, y=490)

            f = f + 1

    def rightshift():

        global f


        i = f
        if f >= 1:
            clearbt()
            ls[i - 1].place(x=920, y=430)
            ls[i].place(x=1025, y=430)
            ls[i + 1].place(x=1135, y=430)
            ls[i + 2].place(x=1235, y=430)

            lsname[i - 1].place(x=915, y=490)
            lsname[i].place(x=1020, y=490)
            lsname[i + 1].place(x=1130, y=490)
            lsname[i + 2].place(x=1230, y=490)

            f = f - 1



    lab18 = Label(base, text="Your Classes", font=("monotype corsiva", 20), bg="white", fg="#8f00ff")
    lab18.place(x=870, y=370)

    bt2 = Button(base, text="<", font=("arial", 30), bd=0, height=1, bg="white", command=leftshift,cursor="hand2")
    bt2.place(x=830, y=430)

    bt3 = Button(base, text=">", font=("arial", 30), bd=0, height=1, bg="white", command=rightshift,cursor="hand2")
    bt3.place(x=1320, y=430)

    #classes buttons
    f = 1

    ls = ['java', 'python', 'ds', 'mpp', 'os', 'sdt']
    lsname = ['java1', 'python1', 'ds1', 'mpp1', 'os1', 'sdt1']
    ls[1] = Button(base, image=my_image1, width=50, height=55, bg="white", bd=0, command=py,cursor="hand2")
    ls[1].place(x=920, y=430)


    ls[2] = Button(base, image=my_image2, width=50, height=55, bg="white", bd=0, command=mpp,cursor="hand2")
    ls[2].place(x=1025, y=430)


    ls[3] = Button(base, image=my_image3, width=50, height=55, bg="white", bd=0, command=os,cursor="hand2")
    ls[3].place(x=1135, y=430)


    ls[4] = Button(base, image=my_image4, width=50, height=55, bg="white", bd=0, command=sdt,cursor="hand2")
    ls[4].place(x=1235, y=430)


    ls[0] = Button(base, image=my_image5, width=50, height=55, bg="white", bd=0, command=java,cursor="hand2")
    ls[0].place(x=1230, y=-32323)


    ls[5] = Button(base, image=my_image6, width=50, height=55, bg="white", bd=0, command=ds,cursor="hand2")
    ls[5].place(x=11430, y=-32360)
    # -----------------------------------------------------------------------------------------------
    lsname[1] = Button(base, text="Python", font=("arial bold", 12), bg="#c3c3fe", width=5, height=1, bd=0, command=py,cursor="hand2")
    lsname[1].place(x=915, y=490)

    lsname[2] = Button(base, text="MPP", font=("arial bold", 12), bg="#c3c3fe", width=5, height=1, bd=0, command=mpp,cursor="hand2")
    lsname[2].place(x=1020, y=490)

    lsname[3] = Button(base, text="OS", font=("arial bold", 12), bg="#c3c3fe", width=5, height=1, bd=0, command=os,cursor="hand2")
    lsname[3].place(x=1130, y=490)

    lsname[4] = Button(base, text="SDT", font=("arial bold", 12), bg="#c3c3fe", width=5, height=1, bd=0, command=sdt,cursor="hand2")
    lsname[4].place(x=1230, y=490)

    lsname[0] = Button(base, text="Java", font=("arial bold", 12), bg="#c3c3fe", width=5, height=1, bd=0, command=java,cursor="hand2")
    lsname[0].place(x=81880, y=490)

    lsname[5] = Button(base, text="DS", font=("arial bold", 12), bg="#c3c3fe", width=5, height=1, bd=0, command=ds,cursor="hand2")
    lsname[5].place(x=818880, y=490)



    #--------------------------------------Overall Score Section----------------------------------------------


    my_label77 = Label(base, image=my_image77, width=35, height=35, bg="white", bd=0)
    my_label77.place(x=270, y=375)

    lab6= Label(base,text="88", font=("arial", 35), bg="white", fg="Black")
    lab6.place(x=180,y=400)

    lab7 = Label(base, text="Overall Score", font=("monotype corsiva", 15), bg="white", fg="Black")
    lab7.place(x=180, y=470)

    #---------------------------------------------------------------------Quiz------------------------------------------------------------------------------
    def seeall():


        def getback():
            lf1.destroy()


        #-----------------------------------------------------------------------------------------------------------------------------------------------
        def python():
            global nn, QueList,OptList,OutList1,flag, Output
            Output=[]
            flag=0
            nn=0
            la2.config(bg="#f7f8fc",fg="black")
            la3.config(bg="#2f3245", fg="white")
            la4.config(bg="#2f3245", fg="white")
            la5.config(bg="#2f3245", fg="white")
            la6.config(bg="#2f3245", fg="white")
            la7.config(bg="#2f3245", fg="white")

            def setansoption1():
                global flag
                flag=1
                lf11.config(bg="#f7f8fc")
                lab12.config(bg="#f7f8fc")
                lab22.config(bg="#f7f8fc",fg="blue")
                lf12.config(bg="#ffffff")
                lab13.config(bg="#ffffff")
                lab23.config(bg="#ffffff",fg="black")
                lf13.config(bg="#ffffff")
                lab14.config(bg="#ffffff")
                lab24.config(bg="#ffffff",fg="black")
                lf14.config(bg="#ffffff")
                lab15.config(bg="#ffffff")
                lab25.config(bg="#ffffff", fg="black")


            def setansoption2():
                global flag
                flag=2
                lf12.config(bg="#f7f8fc")
                lab13.config(bg="#f7f8fc")
                lab23.config(bg="#f7f8fc", fg="blue")
                lf11.config(bg="#ffffff")
                lab12.config(bg="#ffffff")
                lab22.config(bg="#ffffff",fg="black")
                lf13.config(bg="#ffffff")
                lab14.config(bg="#ffffff")
                lab24.config(bg="#ffffff",fg="black")
                lf14.config(bg="#ffffff")
                lab15.config(bg="#ffffff")
                lab25.config(bg="#ffffff", fg="black")

            def setansoption3():
                global flag
                flag=3
                lf11.config(bg="#ffffff")
                lab12.config(bg="#ffffff")
                lab22.config(bg="#ffffff", fg="black")
                lf12.config(bg="#ffffff")
                lab13.config(bg="#ffffff")
                lab23.config(bg="#ffffff", fg="black")
                lf13.config(bg="#f7f8fc")
                lab14.config(bg="#f7f8fc")
                lab24.config(bg="#f7f8fc", fg="blue")
                lf14.config(bg="#ffffff")
                lab15.config(bg="#ffffff")
                lab25.config(bg="#ffffff", fg="black")

            def setansoption4():
                global flag
                flag=4
                lf11.config(bg="#ffffff")
                lab12.config(bg="#ffffff")
                lab22.config(bg="#ffffff", fg="black")
                lf12.config(bg="#ffffff")
                lab13.config(bg="#ffffff")
                lab23.config(bg="#ffffff", fg="black")
                lf13.config(bg="#ffffff")
                lab14.config(bg="#ffffff")
                lab24.config(bg="#ffffff", fg="black")
                lf14.config(bg="#f7f8fc")
                lab15.config(bg="#f7f8fc")
                lab25.config(bg="#f7f8fc", fg="blue")


            def next():
                global nn, QueList, OptList, OutList1, flag, Output
                def view_mark():
                    global nn, QueList, OptList, OutList1, flag, Output
                    lf11 = LabelFrame(lf1, width=885, height=540, bg="#f7f8fc")
                    lf11.place(x=232, y=100)
                    m=0
                    Output.append(flag)
                    marks=0
                    while m<5:

                        if OutList1[m]==Output[m]:
                            marks=marks+1
                        m=m+1
                    laa = Label(lf11,text="Thank you for submiting Quiz...", font=("monotype corsiva", 20),bg="white")
                    laa.place(x=100,y=100)

                    laa = Label(lf11, text="Your score : "+str(marks), font=("monotype corsiva", 20),bg="White")
                    laa.place(x=100, y=180)


                if flag !=0:

                    lf11.config(bg="#ffffff")
                    lab12.config(bg="#ffffff")
                    lab22.config(bg="#ffffff", fg="black")
                    lf12.config(bg="#ffffff")
                    lab13.config(bg="#ffffff")
                    lab23.config(bg="#ffffff", fg="black")
                    lf13.config(bg="#ffffff")
                    lab14.config(bg="#ffffff")
                    lab24.config(bg="#ffffff", fg="black")
                    lf14.config(bg="#ffffff")
                    lab15.config(bg="#ffffff")
                    lab25.config(bg="#ffffff", fg="black")
                    global nn, QueList,OptList,OutList1, Output
                    Output.append(flag)
                    flag=0


                    if nn<4:
                        nn=nn+1
                    else :
                        pass
                        #lab27.config(text="Submit",command=view_mark)

                    lab21.config(text=QueList[nn])
                    lab22.config(text=OptList[nn][0])
                    lab23.config(text=OptList[nn][1])
                    lab24.config(text=OptList[nn][2])
                    lab25.config(text=OptList[nn][3])

                    if nn<4:
                        pass
                    else:
                        lab27.config(text="Submit", command=view_mark)





            nn=0

            lf2=LabelFrame(lf1,width=885,height=540,bg="#f7f8fc")
            lf2.place(x=232,y=100)



            QueList = ["Who created Python ?", "When Python is released ?", "Which of the following is not a keyword ?",
                       "What is the answer to this expression, 22 % 3 is ?",'Python function return type']

            OptList = [["Guido van Rossum", "Bjarne Stroustrup", "James Gosling", "Tim Berners Lee"],
                       ["1992", "1991", "1990", "1994"], ["assert", "nonlocal", "pass", "eval"], ["5", "7", "1", "0"],['def','int','float','char']]

            OutList1 = [1, 2, 2, 3, 1]



            lab21 = Label(lf2, text=QueList[nn], bg="#f7f8fc",font=("arial",20))
            lab21.place(x=50, y=30)

            qn = Label(lf2, text="QUESTION 1", bg="#f7f8fc", font=("arial", 8),fg="#3aa8c7")
            qn.place(x=50, y=70)



            lf11 = Button(lf2, width=80, height=4, bg="#ffffff",bd=0,font=("arial",11),command=setansoption1)
            lf11.place(x=80, y=126)

            lab12 = Button(lf2, image=my_image27, width=50, height=50, bg="white", bd=0,command=setansoption1)
            lab12.place(x=90, y=140)

            lab22 = Button(lf2, text=OptList[nn][0], bg="#ffffff",font=("arial",10),bd=0,command=setansoption1)
            lab22.place(x=150, y=150)

            lf12 = Button(lf2, width=80, height=4, bg="#ffffff", bd=0,font=("arial",11),command=setansoption2)
            lf12.place(x=80, y=206)

            lab13 = Button(lf2, image=my_image28, width=50, height=50, bg="white", bd=0,command=setansoption2)
            lab13.place(x=90, y=220)

            lab23 = Button(lf2, text=OptList[nn][1],  bg="#ffffff",font=("arial",10),bd=0,command=setansoption2)
            lab23.place(x=150, y=230)

            lf13 = Button(lf2, width=80, height=4, bg="#ffffff", bd=0,font=("arial",11),command=setansoption3)
            lf13.place(x=80, y=286)

            lab14 = Button(lf2, image=my_image29, width=50, height=50, bg="white", bd=0,command=setansoption3)
            lab14.place(x=90, y=297)

            lab24 = Button(lf2, text=OptList[nn][2],  bg="#ffffff",font=("arial",10),bd=0,command=setansoption3)
            lab24.place(x=150, y=307)

            lf14 = Button(lf2, width=80, height=4, bg="#ffffff", bd=0,font=("arial",11),command=setansoption4)
            lf14.place(x=80, y=366)

            lab15 = Button(lf2, image=my_image30, width=50, height=50, bg="white", bd=0,command=setansoption4)
            lab15.place(x=90, y=377)

            lab25 = Button(lf2, text=OptList[nn][3], bg="#ffffff",font=("arial",10),bd=0,command=setansoption4)
            lab25.place(x=150, y=387)

            #lab26 = Button(lf2, text="Previous", bg="#3aa8c7", font=("arial", 15), bd=0,width=10,anchor="center",cursor="hand2",fg="white")
            #lab26.place(x=80, y=480)

            lab27 = Button(lf2, text="Next", bg="#3aa8c7", font=("arial", 15), bd=0,width=10,anchor="center",cursor="hand2",fg="white",command=next)
            lab27.place(x=690, y=480)

        #---------------------------------------------------------------------------------------------------------------------------------------------------------
        def java():
            la2.config(bg="#2f3245",fg="white")
            la3.config(bg="#f7f8fc",fg="black")
            la4.config(bg="#2f3245",fg="white")
            la5.config(bg="#2f3245",fg="white")
            la6.config(bg="#2f3245",fg="white")
            la7.config(bg="#2f3245",fg="white")

            lf11 = LabelFrame(lf1, width=885, height=540, bg="#f7f8fc")
            lf11.place(x=232, y=100)

            lab14 = Label(lf11, image=my_image34, width=885, height=540, bg="white", bd=0,)
            lab14.place(x=0, y=0)

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        def os():
            la2.config(bg="#2f3245", fg="white")
            la3.config(bg="#2f3245", fg="white")
            la4.config(bg="#f7f8fc", fg="black")
            la5.config(bg="#2f3245", fg="white")
            la6.config(bg="#2f3245", fg="white")
            la7.config(bg="#2f3245", fg="white")
            lf11 = LabelFrame(lf1, width=885, height=540, bg="#f7f8fc")
            lf11.place(x=232, y=100)

            lab14 = Label(lf11, image=my_image34, width=885, height=540, bg="white", bd=0, )
            lab14.place(x=0, y=0)
        #--------------------------------------------------------------------------------------------------------------------------------------------------
        def ds():
            la2.config(bg="#2f3245", fg="white")
            la3.config(bg="#2f3245", fg="white")
            la4.config(bg="#2f3245", fg="white")
            la5.config(bg="#f7f8fc", fg="black")
            la6.config(bg="#2f3245", fg="white")
            la7.config(bg="#2f3245", fg="white")
            lf11 = LabelFrame(lf1, width=885, height=540, bg="#f7f8fc")
            lf11.place(x=232, y=100)

            lab14 = Label(lf11, image=my_image34, width=885, height=540, bg="white", bd=0, )
            lab14.place(x=0, y=0)
        #--------------------------------------------------------------------------------------------------------------------------------------------------
        def sdt():
            la2.config(bg="#2f3245", fg="white")
            la3.config(bg="#2f3245", fg="white")
            la4.config(bg="#2f3245", fg="white")
            la5.config(bg="#2f3245", fg="white")
            la6.config(bg="#f7f8fc", fg="black")
            la7.config(bg="#2f3245", fg="white")
            lf11 = LabelFrame(lf1, width=885, height=540, bg="#f7f8fc")
            lf11.place(x=232, y=100)

            lab14 = Label(lf11, image=my_image34, width=885, height=540, bg="white", bd=0, )
            lab14.place(x=0, y=0)
        #--------------------------------------------------------------------------------------------------------------------------------------------------
        def mpp():
            la2.config(bg="#2f3245", fg="white")
            la3.config(bg="#2f3245", fg="white")
            la4.config(bg="#2f3245", fg="white")
            la5.config(bg="#2f3245", fg="white")
            la6.config(bg="#2f3245", fg="white")
            la7.config(bg="#f7f8fc", fg="black")
            lf11 = LabelFrame(lf1, width=885, height=540, bg="#f7f8fc")
            lf11.place(x=232, y=100)

            lab14 = Label(lf11, image=my_image34, width=885, height=540, bg="white", bd=0, )
            lab14.place(x=0, y=0)
        #--------------------------------------------------------------------------------------------------------------------------------------------------

        #--------------------------------------------------------------------------------------------------------------------------------------------------






        lf1 = LabelFrame(base, width=1355, height=675)
        lf1.place(x=100, y=70)

        lab11 = Label(lf1, image=my_image15, width=1360, height=675, bg="white", bd=5)
        lab11.place(x=0, y=0)

        l11 = Button(lf1, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                     fg="black", command=getback,cursor="hand2")
        l11.place(x=10, y=10)

        #la1 = Label(lf1, text="Quiz Section", font=("monotype corsiva", 40), bg="white", fg="Black")
        #la1.place(x=575, y=30)

        l11 = Label(lf1, image=my_image31,  width=880, height=540, bg="white",fg="black",)
        l11.place(x=232, y=75)


        la2 = Button(lf1, text="Python", font=("Arial", 20) , fg="white",bg="#2f3245",bd=2,width=10,anchor="center",command=python,activebackground="#f7f8fc")
        la2.place(x=35, y=160)


        la3 = Button(lf1, text="Java", font=("arial", 20), fg="white",bg="#2f3245",bd=2,width=10,anchor="center",command=java)
        la3.place(x=35, y=230)


        la4 = Button(lf1, text="OS", font=("arial", 20), fg="white",bg="#2f3245",bd=2,width=10,anchor="center",command=os)
        la4.place(x=35, y=300)

        la5 = Button(lf1, text="DS", font=("arial", 20), fg="white",bg="#2f3245",bd=2,width=10,anchor="center",command=ds)
        la5.place(x=35, y=370)

        la6 = Button(lf1, text="SDT", font=("arial", 20), fg="white",bg="#2f3245",bd=2,width=10,anchor="center",command=sdt)
        la6.place(x=35, y=440)

        la7 = Button(lf1, text="MPP", font=("arial", 20), fg="white",bg="#2f3245",bd=1,width=10,anchor="center",command=mpp)
        la7.place(x=35, y=510)





    lab8 = Label(base, text="Quiz Section", font=("monotype corsiva", 20), bg="white", fg="Black")
    lab8.place(x=175, y=525)

    lab8 = Label(base, text="Python", font=("monotype corsiva", 15), bg="white", fg="Black")
    lab8.place(x=175, y=565)

    bt5 = Button(base, image=my_image7, width=30, height=30, bg="white", bd=0)
    bt5.place(x=260, y=560)

    lab8 = Label(base, text="Java", font=("monotype corsiva", 15), bg="white", fg="Black")
    lab8.place(x=175, y=595)

    bt6 = Button(base, image=my_image8, width=30, height=30, bg="white", bd=0)
    bt6.place(x=260, y=595)

    lab8 = Label(base, text="OS", font=("monotype corsiva", 15), bg="white", fg="Black")
    lab8.place(x=175, y=625)


    bt7 = Button(base, image=my_image9, width=30, height=30, bg="white", bd=0)
    bt7.place(x=260, y=625)

    bt4 = Button(base, image=my_image78, width=155, height=35, bg="white", bd=0,command=seeall,cursor="hand2")
    bt4.place(x=160, y=660)



    # ----------------------------------------------------------chat bot-------------------------------------------------------------------------
    def Chat_bot():
        global ls, ls1, i, var, jj
        var = 0
        ls1 = []
        ls = []
        i = 0
        jj = 0
        bl = []

        def chatans(chat):

            def bot():
                le = len(ls1)
                n = le - 1

                j = 0
                while n >= 0:
                    ls1[j].place(x=300, y=560 - ((n + 1) * 70))
                    n = n - 1
                    j = j + 1

            global ls, ls1, i, var, jj
            chat1 = chat.lower()
            Hi = ['hii', 'hi', 'hey', 'hello']
            task = ['what is my today tasks', "today's work", "today's task", 'to do list', "what about today work",
                    "today task", 'today work']
            asw = ['show me my assigned work', 'assigned work', ]
            flag = 1

            for k in Hi:
                if chat1 == k:
                    bot()
                    ls1.append("Hello I'm here to resolve all your queries...")
                    flag = 2
                    base.update()
                    time.sleep(0.1)
                    ls1[jj] = Label(lf, text="hello I'm here to resolve all your queries.\nHow can I help you",
                                    font=("verdana", 12), anchor="w", width=40, height=2, bg="light Gray", fg="black")
                    ls1[jj].place(x=300, y=560)
                    jj = jj + 1

            for k in task:
                if chat1 == k:
                    bot()
                    ls1.append("You have to according to your calendar")
                    flag = 2
                    base.update()
                    time.sleep(0.1)
                    ls1[jj] = Label(lf, image=my_image19, font=("verdana", 12), anchor="w", width=200, height=50,
                                    bg="light Gray", fg="black")
                    ls1[jj].place(x=300, y=550)
                    jj = jj + 1

            for k in asw:
                if chat1 == k:
                    bot()
                    ls1.append("You have to according to your calendar")
                    flag = 2
                    base.update()
                    time.sleep(0.1)
                    ls1[jj] = Label(lf, image=my_image20, font=("verdana", 12), anchor="w", width=200, height=50,
                                    bg="light Gray", fg="black")
                    ls1[jj].place(x=300, y=550)
                    jj = jj + 1

            if flag == 1:
                bot()
                ls1.append("I didn't get that, Can you type that again...")
                flag = 2
                base.update()
                time.sleep(0.1)
                ls1[jj] = Label(lf, text="I didn't get that, Can you type that again...", font=("verdana", 12),
                                anchor="w", width=40, height=1, bg="light Gray", fg="black")
                ls1[jj].place(x=300, y=560)
                jj = jj + 1

        def insertchat():
            global ls, i, var
            chat = str(ent.get())
            if chat != "":

                le = len(ls)
                if le > 8:
                    ls.pop(0)
                    i = i - 1
                    var = var + 60

                le = len(ls)
                n = le - 1

                j = 0
                while n >= 0:
                    ls[j].place(x=780, y=530 - ((n + 1) * 70))
                    # bl[j].place(x=730, y=600 - ((n + 1) * 60))
                    n = n - 1
                    j = j + 1

                ls.append(chat)
                bl.append(1)

                # bl[i] = Label(base, image=my_image16, width=520, height=30, bg="black", bd=0)
                # bl[i].place(x=730, y=600)

                ls[i] = Label(lf, text=chat, font=("verdana", 12), width=30, height=1, anchor='e', bg="#55a0fd",
                              fg="black")
                ls[i].place(x=780, y=530)

                lab12 = Button(lf, image=my_image14, width=30, height=30, bg="white", bd=0)
                lab12.place(x=1100, y=525 + var)
                var = var - 70
                i = i + 1
                base.update()
                ent.delete(0, END)
                chatans(chat)

        def insertchat2(e):
            bb = e.keysym
            if bb == "Return":
                global ls, i, var
                chat = str(ent.get())
                if chat != "":

                    le = len(ls)
                    if le > 8:
                        ls.pop(0)
                        i = i - 1
                        var = var + 70

                    le = len(ls)
                    n = le - 1

                    j = 0
                    while n >= 0:
                        ls[j].place(x=780, y=530 - ((n + 1) * 70))
                        # bl[j].place(x=730, y=600 - ((n + 1) * 60))
                        n = n - 1
                        j = j + 1
                    base.update()

                    ls.append(chat)
                    bl.append(1)
                    # bl[i] = Label(base, image=my_image16, width=520, height=30, bg="black", bd=0)
                    # bl[i].place(x=730, y=600)

                    ls[i] = Label(lf, text=chat, font=("verdana", 12), width=30, height=1, anchor='e', bg="#55a0fd",
                                  fg="black")
                    ls[i].place(x=780, y=530)

                    lab12 = Button(lf, image=my_image14, width=30, height=30, bg="white", bd=0)
                    lab12.place(x=1100, y=525 + var)
                    var = var - 70
                    i = i + 1

                    ent.delete(0, END)
                    base.update()
                    chatans(chat)
                    base.update()

        def getback():
            lf.destroy()

        # ---------------------------------------------------
        lf = LabelFrame(base, width=1355, height=675)
        lf.place(x=100, y=70)

        lab11 = Button(lf, image=my_image12, width=1355, height=675, bg="white", bd=0)
        lab11.place(x=0, y=0)

        l11 = Button(lf, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                     fg="black", command=getback,cursor="hand2")
        l11.place(x=10, y=10)

        tex = Label(lf, width=92, height=27, bg="light gray", font=("monotype corsiva", 15))
        tex.place(x=238, y=0)

        tex3 = Label(lf,text="Chat Bot", fg="Black", font=("monotype corsiva", 25),bg="light gray")
        tex3.place(x=650, y=0)

        tex1 = Label(lf, width=92, height=2, bg="light gray", font=("monotype corsiva", 15))
        tex1.place(x=238, y=615)

        lab12 = Button(lf, image=my_image18, width=900, height=570, bg="white", bd=0)
        lab12.place(x=250, y=45)

        tex2 = Label(lf, width=57, height=1, bg="#efefef", font=("monotype corsiva", 20))
        tex2.place(x=257, y=623)

        def on_click(e):
            ent.configure(state=NORMAL)
            ent.delete(0,END)

        ent = Entry(lf, width=78, font=("verdana", 12), bg="#efefef", bd=0)
        ent.focus()
        ent.place(x=260, y=633)
        ent.bind("<Key>", insertchat2)
        ent.insert(0,"Enter your message here...")
        ent.configure(state=DISABLED)
        ent.bind("<Button-1>",on_click)



        lab21 = Button(lf, text="Send", font=("arial", 16), width=6, bg="#00ff00", cursor="hand2", command=insertchat)
        lab21.place(x=1065, y=622)

    lab10 = Button(base, image=my_image10, width=450, height=306, bg="white", bd=0,command=Chat_bot,cursor="hand2")
    lab10.place(x=347, y=376)

    #---------------------------------------chat bot end--------------------------------------------

    #-----------------------------------------------------graph----------------------------------------------------
    def show_graph():
        import matplotlib.pyplot as plt

        x = ["Python", "Java", "MPP", "OS", "DS", "SDT"]
        # h = [55,20,10,45,40,25]
        h = [45, 35, 30, 40, 45, 25]
        c = ["red", "green", "blue", "yellow", "cyan", "orange"]

        plt.bar(x, h, width=0.5, color=c,align="center")
        plt.xlabel("Courses")
        plt.ylabel("Scores")
        plt.title("Overall Performance")
        plt.show()


    la1=Button(base,image=my_image16,width=540,height=130,bg="white",bd=0,command=show_graph,cursor="hand2")
    la1.place(x=828,y=556)



    #-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------


def login():
    #main_page()

    con = sqlite3.connect("Classroom.db")
    ema=en.get()
    query = "select password from Studennt_info where email ='"+ema+"'"
    cur =con.cursor()
    cur.execute(query)
    data=(cur.fetchone())
    if data==None:
        en.delete(0, END)
        en2.delete(0,END)
        en.focus()
        lab0.configure(text="No Account Found!   ")
    else:


        con.execute(query)
        con.commit()
        passw=list(data)
        pas = str(en2.get())
        if passw[0]== pas:
            main_page()
        else:
            en2.delete(0, END)
            lab0.configure(text="Invalid Password!   ")
            



def register():

    def insertdata():



        con = sqlite3.connect("Classroom.db")
        em= en4.get()
        pa= str(en5.get())
        nam=str(en3.get())
        co =str(en5.get())
        query = "insert into Studennt_info (email,password,name,contact) values('" +em + "', '" +pa+ "', '" + nam+ "','" + co+ "')"

        con.execute(query)
        con.commit()





        con.close()
        labb.place(x=1100,y=500)

    def getback():
        labf1.destroy()

    base1 = Tk()
    base1.geometry("100x1")
    base1.geometry("+1+1")
    base1.overrideredirect(1)

    labf1 = LabelFrame(base, width=1355, height=650, bd=0, bg="white")
    labf1.place(x=100, y=70)
    # ------------------------------------------------------------------------------------
    lab1 = Label(labf1, text="Virtual", font=("monotype corsiva", 50, 'underline'), bg="white", fg="#8f00ff")
    lab1.place(x=60, y=170)
    lab1 = Label(labf1, text="Classroom", font=("monotype corsiva", 50, 'underline'), bg="white", fg="#8f00ff")
    lab1.place(x=200, y=270)

    lab2 = Label(labf1, text="Name :", font=("monotype corsiva", 15), bg="white")
    lab2.place(x=550, y=80)
    la = Label(labf1, text="________________________________________________", font=("monotype corsiva", 12), bg="white")
    la.place(x=550, y=120)

    en3 = Entry(labf1, bd=0, width=35, bg="white", font=("arial", 10))
    en3.place(x=555, y=115)

    lab3 = Label(labf1, text="Email :", font=("monotype corsiva", 15), bg="white")
    lab3.place(x=550, y=180)
    la = Label(labf1, text="________________________________________________", font=("monotype corsiva", 12), bg="white")
    la.place(x=550, y=220)
    en4 = Entry(labf1, bd=0, width=20, bg="white", font=("arial", 10))
    en4.place(x=555, y=215)

    lab3 = Label(labf1, text="Contact :", font=("monotype corsiva", 15), bg="white")
    lab3.place(x=550, y=280)
    la = Label(labf1, text="________________________________________________", font=("monotype corsiva", 12), bg="white")
    la.place(x=550, y=320)
    en5 = Entry(labf1, bd=0, width=20, bg="white", font=("arial", 10))
    en5.place(x=555, y=315)

    lab3 = Label(labf1, text="Password :", font=("monotype corsiva", 15), bg="white")
    lab3.place(x=550, y=370)
    la = Label(labf1, text="________________________________________________", font=("monotype corsiva", 12), bg="white")
    la.place(x=550, y=420)
    en5 = Entry(labf1, bd=0, width=20, bg="white", font=("arial", 10), show="*")
    en5.place(x=555, y=415)

    lab3 = Label(labf1, text="Confirm Password :", font=("monotype corsiva", 15), bg="white")
    lab3.place(x=550, y=480)
    la = Label(labf1, text="________________________________________________", font=("monotype corsiva", 12), bg="white")
    la.place(x=550, y=525)
    en5 = Entry(labf1, bd=0, width=20, bg="white", font=("arial", 10), show="*")
    en5.place(x=555, y=520)

    bt1 = Button(labf1, text="     Register   ", font=("calibri", 12), width=47, bg="black", fg="white", height=1,
                 cursor="hand2",command=insertdata)
    bt1.place(x=550, y=590)

    labb = Label(labf1, text="Resister Successfully...!!", font=("monotype corsiva", 20),bg="white",fg="green")

    l11 = Button(labf1, image=my_image17, font=("verdana", 12), anchor="w", width=40, height=40, bg="light Gray",
                 fg="black", command=getback, cursor="hand2",bd=0)
    l11.place(x=10, y=10)
    #------------------------------------------------------

    #---------------------------------------------------------------

    '''
    lab4 = Label(base, text="New to Virtual Classroom ? ", font=("monotype corsiva", 12), bg="white")
    lab4.place(x=750, y=590)

    lab4 = Button(base, text="Register", fg="blue", command=register, font=("monotype corsiva", 15, 'underline'),
                  bg="white", cursor="hand2", bd=0, activeforeground="Orange", activebackground="white")
    lab4.place(x=720, y=590)
    '''
    base1.mainloop()


base = Tk()

base.state('zoomed')
base.geometry("1525x790")
base.geometry("+1+1")
base.title("Classroom")
base.iconbitmap("Images/logo.ico")
base.configure(bg="#8F00FF")
# base.configure(bg="black")
Grid.rowconfigure(base,0,weight=1)
Grid.columnconfigure(base,0,weight=1)

my_image = ImageTk.PhotoImage(Image.open("Images/back1.jpg"))
my_label = Label(base, image=my_image, width=2500, height=1500, bg="white")
my_label.place(x=0, y=0)

labf = LabelFrame(base, width=390, height=650, bd=0, bg="white")
labf.place(x=100, y=70)

lab1 = Label(base, text="Virtual Classroom", font=("monotype corsiva", 30), bg="white", fg="#8f00ff")
lab1.place(x=160, y=160)

lab2 = Label(base, text="Email :", font=("monotype corsiva", 15), bg="white")
lab2.place(x=150, y=300)
la = Label(base, text="___________________________________", font=("monotype corsiva", 12), bg="white")
la.place(x=150, y=340)

en = Entry(base, bd=0, width=35, bg="white", font=("arial", 10))
en.place(x=155, y=335)

lab3 = Label(base, text="Password :", font=("monotype corsiva", 15), bg="white")
lab3.place(x=150, y=400)
la = Label(base, text="___________________________________", font=("monotype corsiva", 12), bg="white")
la.place(x=150, y=440)
en2 = Entry(base, bd=0, width=20, bg="white", font=("arial", 10), show="*")
en2.place(x=155, y=435)

bt1 = Button(base, text="     login   ", font=("calibri", 12), width=34, bg="black", fg="white", height=1,
             cursor="hand2", command=login)
bt1.place(x=150, y=520)

lab4 = Label(base, text="New to Virtual Classroom ? ", font=("monotype corsiva", 12), bg="white")
lab4.place(x=150, y=590)

lab4 = Button(base, text="Register", fg="blue", command=register, font=("monotype corsiva", 15, 'underline'),
              bg="white", cursor="hand2", bd=0, activeforeground="Orange", activebackground="white")
lab4.place(x=320, y=590)

lab0 = Label(base, text="         ", fg="red", font=("arial", 10),bg="white")
lab0.place(x=220, y=640)



my_image11 = ImageTk.PhotoImage(Image.open("Images/l.jpg"))
my_label11 = Label(base, image=my_image11, width=950, height=645, bg="white")
my_label11.place(x=500, y=71)

my_image0 = ImageTk.PhotoImage(Image.open("Images/b.png"))
my_label0 = Label(base, image=my_image0, width=1355, height=670, bg="white")

my_image1 = ImageTk.PhotoImage(Image.open("Images/pp3.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("Images/mpp.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("Images/os.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("Images/sdt.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("Images/java2.png"))
my_image6 = ImageTk.PhotoImage(Image.open("Images/da1.png"))
my_image77 = ImageTk.PhotoImage(Image.open("Images/emoji.jpg"))
my_image78 = ImageTk.PhotoImage(Image.open("Images/seeall.png"))
my_image7 = ImageTk.PhotoImage(Image.open("Images/s1.png"))
my_image8 = ImageTk.PhotoImage(Image.open("Images/s2.png"))
my_image9 = ImageTk.PhotoImage(Image.open("Images/s3.png"))
my_image10 = ImageTk.PhotoImage(Image.open("Images/cb.jpg"))
my_image12 = ImageTk.PhotoImage(Image.open("Images/cy2.png"))
my_image14 = ImageTk.PhotoImage(Image.open("Images/pp.png"))
my_image15 = ImageTk.PhotoImage(Image.open("Images/bl1.png"))

my_image16 = ImageTk.PhotoImage(Image.open("Images/graph1.jpeg"))
my_image17 = ImageTk.PhotoImage(Image.open("Images/bb.png"))
my_image18 = ImageTk.PhotoImage(Image.open("Images/bi.jpg"))
my_image19 = ImageTk.PhotoImage(Image.open("Images/cbb1.png"))
my_image20 = ImageTk.PhotoImage(Image.open("Images/cbb2.jpeg"))
#----------------------------------------------------------------------
my_image21 = ImageTk.PhotoImage(Image.open("Images/py1.jpg"))
my_image22 = ImageTk.PhotoImage(Image.open("Images/os2.jpg"))
my_image23 = ImageTk.PhotoImage(Image.open("Images/java3.png"))
my_image24 = ImageTk.PhotoImage(Image.open("Images/mp.jpg"))
my_image25 = ImageTk.PhotoImage(Image.open("Images/dsa.png"))
my_image26 = ImageTk.PhotoImage(Image.open("Images/sdt2.jpg"))

#------------------------------------------------------------------
my_image27 = ImageTk.PhotoImage(Image.open("Images/A.png"))
my_image28 = ImageTk.PhotoImage(Image.open("Images/B ans.png"))
my_image29 = ImageTk.PhotoImage(Image.open("Images/C.png"))
my_image30 = ImageTk.PhotoImage(Image.open("Images/D.png"))
my_image31 = ImageTk.PhotoImage(Image.open("Images/qbc.jpg"))
#--------------------------------------------------------------

my_image32 = ImageTk.PhotoImage(Image.open("Images/xyz.png"))
my_image33 = ImageTk.PhotoImage(Image.open("Images/nas.png"))
my_image34 = ImageTk.PhotoImage(Image.open("Images/nqt.jpeg"))

base.mainloop()

