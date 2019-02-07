#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:23:54 2018

@author: TEAM 3
"""

#PACKAGE INFORMATION TO HELP RUN THE PROGRAM
from tkinter import *
import sqlite3 as sq
from tkinter import messagebox as msg
from tkinter import ttk
import datetime 
import time



root=Tk() #TO CREATE AND PASS WINDOW TO A FEW PARAMETERS
root.geometry('400x450') #DEFINE WINDOW SIZE
root.title('Welcome to Tax-Aid') #SIMPLE TITLE ON TOP



txt_F_Name = StringVar()      #HOLDS STRING FIRST ANME
txt_L_Name = StringVar()      #HOLDS STRING LAST NAME
txt_Volunteer = StringVar()   #HOLDS STRING VOLUNTEER
txt_Email = StringVar()       #HOLDS STRING EMAIL
txt_Email_Two = StringVar()   #HOLDS STRING EMAIL
txt_Affiliation = StringVar() #HOLDS THE AFFILIATION




menu = Menu(root)
root.config(menu = menu)



""" START OF THE LABEL INFORMATION AND DESIGN OF THE LAYOUT """



f_lab =Label(root,text='First Name: ',font=('none 12 bold'))
f_lab.place(x=70,y=0)

ent_f_name = Entry(root, width=20, font=('none 12 bold'), textvar = txt_F_Name)
ent_f_name.place(x=160, y=0)



l_lab =Label(root,text='Last Name: ',font=('none 12 bold'))
l_lab.place(x=70,y=40)

ent_l_name = Entry(root, width = 20, font = ('none 12 bold'), textvar = txt_L_Name)
ent_l_name.place(x = 160 , y = 40)



v_lab =Label(root,text='Volunteer Role: ',font=('none 12 bold'))
v_lab.place(x=45, y=80)



e_lab =Label(root,text='Email: ',font=('none 12 bold'))
e_lab.place(x=100, y=120)

ent_e = Entry (root, width = 20, font = ('none 12 bold'), textvar = txt_Email)
ent_e.place(x= 160, y = 120) 

htext = Label(root,text='(Use permanent email address helps us stay in touch with you)',font=('none 11 bold'))
htext.place(x=20,y=150)


e_lab =Label(root,text='Re-Enter-Email: ',font=('none 12 bold'))
e_lab.place(x=40, y=180)

ent_e = Entry (root, width = 20, font = ('none 12 bold'), textvar =txt_Email_Two )
ent_e.place(x= 160, y = 180)



a_lab = Label(root, text='Employer/Affiliation:', font=('none 12 bold'))
a_lab.place(x=12, y = 220)

ent_a_name = Entry (root, width = 20, font = ('none 12 bold'), textvar = txt_Affiliation)
ent_a_name.place(x= 160, y = 220)



""" END OF LABEL INFORMATION AND DESIGN OF THE LAYOUT """



#COMBOBOX FOR INFO
userAge = StringVar()
userAgeBox = ttk.Combobox(root, width = 8, textvariable = userAge, state='readonly')
userAgeBox.grid(row = 1, column = 1)
userAgeBox['values'] = tuple(['Greeter', 'Tax Preparer', 'Printer', 'Interviewer', 'Site Manager', 'Translator', 'Tax Expert', 'Not Sure'])
userAgeBox.current(0)
userAgeBox.place(x= 160, y=80)



db = sq.connect('taxprogram.db') 
point = db.cursor() 
point.execute("CREATE TABLE IF NOT EXISTS people(First_Name TEXT, Last_Name TEXT, Volunteer TEXT, Email TEXT, Employer_Affiliation TEXT, Date TEXT)")
db.commit()



#START OF THE FUNCTIONS
def add():
    name1 = txt_F_Name.get()
    name2 = txt_L_Name.get()
    nameVol = userAge.get()
    nameEm = txt_Email.get()
    nameAff = txt_Affiliation.get()
    
 
#datetime.datetime.now()
    conct = sq.connect('taxprogram.db')
    with conct:
        point = conct.cursor()
        point.execute('INSERT INTO people(First_Name,Last_Name, Volunteer, Email, Employer_Affiliation,Date) VALUES (?,?,?,?,?,?)', (name1,name2,nameVol,nameEm,nameAff,time.strftime('%m-%d-%Y %I:%M:%S %p')))
        db.close()
        txt_F_Name.set('')
        txt_L_Name.set('')
        userAge.set('')
        txt_Email.set('')
        txt_Email_Two.set('')
        txt_Affiliation.set('')
        chk_info.set(0)
        

    
#FUNCTION TO CHECK THE INFO
def cln_info():
    each_part()
    
    
    
#ANOTHER FUNCTION
def uf_part():
    if (txt_Email.get() == txt_Email_Two.get()):
        cln_info()
    else:
        msg.showinfo("Email Requirements", "You need to double check your email.")
    
    
    
#FUNCTION TO CHECK BOX
def each_part():
    if chk_info.get():
        show_msg()
    else:
        msg.showinfo("Alert from Tax-Aid", "You need to check the box and accept the terms and conditions.")
        


#FUNCTION FOR INFO
def show_msg():
    answer = msg.askquestion("Tax-Aid", "I understand that as serving as a volunteer for Tax-Aid, a 501c3 nonprofit public charity, I am an important and designated representative of Tax-Aid, and I agree to work with Tax-Aid in achieving its mission. I agree to perform my volunteer duties professionally and in accordance with this Agreement and the guidelines as set out in the Volunteer Handbook and Reference Manual. The full contents and text of the Handbook is available on the Tax-Aid web site, www.tax-aid.org/tax-volunteers.\n\n I understand that during the course serving as a volunteer, confidential information may be made available to me. I understand that confidential information must not be released outside the Tax-Aid organization. I understand that I only share confidential information inside the Tax-Aid organization when it is relevant to the preparation of a tax return for a Tax-Aid client. I will not knowingly prepare a false return. I will not solicit business from taxpayers or use knowledge gained from Tax-Aid for any direct or indirect purposes.\n\nI will not engage in criminal, infamous, dishonest, notoriously disgraceful conduct or any conduct deemed to have a negative effect on Tax-Aid. I will treat all taxpayers in a professional, courteous and respectful manner\n\nI hereby release Tax-Aid, its officers, directors, employees, and agents from any claims, lawsuits, or actions I, my heirs, or legal representatives may have for any personal injury and/or property damage I may incur as a result of my volunteer services.")
    if answer == 'yes':
        add() 
        final_one()
        
    else:
        txt_F_Name.set('')
        txt_L_Name.set('')
        userAge.set('')
        txt_Email.set('')
        txt_Email_Two.set('')
        txt_Affiliation.set('')
        chk_info.set(0)
      
        
        
#FINAL MESSAGE
def final_one():
    msg.showinfo("Thank You and Welcome", "Thank you for registering! Please see a site manager for next steps.")

    

#THE CHECK BOX DISPLAY
chk_info = IntVar()
chk_btn = Checkbutton(root, text="Tax-Aid Requires Volunteers to Sign a waiver", onvalue=1, offvalue=0, variable=chk_info)
chk_btn.place(x= 40, y= 310)      



#BUTTON INFORMATION
btn_add = Button(root, padx=5, pady=5, text='Submit', command=uf_part, font= ('none 12 bold'))
btn_add.place(x= 160, y= 350)
btn_add.config(relief='raised')



root.mainloop() #ALLOWS TO KEEP WINDOW !!DO NOT ERASE!!




"""END OF THE PROGRAM  """