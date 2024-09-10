from tkinter import *
from functools import partial
from tkinter import ttk, messagebox
import mysql.connector as mc
c=mc.connect(host= "localhost", user="root", passwd="12345", database= "jobs360")
cr=c.cursor()


tkWin = Tk()  
tkWin.geometry('1200x675')  
tkWin.title('Home page')
tkWin.configure(bg="white")
bg= PhotoImage(file = "images/homebg.png")
bg_label= Label(tkWin, image=bg)
bg_label.place(x=1,y=1, relwidth=1, relheight=1)
loginbut=PhotoImage(file = "images/loginbut.png")




def login():
    tkWin.destroy()
    def posterlogin():
        username1= username.get()
        password1= password.get()
        datalog=(username1, password1)
        cr.execute("select * from loginpost")
        logdet=cr.fetchall()
        for x in logdet:
            if x==datalog:
                postjob("yes",username1)
                break
        else:
            cr.execute("insert into loginpost values(%s,%s)", datalog)
            cr.execute("insert into post (user) values(%s)", (username1,))
            c.commit()
            postjob("no", username1)
    def validateLogin():
        username1= username.get()
        password1= password.get()
        datalog=(username1, password1)
        cr.execute("select * from login")
        logdet=cr.fetchall()
        for x in logdet:
            if x==datalog:
                formfn("yes",username1)
                break
        else:
            cr.execute("insert into login values(%s,%s)", datalog)
            cr.execute("insert into form (user) values(%s)", (username1,))
            c.commit()
            formfn("no",username1)
    tkWindow = Tk()  
    tkWindow.geometry('1200x675')  
    tkWindow.title('Login page')
    tkWindow.configure(bg="white")
    loginbg= PhotoImage(file = "images/logbg.png")
    loginbut=PhotoImage(file = "images/loginbut.png")
    loginform=PhotoImage(file="images/home.png")
    bg_label= Label(tkWindow, image=loginbg)
    bg_label.place(x=1,y=1, relwidth=1, relheight=1)
    #username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name", font= "Helvetica 20", fg= "Black", bg="white")
    usernameLabel.place(x=400,y=300)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).place(x=600,y=300)  


    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password", font="HELVETICA 20", fg= "black", bg="white")
    passwordLabel.place(x=400,y=340)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*')
    passwordEntry.place(x=600,y=340)
    jobpost=PhotoImage(file = "images/postjobbut.png")
    jobpostbutton = Button(tkWindow, image=jobpost, command=posterlogin)
    jobpostbutton.place(x=400,y=400)
    jobseek=PhotoImage(file = "images/loginbutton.png")
    jobseekbutton = Button(tkWindow, image=jobseek, command=validateLogin)
    jobseekbutton.place(x=600,y=400)
   
   
    def formfn(x,y):
        tkWindow.destroy()
        a=y
        def formout():
            dataform=(full_name.get(), eq.get(),industry.get(),bio.get(),age.get(),contactvar.get(), a)
            cr.execute("update form set full_name=%s, education=%s, industry=%s, bio=%s, age=%s, contact=%s where USER=%s", dataform)
            c.commit()
            dashemp()
        tkform = Tk()  
        tkform.geometry('1200x675')  
        tkform.title('Form')
        tkform.configure(bg="white")
        bgform=PhotoImage(file = "images/formbg.png")
        enter=PhotoImage(file="images/enter.png")
        formbg_label= Label(tkform, image=bgform)
        formbg_label.place(x=1,y=1, relwidth=1, relheight=1)
        full_name = StringVar()
        full_nameentry = Entry(tkform, textvariable=full_name, font="helvetica 24")
        full_nameentry.place(x=400,y=255, width=200,height=40)  
        age = StringVar()
        ageentry = Entry(tkform, textvariable=age, font="helvetica 24")
        ageentry.place(x=400,y=320, width=200,height=40)
        options = ["ClassXII", "BA", "BBA", "BCOMM",
                "BTech", "BSc", "BALLB" , "MBA" , "MSc",
                "MCOMM", "MTech", "MBBS", "PhD"
               
        ]
        eq = StringVar()
        eq.set( "Choose highest qualification" )
        drop1 = OptionMenu( tkform , eq , *options)
        drop1.pack()
        drop1.place(x=400,y=380)
        options1 = ["IT", "Medical", "Finance", "Real_Estate",
                "Pure_Sciences", "Law", "Athletics" , "Entertainment" , "Agriculture",
                "Trade", "Education", "Automotive"
               
        ]
        industry = StringVar()
        industry.set( "Choose suitable option" )
        drop2 = OptionMenu( tkform , industry , *options1)
        drop2.pack()
        drop2.place(x=970,y=410)
        bio = StringVar()
        contactvar= StringVar()
        contactentry=Entry(tkform, textvariable=contactvar)
        contactentry.place(x=970,y=480)
        bioentry = Entry(tkform, textvariable=bio, font="helvetica 24")
        bioentry.place(x=80,y=500, width=600,height=150)
        ent=Button(tkform, image=enter, command=formout)
        ent.place(x=970,y=600)
        def ava():
            cr.execute("update form set status='available' where user=%s", (a,))
            c.commit()
        def unava():
            cr.execute("update form set status='unavailable' where user=%s", (a,))
            c.commit()
        def Simpletoggle(toggle_button):
            if toggle_button.config('text')[-1] == 'ON':
                toggle_button.config(text='OFF')
                ava()
            else:
                toggle_button.config(text='ON')
                unava()
        def dashemp():
            tkform.destroy()
            dashemp=Tk()
            dashemp.title("DASHBOARD")
            dashemp.geometry("1200x675")
            dashemp.config(bg="white")
            dashbg= PhotoImage(file = "images/dashboardbg.png")
            bg_label= Label(dashemp, image=dashbg)
            bg_label.place(x=1,y=1, relwidth=1,relheight=1)
            class Filter_Data:
                def __init__(self, dashemp):


                    self.var_search=StringVar()
                    text_search_ind=Entry(dashemp, textvariable= self.var_search, font="Helvetica 24")
                    self.var_searched=StringVar()
                    text_search_ed=Entry(dashemp, textvariable= self.var_searched, font="Helvetica 24")


                    text_search_ind.place(x=900, y=40,width=200, height=40)
                    text_search_ind.bind("<Key>",self.search)
                    text_search_ed.place(x=900, y=80,width=200, height=40)
                    text_search_ed.bind("<Key>",self.search)


                    self.C_Frame=Frame(dashemp,bd=5,relief=RIDGE)
                    self.C_Frame.place(x=40, y=150,width=1100,height=500)
                    scrolly=Scrollbar(self.C_Frame, orient=VERTICAL)
                    scrollx=Scrollbar(self.C_Frame, orient=HORIZONTAL)
                    self.post=ttk. Treeview(self.C_Frame, columns=("comp_name","Ed_requirements","industry","other_req","position","contact", "status"))
                    scrollx.pack(side=BOTTOM, fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)
                    scrollx.config(command=self.post.xview)
                    scrolly.config(command=self.post.yview)
                    self.post.heading("comp_name",text="COMPANY/ORGANIZATION")
                    self.post.heading("Ed_requirements",text="EDUCATION")
                    self.post.heading("industry",text="INDUSTRY")
                    self.post.heading("other_req",text="WE ARE LOOKING FOR...")
                    self.post.heading("position",text="POSITION OFFERED")
                    self.post.heading("contact",text="CONTACT US")
                    self.post.heading("status",text="STATUS")
                    self.post["show"]='headings'
                    self.post.column("comp_name",width=250)
                    self.post.column("Ed_requirements",width=100)
                    self.post.column("industry",width=100)
                    self.post.column("other_req",width=300)
                    self.post.column("position",width=150)
                    self.post.column("contact",width=250)
                    self.post.column("status",width=150)
                    self.post.pack(fill=BOTH, expand=1)
                    #self.show()
                def search(self,ev):
                    c=mc.connect(host= "localhost", user="root", passwd="12345", database= "jobs360")
                    cur=c.cursor()
                    try:
                        cur.execute("SELECT * FROM POST where industry LIKE '%"+self.var_search.get()+"%' and Ed_Requirements LIKE '%"+self.var_searched.get()+"%'")
                        row= cur.fetchall()
                        # print (row)
                        if len(row)>0:
                            self.post.delete(*self.post.get_children())
                            for i in row:
                                self.post.insert('', END, values=i)
                        else:
                            self.post.delete(*self.post.get_children())
                    except Exception as ex:
                        messagebox.showerror("Error",f"Error due to {str(ex)}")        


            obj=Filter_Data(dashemp)
            Label(dashemp, text=user, font="Helvetica 20").place(x=900, y=20,width=200, height=40)
            toggle_button = Button(text="OFF", width=10,bg="White", command=lambda: Simpletoggle(toggle_button))
            toggle_button.place(x=500, y=70)
           
            dashemp.mainloop()


        if x== "yes":
            alracc=PhotoImage(file="images/alreadyloggedin.png")
            alraccbutton=Button(tkform, image=alracc, command=dashemp)
            alraccbutton.place(x=1,y=1, relwidth=1,relheight=1)
        tkform.mainloop()






    def postjob(x,y):
        tkWindow.destroy()
        a=y
        def postout():
            postform=(comp_name.get(), eq.get(),industry.get(),other.get(),pos.get(),contactvar.get(),y)
            cr.execute("update post set comp_name=%s, ed_requirements=%s, industry=%s, other_req=%s, position=%s, contact=%s where USER=%s", postform)
            c.commit()
            dashjobs()
        tkpost = Tk()  
        tkpost.geometry('1200x675')  
        tkpost.title('Post A Job')
        tkpost.configure(bg="white")
        postbg=PhotoImage(file = "images//postbg.png")
        enter=PhotoImage(file="images/enter.png")
        homepost=PhotoImage(file="images/home.png")
        homeposticon=Button(tkpost, image=homepost)
        homeposticon.place(x=10, y=10, height=50, width=50)
        postbg_label= Label(tkpost, image= postbg)
        postbg_label.place(x=1,y=1, relwidth=1, relheight=1)
        comp_name = StringVar()
        comp_nameentry = Entry(tkpost, textvariable=comp_name).place(x=500,y=255, width=200,height=40)  
        pos = StringVar()
        posentry = Entry(tkpost, textvariable=pos).place(x=400,y=320, width=200,height=40)
        options = ["Class XII", "BA", "BBA", "BCOMM",
                "BTech", "BSc", "BA LLB" , "MBA" , "MSc",
                "MCOMM", "MTech", "MBBS", "PhD"
               
        ]
        eq = StringVar()
        eq.set( "Choose highest qualification" )
        drop1 = OptionMenu( tkpost , eq , *options ).place(x=400,y=380)
        options1 = ["IT", "Medical", "Finance", "Real Estate",
                "Pure Sciences", "Law", "Athletics" , "Entertainment" , "Agriculture",
                "Trade", "Education", "Automotive"
               
        ]
        industry = StringVar()
        industry.set( "Choose suitable option" )
        drop2 = OptionMenu( tkpost , industry , *options1 ).place(x=970,y=390)
        other = StringVar()
        contactvar= StringVar()
        contactentry=Entry(tkpost, textvariable=contactvar).place(x=970,y=480)
        otherentry = Entry(tkpost, textvariable=other).place(x=80,y=540, width=600,height=130)
        ent=Button(tkpost, image=enter, command=postout).place(x=970,y=600)
        def ava():
            cr.execute("update post set status='available' where user=%s", (a,))
            c.commit()
        def unava():
            cr.execute("update post set status='unavailable' where user=%s", (a,))
            c.commit()
        def Simpletoggle(toggle_button):
            if toggle_button.config('text')[-1] == 'ON':
                toggle_button.config(text='OFF')
                ava()
            else:
                toggle_button.config(text='ON')
                unava()


        def dashjobs():
            tkpost.destroy()
            dashjobs=Tk()
            dashjobs.title("DASHBOARD")
            dashjobs.geometry("1200x675")
            dashjobs.config(bg="white")
            dashjobsbg= PhotoImage(file = "images/dashboardbg.png")
            dashjobs_label= Label(dashjobs, image=dashjobsbg)
            dashjobs_label.place(x=1,y=1, relwidth=1, relheight=1)
            homedashjobs=PhotoImage(file="images/home.png")
            homedashjobsicon=Button(dashjobs, image=homedashjobs).place(x=10, y=10, height=50, width=50)
            class Filter_Data:
                def __init__(self, dashjobs):
                    self.var_searchindus=StringVar()
                    text_search_ind=Entry(dashjobs, textvariable= self.var_searchindus, font="Helvetica 24")
                    self.var_searched=StringVar()
                    text_search_ed=Entry(dashjobs, textvariable= self.var_searched, font="Helvetica 24")


                    text_search_ind.place(x=900, y=40,width=200, height=40)
                    text_search_ind.bind("<Key>",self.search)
                    text_search_ed.place(x=900, y=80,width=200, height=40)
                    text_search_ed.bind("<Key>",self.search)
                    self.C_Frame=Frame(dashjobs,bd=5,relief=RIDGE)
                    self.C_Frame.place(x=40, y=150,width=1100,height=500)
                    scrolly=Scrollbar(self.C_Frame, orient=VERTICAL)
                    scrollx=Scrollbar(self.C_Frame, orient=HORIZONTAL)
                    self.post=ttk. Treeview(self.C_Frame, columns=("full_name","education","industry","bio","age","contact","status"))
                    scrollx.pack(side=BOTTOM, fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)
                    scrollx.config(command=self.post.xview)
                    scrolly.config(command=self.post.yview)
                    self.post.heading("full_name",text="FULL NAME")
                    self.post.heading("education",text="EDUCATION")
                    self.post.heading("industry",text="INDUSTRY")
                    self.post.heading("bio",text="BIO/ABOUT")
                    self.post.heading("age",text="AGE")
                    self.post.heading("contact",text="CONTACT ME")
                    self.post.heading("status",text="STATUS")
                    self.post["show"]='headings'
                    self.post.column("full_name",width=150)
                    self.post.column("education",width=100)
                    self.post.column("industry",width=100)
                    self.post.column("bio",width=500)
                    self.post.column("age",width=100)
                    self.post.column("contact",width=250)
                    self.post.column("status",width=150)
                    self.post.pack(fill=BOTH, expand=1)
                    #self.show()
                def search(self,ev):
                    c=mc.connect(host= "localhost", user="root", passwd="12345", database= "jobs360")
                    cur=c.cursor()
                    try:
                        cur.execute("SELECT * FROM form where industry LIKE '%"+self.var_searchindus.get()+"%'and education LIKE '%"+self.var_searched.get()+"%'")
                        row= cur.fetchall()
                        # print (row)
                        if len(row)>0:
                            self.post.delete(*self.post.get_children())
                            for i in row:
                                self.post.insert('', END, values=i)
                        else:
                            self.post.delete(*self.post.get_children())
                    except Exception as ex:
                        messagebox.showerror("Error",f"Error due to {str(ex)}")        


            obj=Filter_Data(dashjobs)


            toggle_button = Button(text="OFF", width=10,bg="White", command=lambda: Simpletoggle(toggle_button))
            toggle_button.place(x=500, y=70)


            dashjobs.mainloop()






        if x== "yes":
            alracc=PhotoImage(file="images/alreadyloggedin.png")
            alraccbutton=Button(tkpost, image=alracc, command=dashjobs)
            alraccbutton.place(x=1,y=1, relwidth=1,relheight=1)
        tkpost.mainloop()
    tkWindow.mainloop()


loginButton = Button(tkWin, image=loginbut, command=login).place(x=1000,y=30)
tkWin.mainloop()
