# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Company_form(object):
    def setupUi(self, Company_form):
        Company_form.setObjectName("Company_form")
        Company_form.resize(897, 789)
        self.groupBox = QtWidgets.QGroupBox(Company_form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 861, 751))
        self.groupBox.setStyleSheet("background-color: rgb(221, 255, 246);\n"
"background-color: rgb(80, 80, 80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(173, 83,137 , 255), stop:0.789773 rgba(60, 16, 83, 255));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 60, 691, 351))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 151, 33);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(206, 255, 180, 246), stop:0.789773 rgba(0, 255, 234, 255));\n"
"border: 1px solid black;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Ratechart_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.Ratechart_combo.setGeometry(QtCore.QRect(130, 20, 311, 20))
        self.Ratechart_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Ratechart_combo.setObjectName("Ratechart_combo")
        self.Ratechart_combo.addItem("")
        self.AddRtNm_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.AddRtNm_btn.setGeometry(QtCore.QRect(450, 20, 75, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AddRtNm_btn.setFont(font)
        self.AddRtNm_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.AddRtNm_btn.setObjectName("AddRtNm_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 140, 281, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.Cow_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Cow_lbl.setGeometry(QtCore.QRect(10, 40, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cow_lbl.setFont(font)
        self.Cow_lbl.setObjectName("Cow_lbl")
        self.Below_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Below_lbl.setGeometry(QtCore.QRect(40, 20, 41, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Below_lbl.setFont(font)
        self.Below_lbl.setObjectName("Below_lbl")
        self.Vas_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Vas_lbl.setGeometry(QtCore.QRect(90, 20, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Vas_lbl.setFont(font)
        self.Vas_lbl.setObjectName("Vas_lbl")
        self.Curd_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Curd_lbl.setGeometry(QtCore.QRect(140, 20, 41, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Curd_lbl.setFont(font)
        self.Curd_lbl.setObjectName("Curd_lbl")
        self.Std_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Std_lbl.setGeometry(QtCore.QRect(190, 20, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Std_lbl.setFont(font)
        self.Std_lbl.setObjectName("Std_lbl")
        self.AddEvn_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.AddEvn_lbl.setGeometry(QtCore.QRect(230, 20, 41, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AddEvn_lbl.setFont(font)
        self.AddEvn_lbl.setObjectName("AddEvn_lbl")
        self.CBelow_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CBelow_txt.setGeometry(QtCore.QRect(50, 40, 31, 18))
        self.CBelow_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CBelow_txt.setObjectName("CBelow_txt")
        self.CVas_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CVas_txt.setGeometry(QtCore.QRect(90, 40, 31, 18))
        self.CVas_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CVas_txt.setObjectName("CVas_txt")
        self.CCurd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CCurd_txt.setGeometry(QtCore.QRect(140, 40, 31, 18))
        self.CCurd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CCurd_txt.setObjectName("CCurd_txt")
        self.CStd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CStd_txt.setGeometry(QtCore.QRect(190, 40, 31, 18))
        self.CStd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CStd_txt.setObjectName("CStd_txt")
        self.CAddEvn_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.CAddEvn_txt.setGeometry(QtCore.QRect(240, 40, 31, 18))
        self.CAddEvn_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CAddEvn_txt.setObjectName("CAddEvn_txt")
        self.Buff_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Buff_lbl.setGeometry(QtCore.QRect(10, 70, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Buff_lbl.setFont(font)
        self.Buff_lbl.setObjectName("Buff_lbl")
        self.BCurd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BCurd_txt.setGeometry(QtCore.QRect(140, 70, 31, 18))
        self.BCurd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BCurd_txt.setObjectName("BCurd_txt")
        self.Bstd_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.Bstd_txt.setGeometry(QtCore.QRect(190, 70, 31, 18))
        self.Bstd_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Bstd_txt.setObjectName("Bstd_txt")
        self.BBelow_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BBelow_txt.setGeometry(QtCore.QRect(50, 70, 31, 18))
        self.BBelow_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BBelow_txt.setObjectName("BBelow_txt")
        self.BVas_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BVas_txt.setGeometry(QtCore.QRect(90, 70, 31, 18))
        self.BVas_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BVas_txt.setObjectName("BVas_txt")
        self.BAddEvn_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.BAddEvn_txt.setGeometry(QtCore.QRect(240, 70, 31, 18))
        self.BAddEvn_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BAddEvn_txt.setObjectName("BAddEvn_txt")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(300, 140, 231, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 101, 71))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.F_Fat_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.F_Fat_lbl.setGeometry(QtCore.QRect(10, 0, 34, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.F_Fat_lbl.setFont(font)
        self.F_Fat_lbl.setObjectName("F_Fat_lbl")
        self.T_fat_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.T_fat_lbl.setGeometry(QtCore.QRect(60, 0, 35, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.T_fat_lbl.setFont(font)
        self.T_fat_lbl.setObjectName("T_fat_lbl")
        self.BTFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.BTFat_txt.setGeometry(QtCore.QRect(60, 50, 31, 18))
        self.BTFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BTFat_txt.setObjectName("BTFat_txt")
        self.CFFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.CFFat_txt.setGeometry(QtCore.QRect(10, 20, 31, 18))
        self.CFFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CFFat_txt.setObjectName("CFFat_txt")
        self.BFFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.BFFat_txt.setGeometry(QtCore.QRect(10, 50, 31, 18))
        self.BFFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BFFat_txt.setObjectName("BFFat_txt")
        self.CTFat_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.CTFat_txt.setGeometry(QtCore.QRect(60, 20, 31, 18))
        self.CTFat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CTFat_txt.setObjectName("CTFat_txt")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(120, 20, 101, 71))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.F_lct_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.F_lct_lbl.setGeometry(QtCore.QRect(10, 0, 41, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.F_lct_lbl.setFont(font)
        self.F_lct_lbl.setObjectName("F_lct_lbl")
        self.T_lct_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.T_lct_lbl.setGeometry(QtCore.QRect(60, 0, 34, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.T_lct_lbl.setFont(font)
        self.T_lct_lbl.setObjectName("T_lct_lbl")
        self.BTlct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.BTlct_txt.setGeometry(QtCore.QRect(60, 50, 31, 18))
        self.BTlct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BTlct_txt.setObjectName("BTlct_txt")
        self.CFlct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.CFlct_txt.setGeometry(QtCore.QRect(10, 20, 31, 18))
        self.CFlct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CFlct_txt.setObjectName("CFlct_txt")
        self.BFlct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.BFlct_txt.setGeometry(QtCore.QRect(10, 50, 31, 18))
        self.BFlct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BFlct_txt.setObjectName("BFlct_txt")
        self.TLct_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.TLct_txt.setGeometry(QtCore.QRect(60, 20, 31, 18))
        self.TLct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TLct_txt.setObjectName("TLct_txt")
        self.RTChrtFileNm_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.RTChrtFileNm_lbl.setGeometry(QtCore.QRect(10, 250, 82, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RTChrtFileNm_lbl.setFont(font)
        self.RTChrtFileNm_lbl.setObjectName("RTChrtFileNm_lbl")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(100, 250, 321, 20))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.Sel_xls_File_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Sel_xls_File_btn.setGeometry(QtCore.QRect(440, 250, 75, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Sel_xls_File_btn.setFont(font)
        self.Sel_xls_File_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Sel_xls_File_btn.setObjectName("Sel_xls_File_btn")
        self.Route_lbl1 = QtWidgets.QLabel(self.groupBox_2)
        self.Route_lbl1.setGeometry(QtCore.QRect(50, 280, 42, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Route_lbl1.setFont(font)
        self.Route_lbl1.setObjectName("Route_lbl1")
        self.Route1_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.Route1_combo.setGeometry(QtCore.QRect(100, 280, 321, 20))
        self.Route1_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Route1_combo.setObjectName("Route1_combo")
        self.NewSetting_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.NewSetting_btn.setGeometry(QtCore.QRect(440, 280, 75, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NewSetting_btn.setFont(font)
        self.NewSetting_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.NewSetting_btn.setObjectName("NewSetting_btn")
        self.Route2_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.Route2_combo.setGeometry(QtCore.QRect(100, 310, 321, 20))
        self.Route2_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Route2_combo.setObjectName("Route2_combo")
        self.Route_lbl2 = QtWidgets.QLabel(self.groupBox_2)
        self.Route_lbl2.setGeometry(QtCore.QRect(50, 310, 42, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Route_lbl2.setFont(font)
        self.Route_lbl2.setObjectName("Route_lbl2")
        self.Update_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Update_btn.setGeometry(QtCore.QRect(440, 310, 75, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Update_btn.setFont(font)
        self.Update_btn.setStyleSheet("background-color: rgb(171, 196, 255);")
        self.Update_btn.setObjectName("Update_btn")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 50, 521, 80))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.Milk_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Milk_combo.setGeometry(QtCore.QRect(40, 10, 51, 18))
        self.Milk_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Milk_combo.setObjectName("Milk_combo")
        self.Milk_combo.addItem("")
        self.Milk_combo.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_7)
        self.dateEdit.setGeometry(QtCore.QRect(120, 50, 110, 18))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.Method_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Method_lbl.setGeometry(QtCore.QRect(384, 10, 51, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Method_lbl.setFont(font)
        self.Method_lbl.setObjectName("Method_lbl")
        self.Method_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Method_combo.setGeometry(QtCore.QRect(440, 10, 75, 18))
        self.Method_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Method_combo.setObjectName("Method_combo")
        self.Method_combo.addItem("")
        self.FIle_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.FIle_combo.setGeometry(QtCore.QRect(440, 50, 75, 18))
        self.FIle_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FIle_combo.setObjectName("FIle_combo")
        self.FIle_combo.addItem("")
        self.Milk_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Milk_lbl.setGeometry(QtCore.QRect(4, 10, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Milk_lbl.setFont(font)
        self.Milk_lbl.setObjectName("Milk_lbl")
        self.Apply_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Apply_lbl.setGeometry(QtCore.QRect(244, 50, 41, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Apply_lbl.setFont(font)
        self.Apply_lbl.setObjectName("Apply_lbl")
        self.Base_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Base_combo.setGeometry(QtCore.QRect(290, 10, 81, 18))
        self.Base_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Base_combo.setObjectName("Base_combo")
        self.Base_combo.addItem("")
        self.Base_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Base_lbl.setGeometry(QtCore.QRect(244, 10, 41, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Base_lbl.setFont(font)
        self.Base_lbl.setObjectName("Base_lbl")
        self.Date_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Date_lbl.setGeometry(QtCore.QRect(4, 50, 105, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Date_lbl.setFont(font)
        self.Date_lbl.setObjectName("Date_lbl")
        self.File_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.File_lbl.setGeometry(QtCore.QRect(400, 50, 31, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.File_lbl.setFont(font)
        self.File_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.File_lbl.setObjectName("File_lbl")
        self.Shift_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Shift_lbl.setGeometry(QtCore.QRect(104, 10, 34, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Shift_lbl.setFont(font)
        self.Shift_lbl.setObjectName("Shift_lbl")
        self.Shift_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Shift_combo.setGeometry(QtCore.QRect(144, 10, 81, 18))
        self.Shift_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Shift_combo.setObjectName("Shift_combo")
        self.Shift_combo.addItem("")
        self.Shift_combo.addItem("")
        self.Shift_combo.addItem("")
        self.Apply_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Apply_combo.setGeometry(QtCore.QRect(290, 50, 81, 18))
        self.Apply_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Apply_combo.setObjectName("Apply_combo")
        self.Apply_combo.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(129, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Table = QtWidgets.QTabWidget(self.groupBox)
        self.Table.setGeometry(QtCore.QRect(40, 420, 251, 251))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Table.setFont(font)
        self.Table.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.Table.setObjectName("Table")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Table.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Table.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.tab_3)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 150, 251, 16))
        self.horizontalScrollBar.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.Table.addTab(self.tab_3, "")
        self.Fat_and_fatrate_table = QtWidgets.QTableWidget(self.groupBox)
        self.Fat_and_fatrate_table.setGeometry(QtCore.QRect(300, 420, 191, 251))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Fat_and_fatrate_table.setFont(font)
        self.Fat_and_fatrate_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border: 1px solid black;")
        self.Fat_and_fatrate_table.setRowCount(1)
        self.Fat_and_fatrate_table.setColumnCount(2)
        self.Fat_and_fatrate_table.setObjectName("Fat_and_fatrate_table")
        item = QtWidgets.QTableWidgetItem()
        self.Fat_and_fatrate_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fat_and_fatrate_table.setHorizontalHeaderItem(1, item)
        self.Fat_and_fatrate_table.horizontalHeader().setCascadingSectionResizes(True)
        self.Fat_Lacto_SNF_rate_table = QtWidgets.QTableWidget(self.groupBox)
        self.Fat_Lacto_SNF_rate_table.setGeometry(QtCore.QRect(500, 420, 231, 251))
        self.Fat_Lacto_SNF_rate_table.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border: 1px solid black;")
        self.Fat_Lacto_SNF_rate_table.setRowCount(1)
        self.Fat_Lacto_SNF_rate_table.setColumnCount(4)
        self.Fat_Lacto_SNF_rate_table.setObjectName("Fat_Lacto_SNF_rate_table")
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_rate_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_rate_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_rate_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_rate_table.setHorizontalHeaderItem(3, item)
        self.Fat_Lacto_SNF_rate_table.horizontalHeader().setDefaultSectionSize(55)
        self.Fat_Lacto_SNF_rate_table.horizontalHeader().setMinimumSectionSize(41)
        self.New_btn = QtWidgets.QPushButton(self.groupBox)
        self.New_btn.setGeometry(QtCore.QRect(40, 680, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.New_btn.setFont(font)
        self.New_btn.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
        self.New_btn.setObjectName("New_btn")
        self.Cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.Cancel_btn.setGeometry(QtCore.QRect(130, 680, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_btn.setFont(font)
        self.Cancel_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
        self.Cancel_btn.setObjectName("Cancel_btn")
        self.Export_btn = QtWidgets.QPushButton(self.groupBox)
        self.Export_btn.setGeometry(QtCore.QRect(220, 680, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Export_btn.setFont(font)
        self.Export_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
        self.Export_btn.setObjectName("Export_btn")
        self.Import_RtChrt_btn = QtWidgets.QPushButton(self.groupBox)
        self.Import_RtChrt_btn.setGeometry(QtCore.QRect(310, 680, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Import_RtChrt_btn.setFont(font)
        self.Import_RtChrt_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
        self.Import_RtChrt_btn.setObjectName("Import_RtChrt_btn")
        self.Excel_btn = QtWidgets.QPushButton(self.groupBox)
        self.Excel_btn.setGeometry(QtCore.QRect(420, 680, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Excel_btn.setFont(font)
        self.Excel_btn.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(171, 196, 255);")
        self.Excel_btn.setObjectName("Excel_btn")
        self.Text_btn = QtWidgets.QPushButton(self.groupBox)
        self.Text_btn.setGeometry(QtCore.QRect(520, 680, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Text_btn.setFont(font)
        self.Text_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
        self.Text_btn.setObjectName("Text_btn")
        self.Exit_btn = QtWidgets.QPushButton(self.groupBox)
        self.Exit_btn.setGeometry(QtCore.QRect(620, 680, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Exit_btn.setFont(font)
        self.Exit_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
        self.Exit_btn.setObjectName("Exit_btn")

        self.retranslateUi(Company_form)
        self.Table.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Company_form)

    def retranslateUi(self, Company_form):
        _translate = QtCore.QCoreApplication.translate
        Company_form.setWindowTitle(_translate("Company_form", "Form"))
        self.groupBox_2.setTitle(_translate("Company_form", "Rate Chart Setting"))
        self.label.setText(_translate("Company_form", "Rate Chart Name :"))
        self.Ratechart_combo.setItemText(0, _translate("Company_form", "Rate Chart"))
        self.AddRtNm_btn.setText(_translate("Company_form", "AddRtNm"))
        self.groupBox_3.setTitle(_translate("Company_form", "Below Grade Milk Rate"))
        self.Cow_lbl.setText(_translate("Company_form", "Cow"))
        self.Below_lbl.setText(_translate("Company_form", "Below"))
        self.Vas_lbl.setText(_translate("Company_form", "Vas"))
        self.Curd_lbl.setText(_translate("Company_form", "Curd"))
        self.Std_lbl.setText(_translate("Company_form", "Std"))
        self.AddEvn_lbl.setText(_translate("Company_form", "AddEvn"))
        self.CBelow_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.CVas_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.CCurd_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.CStd_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.CAddEvn_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.Buff_lbl.setText(_translate("Company_form", "Buff"))
        self.BCurd_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.Bstd_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.BBelow_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.BVas_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.BAddEvn_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.groupBox_4.setTitle(_translate("Company_form", "RtChrt_From-To Range"))
        self.F_Fat_lbl.setText(_translate("Company_form", "F-Fat"))
        self.T_fat_lbl.setText(_translate("Company_form", "T-Fat"))
        self.BTFat_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.CFFat_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.BFFat_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.CTFat_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.F_lct_lbl.setText(_translate("Company_form", "F-Lct"))
        self.T_lct_lbl.setText(_translate("Company_form", "T-Lct"))
        self.BTlct_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.CFlct_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.BFlct_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.TLct_txt.setPlaceholderText(_translate("Company_form", "0.00"))
        self.RTChrtFileNm_lbl.setText(_translate("Company_form", "RtChrt FileNm:"))
        self.Sel_xls_File_btn.setText(_translate("Company_form", "Sel XLs File"))
        self.Route_lbl1.setText(_translate("Company_form", "Route"))
        self.NewSetting_btn.setText(_translate("Company_form", "New Setting"))
        self.Route_lbl2.setText(_translate("Company_form", "Route"))
        self.Update_btn.setText(_translate("Company_form", "Update"))
        self.Milk_combo.setItemText(0, _translate("Company_form", "Cow"))
        self.Milk_combo.setItemText(1, _translate("Company_form", "Bufellow"))
        self.Method_lbl.setText(_translate("Company_form", "Method:"))
        self.Method_combo.setItemText(0, _translate("Company_form", "RateChart"))
        self.FIle_combo.setItemText(0, _translate("Company_form", "Xls"))
        self.Milk_lbl.setText(_translate("Company_form", "Milk:"))
        self.Apply_lbl.setText(_translate("Company_form", "Apply:"))
        self.Base_combo.setItemText(0, _translate("Company_form", "Fat/Lact"))
        self.Base_lbl.setText(_translate("Company_form", "Base:"))
        self.Date_lbl.setText(_translate("Company_form", "Apply From Date:"))
        self.File_lbl.setText(_translate("Company_form", "File:"))
        self.Shift_lbl.setText(_translate("Company_form", "Shift:"))
        self.Shift_combo.setItemText(0, _translate("Company_form", "Moning"))
        self.Shift_combo.setItemText(1, _translate("Company_form", "Noon"))
        self.Shift_combo.setItemText(2, _translate("Company_form", "Night"))
        self.Apply_combo.setItemText(0, _translate("Company_form", "All"))
        self.label_3.setText(_translate("Company_form", "Company Name"))
        self.Table.setTabText(self.Table.indexOf(self.tab), _translate("Company_form", "118"))
        self.Table.setTabText(self.Table.indexOf(self.tab_2), _translate("Company_form", "108"))
        self.Table.setTabText(self.Table.indexOf(self.tab_3), _translate("Company_form", "109"))
        item = self.Fat_and_fatrate_table.horizontalHeaderItem(0)
        item.setText(_translate("Company_form", "Upto Fat"))
        item = self.Fat_and_fatrate_table.horizontalHeaderItem(1)
        item.setText(_translate("Company_form", "Fat Rate"))
        item = self.Fat_Lacto_SNF_rate_table.horizontalHeaderItem(0)
        item.setText(_translate("Company_form", " Fat"))
        item = self.Fat_Lacto_SNF_rate_table.horizontalHeaderItem(1)
        item.setText(_translate("Company_form", "Lacto"))
        item = self.Fat_Lacto_SNF_rate_table.horizontalHeaderItem(2)
        item.setText(_translate("Company_form", "SNF"))
        item = self.Fat_Lacto_SNF_rate_table.horizontalHeaderItem(3)
        item.setText(_translate("Company_form", "Rate"))
        self.New_btn.setText(_translate("Company_form", "New"))
        self.Cancel_btn.setText(_translate("Company_form", "Cancel"))
        self.Export_btn.setText(_translate("Company_form", "Export RtChrt"))
        self.Import_RtChrt_btn.setText(_translate("Company_form", "Import RtChrt"))
        self.Excel_btn.setText(_translate("Company_form", "Excel "))
        self.Text_btn.setText(_translate("Company_form", "Text"))
        self.Exit_btn.setText(_translate("Company_form", "Exit"))
