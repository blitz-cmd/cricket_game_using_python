from PyQt5 import QtCore, QtGui, QtWidgets
from evaluation import Ui_Form,QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_5.addWidget(self.lineEdit_7)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        spacerItem6 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 7, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 6, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_4.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_4.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew_team = QtWidgets.QAction(MainWindow)
        self.actionNew_team.setObjectName("actionNew_team")
        self.actionOpen_team = QtWidgets.QAction(MainWindow)
        self.actionOpen_team.setObjectName("actionOpen_team")
        self.actionSave_team = QtWidgets.QAction(MainWindow)
        self.actionSave_team.setObjectName("actionSave_team")
        self.actionEvaluate_team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_team.setObjectName("actionEvaluate_team")
        self.menuManage_Teams.addAction(self.actionNew_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOpen_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSave_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEvaluate_team)
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.exit)                              #when push button exit is pressed
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)   #when menu button is pressed

        self.radioButton_4.toggled.connect(self.ctg)                            #when radio button BAT is pressed
        self.radioButton_3.toggled.connect(self.ctg)                            #when radio button BWL is pressed
        self.radioButton_2.toggled.connect(self.ctg)                            #when radio button WKT is pressed
        self.radioButton.toggled.connect(self.ctg)                              #when radio button AR is pressed

        self.bat = 4                                                            #initializing the value of bat,bwl,wkt,ar,avl & used
        self.bwl = 3
        self.ar = 3
        self.wkt = 1
        self.avl = 1000
        self.used = 0

        self.listWidget.itemDoubleClicked.connect(self.removelist1)             #when items in list view1 is pressed
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)           #when items in list view2 is pressed

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Team Name"))
        self.label_6.setText(_translate("MainWindow", "Points Available"))
        self.label_7.setText(_translate("MainWindow", "Points Used"))
        self.label_4.setText(_translate("MainWindow", "BATSMAN (BAT)"))
        self.label_3.setText(_translate("MainWindow", "BOWLER (BWL)"))
        self.label_2.setText(_translate("MainWindow", "ALL ROUNDERS (AR)"))
        self.label.setText(_translate("MainWindow", "WICKET-KEEPER (WKT)"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label_5.setText(_translate("MainWindow", "Your selections"))
        self.radioButton_4.setText(_translate("MainWindow", "BAT"))
        self.radioButton_3.setText(_translate("MainWindow", "BWL"))
        self.radioButton.setText(_translate("MainWindow", "AR"))
        self.radioButton_2.setText(_translate("MainWindow", "WKT"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_team.setText(_translate("MainWindow", "New team"))
        self.actionOpen_team.setText(_translate("MainWindow", "Open team"))
        self.actionSave_team.setText(_translate("MainWindow", "Save team"))
        self.actionEvaluate_team.setText(_translate("MainWindow", "Evaluate team"))

    def exit(self):                                                             #its function is to exit the program when exit button is pressed
        import sys
        self.sd("Thanks")
        sys.exit()

    def sd(self,msg):                                                           #its function is to show message when required
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Fantasy Cricket")
        ret=Dialog.exec()

    def ctg(self):                                                              #when radio button is pressed, it checked which button is pressed and then fill the list
        ctgr=''
        if self.radioButton.isChecked()==True:ctgr='AR'
        if self.radioButton_2.isChecked()==True:ctgr='WKT'
        if self.radioButton_3.isChecked()==True:ctgr='BWL'
        if self.radioButton_4.isChecked()==True:ctgr='BAT'
        self.fillList(ctgr)

    def fillList(self,ctgr):                                                    #it fills the list according to the button pressed
        if self.lineEdit_7.text()=='':
            self.sd("Enter team name!")
            return
        self.listWidget.clear()                                                 #clear list widget1
        sql="select player from stats where ctg='"+ctgr+"';"                    #sql command to fetch data from database
        cur=conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.listWidget_2.count()):
                selected.append(self.listWidget_2.item(i).text())
            if row[0] not in selected:self.listWidget.addItem(row[0])

    def removelist1(self,item):                                                 #its function is to remove players from list1 and add to the list2
        ctgr=''
        if self.radioButton.isChecked()==True:ctgr='AR'
        if self.radioButton_2.isChecked()==True:ctgr='WKT'
        if self.radioButton_3.isChecked()==True:ctgr='BWL'
        if self.radioButton_4.isChecked()==True:ctgr='BAT'
        ret=self.cr(ctgr,item)                                                  #it check is adding player in list2 fulfills the condition
        if ret==True:                                                           #if the condition is true
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.show()                                                         #shows changes made in the program

    def removelist2(self,item):                                                 #its function is to remove players from list2 and add to the list1
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        cur=conn.execute("select player,value,ctg from stats where player='"+item.text()+"'") #sql command
        row=cur.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":                                                         #condition for adding players back to list1
            self.bat+=1
            if self.radioButton_4.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="BWL":                                                         #condition for adding players back to list1
            self.bwl+=1
            if self.radioButton_3.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="AR":                                                          #condition for adding players back to list1
            self.ar+=1
            if self.radioButton.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="WKT":                                                         #condition for adding players back to list1
            self.wkt+=1
            if self.radioButton_2.isChecked()==True:self.listWidget.addItem(item.text())
        self.show()

    def cr(self,ctgr,item):                                                     #check conditions
        msg=''
        if ctgr=="BAT" and self.bat<1:msg="More than 4 batsmen are not allowed"
        if ctgr=="BWL" and self.bwl<1:msg="More than 3 bowlers are not allowed"
        if ctgr=="AR" and self.ar<1:msg="More than 3 all rounders are not allowed"
        if ctgr=="WKT" and self.wkt<1:msg="More than 1 wicketkeeper are not allowed"
        if msg!='':
            self.sd(msg)                                                        #shows dialog box when condition is not meet
            return False
        if self.avl<=0:
            msg="Points has been exhausted!!"
            self.sd(msg)                                                        #shows dialog box when points has been exhausted
            return False
        if ctgr=="BAT":self.bat-=1
        if ctgr=="BWL":self.bwl-=1
        if ctgr=="WKT":self.wkt-=1
        if ctgr=="AR":self.ar-=1
        sql="select value from stats where player='"+item.text()+"'"            #sql commnad
        cur=conn.execute(sql)
        row=cur.fetchone()
        self.avl-=int(row[0])
        self.used+=int(row[0])
        return True

    def show(self):                                                             #updates value in the program
        self.lineEdit.setText(str(self.bat))
        self.lineEdit_2.setText(str(self.bwl))
        self.lineEdit_3.setText(str(self.ar))
        self.lineEdit_4.setText(str(self.wkt))
        self.lineEdit_5.setText(str(self.avl))
        self.lineEdit_6.setText(str(self.used))

    def menu(self,action):                                                      #when menu button is pressed
        txt=(action.text())                                                     #button action converted to text

        if txt=='New team':                                                     #when new team button is pressed
            self.bat=4
            self.bwl=3
            self.ar=3
            self.wkt=1
            self.used=0
            self.avl=1000
            self.listWidget.clear()                                             #clear list widget1 when new team is selected
            self.listWidget_2.clear()                                           #clear list widget2
            text,ok=QtWidgets.QInputDialog.getText(MainWindow,"Team","Enter name of team:") #dialog box for entering team name
            if ok==True:
                self.lineEdit_7.setText(str(text))
            self.show()                                                         #update the dialog box

        if txt == 'Save team':                                                  #when save team button is pressed
            count = self.listWidget_2.count()                                   #count players in list2
            selected = ""
            for i in range(count):
                selected += self.listWidget_2.item(i).text()
                if i < count:
                    selected += ","
            self.saveteam(self.lineEdit_7.text(), selected, self.used)

        if txt == 'Open team':                                                  #when open team button is pressed
            self.bat = 0
            self.bwl = 0
            self.ar = 0
            self.wk = 0
            self.avl = 1000
            self.used = 0
            self.listWidget.clear()                                             #clear list widget1 when open team is selected
            self.listWidget_2.clear()                                           #clear list widget2
            self.show()
            self.openteam()

        if txt == 'Evaluate team':                                              #when evaluate button is pressed
            from evaluation import Ui_Form                                      #import evaluate.py
            Form = QtWidgets.QDialog()
            ui = Ui_Form()
            ui.setupUi(Form)
            ret = Form.exec()

    def openteam(self):                                                         #open team main funtion
        sql = "select name from teams;"                                         #sql command
        cur = conn.execute(sql)
        teams = []
        for row in cur:
            teams.append(row[0])
        team, ok = QtWidgets.QInputDialog.getItem(MainWindow, "Dream", "Choose A Team", teams, 0, False) #dialog box for entering team name to be open
        if ok and team:
            self.lineEdit_7.setText(team)
        sql1 = "SELECT players,value from teams where name='" + team + "';"     #sql command
        cur = conn.execute(sql1)
        row = cur.fetchone()
        selected = row[0].split(',')
        self.listWidget_2.addItems(selected)
        self.used = row[1]
        self.avl = 1000 - row[1]
        count = self.listWidget_2.count()

        for i in range(count - 1):
            ply = self.listWidget_2.item(i).text()
            sql = "select ctg from stats where player='" + ply + "';"           #sql command
            cur = conn.execute(sql)
            row = cur.fetchone()
            ctgr = row[0]
            if ctgr == "BAT": self.bat =0
            if ctgr == "BWL": self.bwl =0
            if ctgr == "AR": self.ar =0
            if ctgr == "WKT": self.wkt =0
        self.show()

    def saveteam(self, nm, ply, val):                                           #save team main funtion
        if self.bat + self.bwl + self.ar + self.wkt!= 0:                        #check total number of players
            self.sd("Insufficient players")
            return

        sql = "INSERT INTO teams (name,players,value) VALUES ('" + nm + "','" + ply + "','" + str(val) + "');" #sql command
        try:
            cur = conn.execute(sql)
            self.sd("Team Saved Succesfully")
            conn.commit()
        except:
            self.sd("Error in Operation")
            conn.rollback()

if __name__ == "__main__":                                                      #main function
    import sys                                                                  #import system
    import sqlite3                                                              #import sqlite3
    conn=sqlite3.connect('players.db')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
