import wx
import os
import MySQLdb
class AddressBook(wx.Frame):
    def __init__(self):
        #creating database:
        wx.Frame.__init__(self,None,-1,"Address Book",size=(700,700))
        self.panel=wx.Panel(self,-1)
        self.SetBackgroundColour("#95CAE4")
       
        self.title=wx.StaticText(self.panel,-1,"ADDRESS BOOK DATABASE",pos=(120,10))
        self.title=wx.StaticText(self.panel,-1,"DATABASE SECTION",pos=(450,10))
        self.firstname=wx.StaticText(self.panel,-1,"FirstName",pos=(50,50))
        #self.firstname1=wx.TextCtrl(self.panel,-1,"",pos=(160,50),size=(100,20))
        self.secondname=wx.StaticText(self.panel,-1,"SecondName",pos=(35,80))
        
        self.hostname=wx.StaticText(self.panel,-1,"HostName",pos=(420,50))
        self.username=wx.StaticText(self.panel,-1,"UserName",pos=(420,75))
        self.password=wx.StaticText(self.panel,-1,"Password",pos=(420,100))
        self.dbname=wx.StaticText(self.panel,-1,"DbName",pos=(420,125))
        self.dbname=wx.StaticText(self.panel,-1,"Table Name: AddressBookDatabase",pos=(420,200))
        self.btnconnect=wx.Button(self.panel,300,"connect",pos=(520,150),size=(70,30))
        self.btncreate=wx.Button(self.panel,301,"Create Table",pos=(520,225))
        self.btncreate=wx.Button(self.panel,302,"close database",pos=(520,300))
        self.Bind(wx.EVT_BUTTON,self.clsdb,id=302)
        self.Bind(wx.EVT_BUTTON,self.connect,id=300)
        self.Bind(wx.EVT_BUTTON,self.create,id=301)
        self.dbname=wx.StaticText(self.panel,-1,"for first time click create table button. ",pos=(420,260))
        
        self.thostname=wx.TextCtrl(self.panel,-1,"",pos=(490,50),size=(170,20))
        self.tusername=wx.TextCtrl(self.panel,-1,"",pos=(490,75),size=(170,20))
        self.tpassword=wx.TextCtrl(self.panel,-1,"",pos=(490,100),size=(170,20))
        self.tdbname=wx.TextCtrl(self.panel,-1,"",pos=(490,125),size=(170,20))

        #self.secondname1=wx.TextCtrl(self.panel,-1,"",pos=(160,80),size=(100,20))
        self.addressline1=wx.StaticText(self.panel,-1,"Address(Line1)",pos=(30,110))
        self.addressline2=wx.StaticText(self.panel,-1,"Address(Line2)",pos=(30,140))
        self.addressline3=wx.StaticText(self.panel,-1,"Address(Line3)",pos=(30,170))
        self.city=wx.StaticText(self.panel,-1,"City",pos=(85,200))
        self.state=wx.StaticText(self.panel,-1,"State or Province",pos=(20,230))
        self.zip=wx.StaticText(self.panel,-1,"Postal(zip)Code",pos=(25,260))
        self.homephe=wx.StaticText(self.panel,-1,"HomePhone",pos=(40,290))
        self.workphe=wx.StaticText(self.panel,-1,"WorkPhone",pos=(45,320))
        self.mobile=wx.StaticText(self.panel,-1,"Mobile",pos=(70,350))
        self.email=wx.StaticText(self.panel,-1,"Primary Email",pos=(35,380))
        self.email2=wx.StaticText(self.panel,-1,"Secondary Email",pos=(20,410))
        self.notes=wx.StaticText(self.panel,-1,"Notes",pos=(75,440))

        self.firstname1=wx.TextCtrl(self.panel,-1,"",pos=(130,50),size=(170,20))
        self.secondname1=wx.TextCtrl(self.panel,-1,"",pos=(130,80),size=(170,20))
        self.addressline11=wx.TextCtrl(self.panel,-1,"",pos=(130,110),size=(250,20))
        self.addressline21=wx.TextCtrl(self.panel,-1,"",pos=(130,140),size=(250,20))
        self.addressline31=wx.TextCtrl(self.panel,-1,"",pos=(130,170),size=(250,20))
        
        self.city1=wx.TextCtrl(self.panel,-1,"",pos=(130,200),size=(170,20))
        self.state1=wx.TextCtrl(self.panel,-1,"",pos=(130,230),size=(170,20))
        self.zip1=wx.TextCtrl(self.panel,-1,"",pos=(130,260),size=(170,20))
        self.homephe1=wx.TextCtrl(self.panel,-1,"",pos=(130,290),size=(170,20))
        self.workphe1=wx.TextCtrl(self.panel,-1,"",pos=(130,320),size=(170,20))
        self.mobile1=wx.TextCtrl(self.panel,-1,"",pos=(130,350),size=(170,20))
        self.email3=wx.TextCtrl(self.panel,-1,"",pos=(130,380),size=(170,20))
        self.email4=wx.TextCtrl(self.panel,-1,"",pos=(130,410),size=(170,20))
        self.notes1=wx.TextCtrl(self.panel,-1,"",pos=(130,440),size=(250,100),style=wx.TE_MULTILINE)
        self.btn=wx.Button(self.panel,201,"save",pos=(170,570),size=(70,30))
        self.btn1=wx.Button(self.panel,202,"clear all",pos=(80,570),size=(70,30))
        self.btn2=wx.Button(self.panel,203,"retrieve",pos=(260,570),size=(70,30))
        
        self.Bind(wx.EVT_BUTTON,self.retrive,id=203)
        self.Bind(wx.EVT_BUTTON,self.clear,id=202)
        self.Bind(wx.EVT_BUTTON,self.save,id=201)


    def connect(self,event):

        #try:

        self.hn = self.thostname.GetValue()
        self.un = self.tusername.GetValue()
        self.p = self.tpassword.GetValue()
        self.db = self.tdbname.GetValue()
        
        self.db = MySQLdb.connect(self.hn,self.un,self.p,self.db)
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        self.data = self.cursor.fetchone()
        s=str(self.data)
        self.dial = wx.MessageDialog(None,'database connected, version:'+s, 'Info', wx.OK)
        self.dial.ShowModal()

      
            

    def clsdb(self,event):
        
        try:
            self.db.close()
            self.dial = wx.MessageDialog(None,'database connec closed', 'Info', wx.OK)
            self.dial.ShowModal()
        except:
             self.dial = wx.MessageDialog(None,'database already closed', 'Info', wx.OK)
             self.dial.ShowModal()
        

    def create(self,event):
        
        sql = "CREATE TABLE addressbookdatabase(Id INT PRIMARY KEY AUTO_INCREMENT,\
         FIRST_NAME  CHAR(20) NOT NULL,\
         LAST_NAME  CHAR(20),\
         ADDR_LINE1 CHAR(50),  \
         ADDR_LINE2 CHAR(50),\
         ADDR_LINE3 CHAR(50),\
         CITY CHAR(50),\
         STATE_OR_PROVINCE CHAR(50),\
         POSTAL_OR_ZIPCODE CHAR(50),\
         HOMEPHONE CHAR(50),\
         WORKPHONE CHAR(50),\
         MOBILE CHAR(50),\
         PRIMARY_EMAIL CHAR(50),\
         SECONDARY_EMAIL CHAR(50),\
         NOTES CHAR(150) )"

        try:
            self.cursor.execute(sql)
        except:
            
            self.dial = wx.MessageDialog(None, 'table name "addressbookdatabase already created"', 'Info', wx.OK)
            self.dial.ShowModal()
   


    def save(self,event):
        
        self.firstname=self.firstname1.GetValue()
        self.secondname=self.secondname1.GetValue()
        self.addressline1=self.addressline11.GetValue()
        self.addressline2=self.addressline21.GetValue()
        self.addressline3=self.addressline31.GetValue()
        self.city=self.city1.GetValue()
        self.state=self.state1.GetValue()
        self.zip=self.zip1.GetValue()
        self.homephe=self.homephe1.GetValue()
        self.workphe=self.workphe1.GetValue()
        self.mobile=self.mobile1.GetValue()
        self.email=self.email3.GetValue()
        self.email2=self.email4.GetValue()
        self.notes=self.notes1.GetValue()
        self.firstname.rstrip()
        self.secondname.rstrip()
        self.addressline1.rstrip()
        self.addressline2.rstrip()
        self.city.rstrip()
        self.state.rstrip()
        self.zip.rstrip()
        self.homephe.rstrip()
        self.workphe.rstrip()
        self.mobile.rstrip()
        self.email.rstrip()
        self.email2.rstrip()
        self.notes.rstrip()
        if (len(self.firstname) and len(self.secondname) and len(self.addressline1) and len(self.addressline2) and len(self.addressline3) and len(self.city) and len(self.state) and len(self.zip) and len(self.homephe) and len(self.workphe) and len(self.mobile) and len(self.email) and len(self.email2) and len(self.notes))>0:
            
           # print self.firstname
            box=wx.TextEntryDialog(None,"Enter AddressBookName To Save","Title","default text")
            
                #self.dial = wx.MessageDialog(None, 'saved successfully', 'Info', wx.OK)
                #self.dial.ShowModal()
                
                    #insert data to database
                    #self.db = MySQLdb.connect(self.hn,self.un,self.p,self.db)
                    #self.cursor = self.db.cursor()
                    
            sql1 = "INSERT INTO addressbookdatabase(FIRST_NAME,\
                              LAST_NAME,ADDR_LINE1,ADDR_LINE2,ADDR_LINE3,CITY,STATE_OR_PROVINCE,\
                                  POSTAL_OR_ZIPCODE, HOMEPHONE,WORKPHONE,MOBILE,PRIMARY_EMAIL,SECONDARY_EMAIL,NOTES)\
                                 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                             (self.firstname,self.secondname,self.addressline1,self.addressline2,self.addressline3,self.city,self.state,self.zip,self.homephe,self.workphe,self.mobile,self.email,self.email2,self.notes)
            self.cursor.execute(sql1)
            self.db.commit()
            self.dial = wx.MessageDialog(None, 'saved successfully to database', 'Info', wx.OK)
            self.dial.ShowModal()

            
                
                    
        else:

            self.dial = wx.MessageDialog(None, 'please fill all fields', 'Info', wx.OK)
            self.dial.ShowModal()

    def clear(self,event):
        self.firstname1.Clear()
        self.secondname1.Clear()
        self.addressline11.Clear()
        self.addressline21.Clear()
        self.addressline31.Clear()
        self.city1.Clear()
        self.state1.Clear()
        self.zip1.Clear()
        self.homephe1.Clear()
        self.workphe1.Clear()
        self.mobile1.Clear()
        self.email3.Clear()
        self.email4.Clear()
        self.notes1.Clear()
        

    def retrive(self,event):

        
        sql2 = "SELECT * FROM addressbookdatabase"
        self.cursor.execute(sql2)
        results = self.cursor.fetchall()
        
        fnames = list()
        for row in results:
            id = row[0]
            fname = row[1]
            ifn = str(id)+str(fname)
            fnames.append(ifn)
        #print fnames

        self.box=wx.SingleChoiceDialog(None,"choose Address book name","filenames",fnames)
        if self.box.ShowModal()==wx.ID_OK:
            self.apples=self.box.GetStringSelection()
            self.app=self.apples[:1]
            #self.uid = int(self.app)
            
            sql3 = "SELECT * FROM addressbookdatabase WHERE ID = "+self.app+""
            self.cursor.execute(sql3)
            results = self.cursor.fetchall()
            for row in results:
                line1 = row[1]
                line2 = row[2]
                line3 = row[3]
                line4 = row[4]
                line5 = row[5]
                line6 = row[6]
                line7 = row[7]
                line8 = row[8]
                line9 = row[9]
                line10 = row[10]
                line11 = row[11]
                line12 = row[12]
                line13 = row[13]
                line14 = row[14]
            self.firstname1.SetValue(str(line1))
            self.secondname1.SetValue(line2)
            self.addressline11.SetValue(line3)
            self.addressline21.SetValue(line4)
            self.addressline31.SetValue(line5)
        
            self.city1.SetValue(line6)
            self.state1.SetValue(line7)
            self.zip1.SetValue(line8)
            self.homephe1.SetValue(line9)
            self.workphe1.SetValue(line10)
            self.mobile1.SetValue(line11)
            self.email3.SetValue(line12)
            self.email4.SetValue(line13)
            self.notes1.SetValue(line14)
            self.btn4=wx.Button(self.panel,205,"update",pos=(350,570),size=(70,30))
            self.Bind(wx.EVT_BUTTON,self.update,id=205)
            self.note=wx.StaticText(self.panel,-1,"Note: After modification HIT UPDATE button",pos=(10,610))

    def update(self,event):

        
        self.firstname=self.firstname1.GetValue()
        #print self.firstname
        self.secondname=self.secondname1.GetValue()
        self.addressline1=self.addressline11.GetValue()
        self.addressline2=self.addressline21.GetValue()
        self.addressline3=self.addressline31.GetValue()
        self.city=self.city1.GetValue()
        self.state=self.state1.GetValue()
        self.zip=self.zip1.GetValue()
        self.homephe=self.homephe1.GetValue()
        self.workphe=self.workphe1.GetValue()
        self.mobile=self.mobile1.GetValue()
        self.email=self.email3.GetValue()
        self.email2=self.email4.GetValue()
        self.notes=self.notes1.GetValue()
        
        sql4 = "UPDATE addressbookdatabase SET FIRST_NAME = '%s',LAST_NAME = '%s',ADDR_LINE1='%s',ADDR_LINE2='%s',ADDR_LINE3='%s',\
               CITY='%s',STATE_OR_PROVINCE='%s',POSTAL_OR_ZIPCODE='%s',HOMEPHONE='%s',WORKPHONE='%s',MOBILE='%s',PRIMARY_EMAIL='%s',\
                SECONDARY_EMAIL='%s',NOTES='%s'\
        WHERE ID = '%s'" %(self.firstname,self.secondname,self.addressline1,self.addressline2,self.addressline3,self.city,self.state,self.zip,
                           self.homephe,self.workphe,self.mobile,self.email,self.email2,self.notes,self.app)
        self.cursor.execute(sql4)
        self.db.commit()
        self.updat.close()
        self.app=0
        self.btn4.Destroy()
        self.dial = wx.MessageDialog(None, 'updated', 'Info', wx.OK)
        self.dial.ShowModal()
        
app=wx.App()
frame=AddressBook()
frame.Centre()
frame.Show()
app.MainLoop()
