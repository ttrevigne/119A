# ----------------------------------------------------------------------
# Name:     Tax-Aid Volunteer Form (Generation 2)
# Purpose:  Local database for volunteer information
#
# Date:     2/7/19
# ----------------------------------------------------------------------
"""
Created on Mon Dec  3 14:23:54 2018

@author: TEAM 3
"""
from tkinter import *
import sqlite3 as sq
from tkinter import messagebox as msg
from tkinter import ttk
import datetime 
import time


class TaxAidApp:
    """
    Implements GUI & GUI functionality for the Tax-Aid sign-in program
    """
    root = Tk()  # Creates a window that is populated below
    first_name = StringVar()  # HOLDS STRING FIRST NAME
    last_name = StringVar()  # HOLDS STRING LAST NAME
    email = StringVar()  # HOLDS STRING EMAIL
    email_two = StringVar()  # HOLDS STRING EMAIL
    affiliation = StringVar()  # HOLDS THE AFFILIATION
    user_role = StringVar()  # HOLDS THE USER ROLE
    chk_info = IntVar()

    def __init__(self, master):
        """
        Function that initializes a TaxAid object that contains the
        attributes for the graphical user interface
        :param master: (tkinter.Tk) tkinter object that initializes GUI
        """

        self.master = master
        master.title("Tax-Aid Volunteer Sign-in")

        # Creates a label "First Name" & entry box for input
        self.f_lab = Label(master, text='First Name: ', font='none 12 bold')
        # f_lab.place(x=70, y=0)
        self.f_lab.pack()
        self.ent_f_name = Entry(master, width=20, font='none 12 bold',
                                textvariable=TaxAidApp.first_name)
        self.ent_f_name.place(x=160, y=0)

        # Creates label "Last Name" & entry box for input
        self.l_lab = Label(master, text='Last Name: ', font='none 12 bold')
        # self.l_lab.place(x=70, y=40)
        self.l_lab.pack()
        self.ent_l_name = Entry(master, width=20, font='none 12 bold',
                                textvariable=TaxAidApp.last_name)
        # self.ent_l_name.place(x=160, y=40)
        self.ent_l_name.pack()

        # Creates label "Volunteer Role" & drop down menu with choices
        self.v_lab = Label(master, text='Volunteer Role: ',
                           font='none 12 bold')
        # v_lab.place(x=45, y=80)
        self.v_lab.pack()
        self.user_role_box = ttk.Combobox(master, width=8,
                                          textvar=TaxAidApp.user_role,
                                          state='readonly')
        # self.user_age_box.grid(row=1, column=1)
        self.user_role_box['values'] = ['Greeter', 'Tax Preparer', 'Printer',
                                        'Interviewer', 'Site Manager',
                                        'Translator',
                                        'Tax Expert', 'Not Sure']
        self.user_role_box.current(0)
        # self.user_age_box.place(x=160, y=80)
        self.user_role_box.pack()

        # Creates label "Email" & entry box for email
        self.e_lab = Label(master, text='Email: ', font='none 12 bold')
        # self.e_lab.place(x=100, y=120)
        self.e_lab.pack()
        self.ent_email = Entry(master, width=20, font='none 12 bold',
                               textvariable=TaxAidApp.email)
        # self.ent_e.place(x=160, y=120)
        self.ent_email.pack()
        self.e_lab = Label(master, text='Re-Enter-Email:', font='none 12 bold')
        # self.e_lab.place(x=40, y=180)
        self.e_lab.pack()
        self.ent_email = Entry(master, width=20, font='none 12 bold',
                               textvariable=TaxAidApp.email_two)
        # self.ent_e.place(x=160, y=180)
        self.ent_email.pack()

        # Creates label "Employer/Affiliation" & entry box
        self.a_lab = Label(master, text='Employer/Affiliation:',
                           font='none 12 bold')
        self.a_lab.place(x=12, y=220)
        self.a_lab.pack()
        self.ent_affiliation = Entry(master, width=20, font='none 12 bold',
                                     textvariable=TaxAidApp.affiliation)
        # self.ent_a_name.place(x=160, y=220)
        self.ent_affiliation.pack()

        # Creates "Submit" button
        self.submit = Button(master, padx=5, pady=5, text='Submit',
                             font='none 12 bold')
        # self.btn_add.place(x=160, y=350)
        self.submit.pack()
        self.submit.config(relief='raised')

        # Creates "Clear" button
        self.clear = Button(master, padx=5, pady=5, text='Clear',
                            font='none 12 bold')
        self.clear.pack()
        self.clear.config(relief='raised')

        # Creates "Exit" button
        self.exit = Button(master, padx=5, pady=5, text='Exit',
                           font='none 12 bold')
        self.exit.pack()
        self.exit.config(relief='raised')

        # Creates check box for waiver
        self.chk_btn = Checkbutton(master, text='''Tax-Aid Requires Volunteers 
                                   to Sign a waiver''', onvalue=1, offvalue=0,
                                   variable=TaxAidApp.chk_info)
        # chk_btn.place(x=40, y=310)
        self.chk_btn.pack()

    @staticmethod
    def add():
        """
        Adds the information given by the volunteer to the database
        :return: None
        """
        first_name = TaxAidApp.first_name.get()
        last_name = TaxAidApp.last_name.get()
        role = TaxAidApp.user_role.get()
        email = TaxAidApp.email.get()
        affiliation = TaxAidApp.affiliation.get()

        datetime.datetime.now()
        connect = sq.connect('volunteers.db')
        with connect:
            point = connect.cursor()
            point.execute(
                '''INSERT INTO people(First_Name,Last_Name, Volunteer, Email, 
                Employer_Affiliation,Date) VALUES (?,?,?,?,?,?)''',
                (first_name, last_name, role, email, affiliation,
                 time.strftime('%m-%d-%Y %I:%M:%S %p')))
            db.close()
            TaxAidApp.first_name.set('')
            TaxAidApp.last_name.set('')
            TaxAidApp.user_role.set('')
            TaxAidApp.email.set('')
            TaxAidApp.email_two.set('')
            TaxAidApp.affiliation.set('')
            TaxAidApp.chk_info.set(0)

    @staticmethod
    def validate_email():
        """
        Verifies that the two emails entered are the same
        :return: None
        """
        if TaxAidApp.email.get() == TaxAidApp.email_two.get():
            TaxAidApp.validate_check()
        else:
            msg.showinfo("Email Requirements",
                         "Please verify you entered the same email.")

    @staticmethod
    def validate_check():
        """
        Verifies that the check box has been checked
        :return: None
        """
        if TaxAidApp.chk_info.get():
            TaxAidApp.show_msg()
        else:
            msg.showinfo("Alert from Tax-Aid",
                         '''Please accept the terms and conditions to 
                         continue.''')

    @staticmethod
    def show_msg():
        """
        Function that displays Tax-Aid terms & conditions/Thank you message
        :return: None
        """
        answer = msg.askquestion("Tax-Aid",
                                 '''I understand that as serving as a volunteer
                                  for Tax-Aid, a 501c3 nonprofit public charity
                                  , I am an important and designated 
                                  representative of Tax-Aid, and I agree to 
                                  work with Tax-Aid in achieving its mission. 
                                  I agree to perform my volunteer duties 
                                  professionally and in accordance with this 
                                  Agreement and the guidelines as set out in 
                                  the Volunteer Handbook and Reference Manual. 
                                  The full contents and text of the Handbook is
                                   available on the Tax-Aid web site, 
                                   www.tax-aid.org/tax-volunteers.\n\n I 
                                   understand that during the course serving 
                                   as a volunteer, confidential information may
                                    be made available to me. I understand that 
                                    confidential information must not be 
                                    released outside the Tax-Aid organization. 
                                    I understand that I only share confidential
                                     information inside the Tax-Aid 
                                     organization when it is relevant to the 
                                     preparation of a tax return for a Tax-Aid 
                                     client. I will not knowingly prepare a 
                                     false return. I will not solicit business 
                                     from taxpayers or use knowledge gained 
                                     from Tax-Aid for any direct or indirect 
                                     purposes.\n\nI will not engage in 
                                     criminal, infamous, dishonest, notoriously
                                      disgraceful conduct or any conduct deemed
                                       to have a negative effect on Tax-Aid. 
                                       I will treat all taxpayers in a 
                                       professional, courteous and respectful 
                                       manner\n\nI hereby release Tax-Aid, its 
                                       officers, directors, employees, and 
                                       agents from any claims, lawsuits, or 
                                       actions I, my heirs, or legal 
                                       representatives may have for any 
                                       personal injury and/or property damage 
                                       I may incur as a result of my volunteer 
                                       services.''')
        if answer == 'yes':
            TaxAidApp.add()
            msg.showinfo("Thank You and Welcome",
                         '''Thank you for registering! Please see a site 
                         manager for next steps.''')
        else:
            return


db = sq.connect('volunteers.db')
point = db.cursor()
point.execute('''CREATE TABLE IF NOT EXISTS volunteers(First_Name TEXT, 
             Last_Name TEXT, Volunteer TEXT, Email TEXT, 
             Employer_Affiliation TEXT, Date TEXT)''')
db.commit()


tax_aid = TaxAidApp(TaxAidApp.root)
tax_aid.root.mainloop()
