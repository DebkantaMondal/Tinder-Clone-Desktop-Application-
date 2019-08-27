from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from urllib.request import urlopen
import mysql.connector

class Tinder:

    def __init__(self):

        # connect to the database
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="tinderb1")
        self.mycursor = self.conn.cursor()
        
        # define GUI Window
        self.root=Tk()
        
        # define Title of The window
        self.root.title("Tinder Login")
        
        # define max min size of window
        
        self.root.minsize(500,500)
        self.root.maxsize(500,500)
        
        # homepage
        Label(self.root, text="WELCOME TO TINDER  |  LOGIN FROM HERE | @DEBKANTA", fg="#ff3333", width=0, height=0).grid(row=0, column=1)

        #Modify Area - Work on modifying
        
        self.img = ImageTk.PhotoImage(Image.open('images/Wall9.jpg'))
        panel = Label(self.root,image=self.img, width=500,height=200)
        panel.grid(row=0, columnspan=2)
        
        self.message=Label(text="",fg="red")
        self.message.grid(row=1, column=1)
        
        Label(self.root, text="Enter Email Id").grid(row=2, column=0)
        self.emailLogin = Entry(width=40)
        self.emailLogin.grid(row=2, column=1)

        Label(self.root, text="Enter Password").grid(row=3, column=0)
        self.passwordLogin = Entry(show="*", width=40)
        self.passwordLogin.grid(row=3, column=1)

        Button(text="Click to login", bg="#ff3333", fg="#fff", command=lambda: self.login()).grid(row=4, column=1)

        

        Label(text="New to Tinder? Register Here!", fg="blue").grid(row=6,column=1)
        Button(text="Click To Register", bg="#ff3333", fg="#fff", command=lambda: self.launchRegWindow()).grid(row=8,column=1)

        Label(text="powered by APPS/developer:debkanta", fg="#ff8080", justify="right").grid(row=10, column=1)

        self.root.mainloop()

    def check(self):
        self.mycursor.execute("""SELECT `mobno` FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                                  .format(self.emailLogin.get(), self.passwordLogin.get()))
        get=self.mycursor.fetchall()
        #print(getResponse)
        if len(get)==0:
            
            self.launchMoreDetails()
        else:
            self.login()

    def login(self):
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(self.emailLogin.get(), self.passwordLogin.get()))
        response=self.mycursor.fetchall()
        #print(response)
        
        if len(response)>0:
            self.current_user_id = response[0][0]
            self.current_user_gender = response[0][5]
            self.Id=response[0][0]
            self.name=response[0][1]
        #print(self.name)
            self.email=response[0][2]
            self.age=response[0][4]
            self.gender=response[0][5]
            self.city=response[0][6]
            self.Image=response[0][8]
            self.account(self.name)
        else:
            self.message.configure(text="Incorrect Email/Password!",)

    def launchRegWindow(self):
        self.destroyWindow()
        Label(self.root, text="WELCOME TO TINDER  |  REGISTRATION PAGE | @DEBKANTA", fg="#ff3333", width=0, height=0).grid(row=0,column=1)
        self.root.minsize(500,530)
        self.root.maxsize(500,530)
        self.img = ImageTk.PhotoImage(Image.open('images/Wall6.jpeg'))
        panel = Label(self.root,image=self.img, width=500,height=200)
        panel.grid(row=0, columnspan=2)

        self.reg=Label(text="", fg="red")
        self.reg.grid(row=1, column=1)

        self.reg1=Label(text="", fg="red")
        self.reg1.grid(row=2, column=1)

        self.reg2=Label(text="Fill this form with correct details", fg="blue")
        self.reg2.grid(row=3, column=1)

        Label(self.root, text="Full Name :").grid(row=4, column=0)
        self.nameInput = Entry(width=40)
        self.nameInput.grid(row=4, column=1)

        Label(self.root, text="Email Id :").grid(row=5, column=0)
        self.emailInput = Entry(width=40)
        self.emailInput.grid(row=5, column=1)

        Label(self.root, text="Password :").grid(row=6, column=0)
        self.passwordInput = Entry(show="*",width=40)
        self.passwordInput.grid(row=6, column=1)

        Label(self.root, text="Gender :").grid(row=7, column=0)
        self.genderInput = Entry(width=40)
        self.genderInput.grid(row=7, column=1)

        Label(self.root, text="Age :").grid(row=8, column=0)
        self.ageInput = Entry(width=40)
        self.ageInput.grid(row=8, column=1)

        Label(self.root, text="City :").grid(row=9, column=0)
        self.cityInput = Entry(width=40)
        self.cityInput.grid(row=9, column=1)

        Label(self.root, text="Mob No is registered only for Security Reason & we don't display it publicly.", fg="#ff3333").grid(row=10, columnspan=4)
        Label(self.root, text="Mob No :").grid(row=11, column=0)
        self.mobInput = Entry(width=40)
        self.mobInput.grid(row=11, column=1)
        
        

        Button(text="Submit", bg="#ff3333", fg="#fff", command=lambda: self.insertdetails(self.nameInput,self.emailInput,
                                                                                          self.passwordInput,self.genderInput,
                                                                                          self.ageInput,self.cityInput,self.mobInput)).grid(row=12, column=1)
        #self.__init__()

        Label(self.root, text="Ooops!I want to Login", fg="blue").grid(row=13, column=1)
        Button(text="Back to Login", bg="#ff3333", fg="#fff", command=lambda: self.loginRefresh()).grid(row=14, column=1)

        Label(text="powered by APPS/developer:debkanta", fg="#ff8080", justify="right").grid(row=15, column=1)
        
        
    def destroyWindow(self):
        for i in self.root.grid_slaves():
            i.destroy()
        self.root.title("Tinder Registration")

    def launchMoreDetails(self):
        self.destroyWindow()
        Label(text=" Mobile No Registration | Only For Security Purpose | Mob No Don't display Publicly ", fg="blue").grid(row=0,columnspan=2)
        Label(self.root, text="Enter Mobile No :").grid(row=1, column=0)
        self.mobInput = Entry()
        self.mobInput.grid(row=1, column=1)
        self.mobMsg=Label(text="",fg="red").grid(row=2, columnspan=1)
        Button(text="Submit", bg="#ff3333", fg="#fff", command=lambda: self.mobInsert(self.mobInput)).grid(row=3, column=1)
        


    def insertdetails(self,nameInput,emailInput,passwordInput,genderInput,ageInput,cityInput,mobInput):
        if (nameInput.get()=='' and emailInput.get()=='' and passwordInput.get()=='' and genderInput.get()=='' and ageInput.get()=='' and cityInput
            .get()=='' and mobInput.get()==''):
            self.reg.configure(text="Required Fields is/are empty. Fill now and Submit")
        else:
            
            if '@' in emailInput.get() and '.com' in emailInput.get() and len(mobInput.get())==10:
                if len(passwordInput.get())>3:
                    
                
                    self.mycursor.execute("""INSERT INTO `users` (`user_id`, `name`, `email`,  `password`, `gender`, `age`, `city`, `mobno`)
            VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}','{}')""".format(self.nameInput.get(), self.emailInput.get(), self.passwordInput.get(),
                                                                        self.genderInput.get(), self.ageInput.get(), self.cityInput.get(), self.mobInput.get()))
                    self.conn.commit()

                    self.loginRefresh()
                    
                else:
                    self.reg1.configure(text="Password minimum size must be 4 or greater than 4.")
            else:
                self.reg.configure(text="EmailInput/Mob No or Both is/are Invalid. Input Valid One.")

    
        

    def loginRefresh(self):
        self.destroyWindow()
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.root.title("Tinder Login")
        Label(self.root, text="Login to Tinder using your registered email_id & password", fg="#ff3333").grid(row=0,
                                                                                                           column=1)

        self.img = ImageTk.PhotoImage(Image.open('Wall9.jpg'))
        panel = Label(self.root,image=self.img, width=500,height=200)
        panel.grid(row=0, columnspan=2)
        
        self.message=Label(text="",fg="red")
        self.message.grid(row=1, column=1)
        
        Label(self.root, text="Enter Email Id").grid(row=2, column=0)
        self.emailLogin = Entry(width=40)
        self.emailLogin.grid(row=2, column=1)

        Label(self.root, text="Enter Password").grid(row=3, column=0)
        self.passwordLogin = Entry(show="*", width=40)
        self.passwordLogin.grid(row=3, column=1)

        Button(text="Click to login", bg="#ff3333", fg="#fff", command=lambda: self.login()).grid(row=4, column=1)

        

        Label(text="New to Tinder? Register Here!", fg="blue").grid(row=6,column=1)
        Button(text="Click To Register", bg="#ff3333", fg="#fff", command=lambda: self.launchRegWindow()).grid(row=8,column=1)

        Label(text="powered by APPS/developer:debkanta", fg="#ff8080", justify="right").grid(row=10, column=1)

        

    def account(self,name):
        self.destroyWindow()
        self.root.title("User Account")
        self.root.minsize(620, 500)
        self.root.maxsize(620, 500)
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff", command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff", command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff", command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=5)
        Label(self.root, text=name, fg="blue").grid(row=1,columnspan=4)
        Label(self.root, text="Welcome to Your Tinder Account", fg="blue").grid(row=2,columnspan=4)
        
        #image_url = Image
        #image_byt = urlopen(str(Image)).read()
        #image_b64 = base64.encodestring(image_byt)
        #photo = tk.PhotoImage(data=image_b64)
        #panel= Label(self.root, image=photo)
        #panel.grid(row=3, columnspan=4)
        
        Button(text="Dashboard", bg="#ff3333", fg="#fff",command=lambda :self.launchDashboard()).grid(row=4, columnspan=4)
        Button(text="Edit Profile", bg="#ff3333", fg="#fff",command=lambda :self.launchUpdate()).grid(row=5, columnspan=4)

    def launchDashboard(self):
        self.destroyWindow()
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff", command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff", width=16, command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff", command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Dashboard", fg="#ff3333", relief="sunken").grid(row=0, column=5)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=6)
        self.dashboard(self.Id,self.name,self.email,self.age,self.gender,self.city)

    def dashboard(self,Id,name,email,age,gender,city):
        self.root.title('User Dashboard')
        self.root.minsize(800,500)
        self.root.maxsize(800,500)
        Label(self.root, text="User_ID:", fg="#ff3333").grid(row=2,column=1)
        Label(self.root, text=Id, fg="#ff3333").grid(row=2,column=3)
        Label(self.root, text="User Name:", fg="#ff3333").grid(row=3,column=1)
        Label(self.root, text=name, fg="#ff3333").grid(row=3,column=3)
        Label(self.root, text="Email_ID:", fg="#ff3333").grid(row=4,column=1)
        Label(self.root, text=email, fg="#ff3333").grid(row=4,column=3)
        Label(self.root, text="Age:", fg="#ff3333").grid(row=5,column=1)
        Label(self.root, text=age, fg="#ff3333").grid(row=5,column=3)
        Label(self.root, text="Gender:", fg="#ff3333").grid(row=6,column=1)
        Label(self.root, text=gender, fg="#ff3333").grid(row=6,column=3)
        Label(self.root, text="City:", fg="#ff3333").grid(row=7,column=1)
        Label(self.root, text=city, fg="#ff3333").grid(row=7,column=3)


    def launchUpdate(self):
        self.destroyWindow()
        self.root.title('Edit User Profile')
        self.root.minsize(800,500)
        self.root.maxsize(800,500)
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff", command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff", width=16, command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff", command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Edit Profile", fg="#ff3333", relief="sunken").grid(row=0, column=5)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=6)
        self.dashboard(self.Id,self.name,self.email,self.age,self.gender,self.city)

        Button(text="Update", bg="#ff3333", fg="#fff", command=lambda :self.launchUpdateEmail()).grid(row=9, columnspan=4)
        

    

    def launchUpdateEmail(self):
        self.destroyWindow()
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff", command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff", width=16, command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff", command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Edit Profile", fg="#ff3333", relief="sunken").grid(row=0, column=5)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=6)

        self.msgUpdate=Label(text="", fg="red")
        self.msgUpdate.grid(row=1, columnspan=1)

        Label(text="Enter New Email:").grid(row=2, column=0)
        self.email=Entry()
        self.email.grid(row=2,column=1)

        

        Button(text="Update", bg="#ff3333", fg="#fff",command=lambda :self.updateEmail(self.email)).grid(row=3, column=1)

    
        
        


    def updateEmail(self,email):
        self.root.title('Edit Profile')
        self.root.minsize(800,500)
        self.root.maxsize(800,500)
        if (email.get()!=''):
            if '@' in email.get() and '.com' in email.get():
                self.mycursor.execute("""SELECT `email` FROM `users` WHERE `user_id` LIKE '{}'""".format(self.current_user_id))
                answer=self.mycursor.fetchall()
                email_prev=answer[0][0]
                if (email.get()!= email_prev):
                    self.mycursor.execute("""UPDATE `users` SET `email` = '{}'  WHERE `users`.`user_id` = '{}'""".format(email.get(),self.current_user_id))
                    self.conn.commit()
                    self.account(self.name)
                else:
                    self.msgUpdate.configure(text="This Email Id is already Registered")
            else:
                self.msgUpdate.configure(text="Email is Invalid")
        else:
            self.msgUpdate.configure(text="Fill Required Input Field")

    

    
        

    def launchViewAllUsers(self):
        self.destroyWindow()
        Button(text="View All Tinder Users", fg="#ff3333", relief="sunken").grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff", width=16, command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff", command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff", command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=5)
        self.viewAllUsers()

    def viewAllUsers(self):
        self.mycursor.execute("""SELECT `user_id`,`name`,`email`,`age`,`gender`,`city` FROM `users` WHERE `user_id` NOT LIKE '{}' AND `gender` NOT LIKE '{}'"""
                              .format(self.current_user_id, self.current_user_gender))
        all_users = self.mycursor.fetchall()
        self.root.title('View All Users')
        self.root.minsize(800,500)
        self.root.maxsize(800,500)
        Label1 = Label(self.root, text="USER_ID")
        Label1.grid(row=1, column=0)
        Label2 = Label(self.root, text="NAME")
        Label2.grid(row=1, column=1)
        Label3 = Label(self.root, text="AGE")
        Label3.grid(row=1, column=2)
        Label4 = Label(self.root, text="GENDER")
        Label4.grid(row=1, column=3)
        Label5 = Label(self.root, text="CITY")
        Label5.grid(row=1, column=4)
        Label6 = Label(self.root, text="EMAIL ID")
        Label6.grid(row=1, column=6)
        for index, dat in enumerate(all_users):
            Label(self.root, text=dat[0]).grid(row=index + 2, column=0)
            Label(self.root, text=dat[1]).grid(row=index + 2, column=1)
            Label(self.root, text=dat[3]).grid(row=index + 2, column=2)
            Label(self.root, text=dat[4]).grid(row=index + 2, column=3)
            Label(self.root, text=dat[5]).grid(row=index + 2, column=4)
            Label(self.root, text=dat[2]).grid(row=index + 2, column=6)

    def launchViewProposals(self):
        self.destroyWindow()
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff",command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", fg="#ff3333", relief="sunken").grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff",command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=5)
        self.viewProposals()

    def viewProposals(self):
        self.mycursor.execute(
            """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE `juliet_id`='{}'""".format(
                self.current_user_id))

        who_proposed = self.mycursor.fetchall()
        if len(who_proposed) > 0:



            self.root.title('View Proposals')
            self.root.minsize(620, 500)
            self.root.maxsize(620, 500)
            Label1 = Label(self.root, text="NAME")
            Label1.grid(row=1, column=0)
            Label2 = Label(self.root, text="AGE")
            Label2.grid(row=1, column=1)
            Label3 = Label(self.root, text="GENDER")
            Label3.grid(row=1, column=2)
            Label4 = Label(self.root, text="CITY")
            Label4.grid(row=1, column=3)
            for index, dat in enumerate(who_proposed):
                Label(self.root, text=dat[4]).grid(row=index + 2, column=0)
                Label(self.root, text=dat[7]).grid(row=index + 2, column=1)
                Label(self.root, text=dat[8]).grid(row=index + 2, column=2)
                Label(self.root, text=dat[9]).grid(row=index + 2, column=3)
        else:
            Label(self.root, text="No Proposals Seen", fg="red").grid(row=1,column=1)


    def launchViewProposed(self):
        self.destroyWindow()
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff",command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff",command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", fg="#ff3333", relief="sunken").grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=5)
        self.viewProposed()

    def viewProposed(self):
        self.mycursor.execute(
            """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE `romeo_id`='{}'""".format(
                self.current_user_id))

        who_proposal = self.mycursor.fetchall()

        if len(who_proposal) > 0:
            self.root.title('View Proposed')
            self.root.minsize(620, 500)
            self.root.maxsize(620, 500)
            Label1 = Label(self.root, text="NAME")
            Label1.grid(row=1, column=0)
            Label2 = Label(self.root, text="AGE")
            Label2.grid(row=1, column=1)
            Label3 = Label(self.root, text="GENDER")
            Label3.grid(row=1, column=2)
            Label4 = Label(self.root, text="CITY")
            Label4.grid(row=1, column=3)
            for index, dat in enumerate(who_proposal):
                Label(self.root, text=dat[4]).grid(row=index + 2, column=0)
                Label(self.root, text=dat[7]).grid(row=index + 2, column=1)
                Label(self.root, text=dat[8]).grid(row=index + 2, column=2)
                Label(self.root, text=dat[9]).grid(row=index + 2, column=3)



        else:
            Label(self.root, text="No Propose You ave Done", fg="red").grid(row=1, column=2)

    def launchMatches(self):
        self.destroyWindow()
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff",command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff",command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff",command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", fg="#ff3333", relief="sunken").grid(row=0, column=3)
        Button(text="Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchPropose()).grid(row=0, column=4)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=5)
        self.matches()


    def matches(self):
        self.mycursor.execute("""SELECT `name`,`age`,`email` FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`juliet_id`
                IN (SELECT `romeo_id` FROM `proposals` WHERE `juliet_id` LIKE '{}') AND `romeo_id` LIKE '{}'""".format(
            self.current_user_id, self.current_user_id))

        matched_user = self.mycursor.fetchall()
        if len(matched_user)>0:
            self.root.title('View Matches')
            self.root.minsize(680, 500)
            self.root.maxsize(680, 500)
            Label1 = Label(self.root, text="NAME")
            Label1.grid(row=1, column=0)
            Label2 = Label(self.root, text="AGE")
            Label2.grid(row=1, column=1)
            Label3 = Label(self.root, text="EMAIL ID")
            Label3.grid(row=1, columnspan=4)
            for index, dat in enumerate(matched_user):
                Label(self.root, text=dat[0]).grid(row=index + 2, column=0)
                Label(self.root, text=dat[1]).grid(row=index + 2, column=1)
                Label(self.root, text=dat[2]).grid(row=index + 2, columnspan=4)
        else:
            Label(self.root, text="No Matches Found", fg="red").grid(row=1, columnspan=2)

    def launchPropose(self):
        self.destroyWindow()
        self.root.title("Propose")
        self.root.minsize(620, 500)
        self.root.maxsize(620, 500)
        Button(text="View All Tinder Users", bg="#ff3333", fg="#fff",command=lambda :self.launchViewAllUsers()).grid(row=0, column=0)
        Button(text="View Proposals", bg="#ff3333", fg="#fff",command=lambda :self.launchViewProposals()).grid(row=0, column=1)
        Button(text="View Proposes", bg="#ff3333", fg="#fff",command=lambda :self.launchViewProposed()).grid(row=0, column=2)
        Button(text="View Matching of Proposal and Propose", bg="#ff3333", fg="#fff",command=lambda :self.launchMatches()).grid(row=0, column=3)
        Button(text="Propose", fg="#ff3333", relief="sunken").grid(row=0, column=4)
        Button(text="Logout", bg="#ff3333", fg="#fff",command=lambda :self.logout()).grid(row=0, column=5)

        Label(self.root, text="Enter Juliet_ID Whom You Want To Propose:", fg="blue").grid(row=2, columnspan=3)
        self.juliet_id = Entry()
        self.juliet_id.grid(row=3, columnspan=3)
        self.proposeMsg=Label(text="", fg="red")
        self.proposeMsg.grid(row=4, columnspan=3)
        Button(self.root, text="Propose", command=lambda :self.propose(self.juliet_id), bg="skyblue").grid(row=5, columnspan=3)

    def propose(self,juliet_id):
        self.root.title("Propose")
        self.root.minsize(620, 500)
        self.root.maxsize(620, 500)
        if juliet_id.get()=='':
            self.proposeMsg.configure(text="Input Juliet_ID whom You want to Propose.")
        else:
            self.mycursor.execute(
                """SELECT * FROM `proposals` WHERE `romeo_id` LIKE '{}' AND `juliet_id` LIKE'{}'""".format(
                    self.current_user_id, juliet_id.get()))
            already_proposed = self.mycursor.fetchall()
            if len(already_proposed) == 0:


                self.mycursor.execute(
                    """INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES (NULL, '{}', '{}')""".format(
                self.current_user_id, juliet_id.get()))
                self.conn.commit()

                Label(self.root, text="Proposal Sent Successfully.Fingers Crossed!", fg="blue").grid(row=1, columnspan=4)

            else:
                Label(self.root, text="You are already Proposed to This User_ID.", fg="red").grid(row=1, columnspan=4)

    def logout(self):
        self.current_user_id=0
        self.destroyWindow()
        self.loginRefresh()


obj=Tinder()
