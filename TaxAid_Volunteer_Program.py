# ----------------------------------------------------------------------
# Name:     Tax-Aid Volunteer Form (Generation 2)
# Purpose:  Local database for volunteer information
#
# Date:     2/7/19
# ----------------------------------------------------------------------

from tkinter import *
from tkinter import PhotoImage
import sqlite3 as sq
from tkinter import messagebox as msg
from tkinter import ttk
import datetime
import time
import string


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
    DB = sq.connect('volunteers.db')

    def __init__(self, master):
        """
        Function that initializes a TaxAid object that contains the
        attributes for the graphical user interface
        :param master: (tkinter.Tk) tkinter object that initializes GUI
        """
        # Creates master window & defines size
        master = master
        master.title("Tax-Aid Volunteer Sign-in")
        w = TaxAidApp.root.winfo_screenwidth()
        h = TaxAidApp.root.winfo_screenheight()
        TaxAidApp.root.geometry("%dx%d+0+0" % (w, h))
        TaxAidApp.root.resizable(False, False)
        TaxAidApp.root.configure(background='white')

        # Creates label containing Tax-Aid logo
        image = PhotoImage(file="tax-aid-logo.gif")
        self.logo = Label(image=image)
        self.logo.image = image
        self.logo.configure(background='white')
        self.logo.pack(side=LEFT)

        # Creation of registration label
        self.registration = Label(master, text='Registration',
                                  font='none 12 bold', background='white')
        self.registration.place(relx=0.51, rely=0.05, anchor=CENTER)

        # Creates a label "First Name" & entry box for input
        self.f_lab = Label(master, text='First Name: ', font='none 12 bold',
                           background='white')
        self.f_lab.place(relx=0.43, rely=0.1, anchor=CENTER)
        self.ent_f_name = Entry(master, width=20, font='none 12 bold',
                                textvariable=TaxAidApp.first_name,
                                background='gainsboro')
        self.ent_f_name.place(relx=0.56, rely=0.1, anchor=CENTER)

        # Creates label "Last Name" & entry box for input
        self.l_lab = Label(master, text='Last Name: ', font='none 12 bold',
                           background='white')
        self.l_lab.place(relx=0.43, rely=0.2, anchor=CENTER)
        self.ent_l_name = Entry(master, width=20, font='none 12 bold',
                                textvariable=TaxAidApp.last_name,
                                background='gainsboro')
        self.ent_l_name.place(relx=0.56, rely=0.2, anchor=CENTER)

        # Creates label "Volunteer Role" & drop down menu with choices
        self.v_lab = Label(master, text='Volunteer Role: ',
                           font='none 12 bold', background='white')
        self.v_lab.place(relx=0.43, rely=0.3, anchor=CENTER)
        self.user_role_box = ttk.Combobox(master, width=15,
                                          textvar=TaxAidApp.user_role,
                                          state='readonly')
        self.user_role_box['values'] = ['Greeter', 'Tax Preparer', 'Printer',
                                        'Interviewer', 'Site Manager',
                                        'Translator',
                                        'Tax Expert', 'Not Sure']
        self.user_role_box.current(0)
        self.user_role_box.place(relx=0.56, rely=0.3, anchor=CENTER)

        # Creates label "Email" & entry box for email
        self.e_lab = Label(master, text='Email: ', font='none 12 bold',
                           background='white')
        self.e_lab.place(relx=0.43, rely=0.4, anchor=CENTER)
        self.ent_email = Entry(master, width=20, font='none 12 bold',
                               textvariable=TaxAidApp.email,
                               background='gainsboro')
        self.ent_email.place(relx=0.56, rely=0.4, anchor=CENTER)
        self.e_lab = Label(master, text='Re-Enter-Email:', font='none 12 bold',
                           background='white')
        self.e_lab.place(relx=0.43, rely=0.5, anchor=CENTER)
        self.ent_email_two = Entry(master, width=20, font='none 12 bold',
                                   textvariable=TaxAidApp.email_two,
                                   background='gainsboro')
        self.ent_email_two.place(relx=0.56, rely=0.5, anchor=CENTER)

        # Creates label "Employer/Affiliation" & entry box
        self.a_lab = Label(master, text='Employer/Affiliation:',
                           font='none 12 bold', background='white')
        self.a_lab.place(relx=0.43, rely=0.6, anchor=CENTER)
        self.ent_affiliation = Entry(master, width=20, font='none 12 bold',
                                     textvariable=TaxAidApp.affiliation,
                                     background='gainsboro')
        self.ent_affiliation.place(relx=0.56, rely=0.6, anchor=CENTER)

        # Creates check box for waiver
        self.chk_btn = Checkbutton(master, text='''Tax-Aid requires volunteers 
                                          \nto sign a waiver''', onvalue=1,
                                   offvalue=0, variable=TaxAidApp.chk_info,
                                   background='white', font='non 10 bold')
        self.chk_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Creates "Exit" button
        self.exit = Button(master, padx=5, pady=5, text='Exit',
                           font='none 12 bold', command=self.close)
        self.exit.place(relx=0.6, rely=0.8, anchor=CENTER)
        self.exit.config(relief='raised')

        # Creates "Clear" button
        self.clear = Button(master, padx=5, pady=5, text='Clear',
                            font='none 12 bold',
                            command=self.clear)
        self.clear.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.clear.config(relief='raised')

        # Creates "Submit" button
        self.submit = Button(master, padx=5, pady=5, text='Submit',
                             font='none 12 bold',
                             command=self.complete_validation)
        self.submit.place(relx=0.4, rely=0.8, anchor=CENTER)
        self.submit.config(relief='raised')

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
                '''INSERT INTO volunteers(First_Name,Last_Name, Volunteer,
                Email, Employer_Affiliation,Date) VALUES (?,?,?,?,?,?)''',
                (first_name, last_name, role, email, affiliation,
                 time.strftime('%m-%d-%Y %I:%M:%S %p')))
            TaxAidApp.DB.commit()
            TaxAidApp.DB.close()
            TaxAidApp.first_name.set('')
            TaxAidApp.last_name.set('')
            TaxAidApp.user_role.set('')
            TaxAidApp.email.set('')
            TaxAidApp.email_two.set('')
            TaxAidApp.affiliation.set('')
            TaxAidApp.chk_info.set(0)

    @staticmethod
    def validate_name():
        """
        Validates that the name provided consists of only letters
        :return: (Boolean) whether the input provided consists of only letters
        """
        if not TaxAidApp.first_name.get() or not TaxAidApp.last_name.get():
            msg.showinfo("Name Requirements", "Please enter name")
            return False
        alphabet = string.ascii_lowercase
        for char in TaxAidApp.first_name.get().lower():
            if char not in alphabet:
                msg.showinfo("Name Requirements", '''Please only use characters
                A-Z''')
                return False
        for char in TaxAidApp.last_name.get().lower():
            if char not in alphabet:
                msg.showinfo("Name Requirements", '''Please only use characters
                A-Z''')
                return False
        return True

    @staticmethod
    def validate_email():
        """
        Verifies that the two emails entered are the same
        :return: None
        """
        if "@" and "." not in TaxAidApp.email.get():
            msg.showinfo("Email Requirements", "Please enter valid email")
            return
        else:
            if TaxAidApp.email.get() == TaxAidApp.email_two.get():
                TaxAidApp.validate_check()
            else:
                msg.showinfo("Email Requirements",
                             "Please verify you entered the same email.")
                return

    @staticmethod
    def complete_validation():
        if TaxAidApp.validate_name():
            TaxAidApp.validate_email()

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
    def close():
        """
        Function that closes the root window and stops the program
        :return: None
        """
        TaxAidApp.root.destroy()

    def clear(self):
        """
        Clears all fields and boxes with exception of the combobox
        :return: None
        """
        self.ent_f_name.delete(0, END)
        self.ent_l_name.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_email_two.delete(0, END)
        self.ent_affiliation.delete(0, END)
        TaxAidApp.chk_info.set(0)

    @staticmethod
    def show_msg():
        """
        Function that displays Tax-Aid terms & conditions/Thank you message
        :return: None
        """
        answer = msg.askquestion("Tax-Aid", "I understand that as serving as a\
                                volunteer for Tax-Aid, a 501c3 nonprofit \
                                public charity, I am an important and \
                                designated representative of Tax-Aid, and I \
                                agree to work with Tax-Aid in achieving its \
                                mission. I agree to perform my volunteer \
                                duties professionally and in accordance with \
                                this Agreement and the guidelines as set out \
                                in the Volunteer Handbook and Reference \
                                Manual. The full contents and text of the \
                                Handbook is available on the Tax-Aid web site,\
                                 www.tax-aid.org/tax-volunteers.\n\n I \
                                 understand that during the course serving as \
                                 a volunteer, confidential information may be \
                                 made available to me. I understand that \
                                 confidential information must not be released\
                                  outside the Tax-Aid organization. I \
                                  understand that I only share confidential \
                                  information inside the Tax-Aid organization \
                                  when it is relevant to the preparation of a \
                                  tax return for a Tax-Aid client. I will not \
                                  knowingly prepare a false return. I will \
                                  not solicit business from taxpayers or use \
                                  knowledge gained from Tax-Aid for any \
                                  direct or indirect purposes.\n\nI will not \
                                  engage in criminal, infamous, dishonest, \
                                  notoriously disgraceful conduct or any \
                                  conduct deemed to have a negative effect \
                                  on Tax-Aid. I will treat all taxpayers in a \
                                  professional, courteous and respectful \
                                  manner\n\nI hereby release Tax-Aid, its \
                                  officers, directors, employees, and agents \
                                  from any claims, lawsuits, or actions I, my \
                                  heirs, or legal representatives may have \
                                  for any personal injury and/or property \
                                  damage I may incur as a result of my \
                                  volunteer services.")
        if answer == 'yes':
            TaxAidApp.add()
            msg.showinfo("Thank You and Welcome",
                         '''Thank you for registering! Please see a site 
                         manager for next steps.''')
        else:
            return


def main():
    tax_aid = TaxAidApp(TaxAidApp.root)
    tax_aid.root.mainloop()


if __name__ == '__main__':
    main()
