# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 751)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 861, 751))
        self.groupBox.setStyleSheet("background-color: rgb(221, 255, 246);\n"
"background-color: rgb(80, 80, 80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(173, 83,137 , 255), stop:0.789773 rgba(60, 16, 83, 255));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Rate_Chart_Setting_Groupbox = QtWidgets.QGroupBox(self.groupBox)
        self.Rate_Chart_Setting_Groupbox.setGeometry(QtCore.QRect(40, 60, 681, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Rate_Chart_Setting_Groupbox.setFont(font)
        self.Rate_Chart_Setting_Groupbox.setStyleSheet("border: 1px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(206, 255, 180, 246), stop:0.789773 rgba(0, 255, 234, 255));")
        self.Rate_Chart_Setting_Groupbox.setObjectName("Rate_Chart_Setting_Groupbox")
        self.label = QtWidgets.QLabel(self.Rate_Chart_Setting_Groupbox)
        self.label.setGeometry(QtCore.QRect(10, 20, 115, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Ratechart_combo = QtWidgets.QComboBox(self.Rate_Chart_Setting_Groupbox)
        self.Ratechart_combo.setGeometry(QtCore.QRect(130, 20, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ratechart_combo.setFont(font)
        self.Ratechart_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Ratechart_combo.setObjectName("Ratechart_combo")
        self.Ratechart_combo.addItem("")
        self.AddRtNm_btn = QtWidgets.QPushButton(self.Rate_Chart_Setting_Groupbox)
        self.AddRtNm_btn.setGeometry(QtCore.QRect(450, 20, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AddRtNm_btn.setFont(font)
        self.AddRtNm_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.AddRtNm_btn.setObjectName("AddRtNm_btn")
        self.groupBox_7 = QtWidgets.QGroupBox(self.Rate_Chart_Setting_Groupbox)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 50, 551, 80))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.Milk_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Milk_combo.setGeometry(QtCore.QRect(50, 10, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Milk_combo.setFont(font)
        self.Milk_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Milk_combo.setObjectName("Milk_combo")
        self.Milk_combo.addItem("")
        self.Milk_combo.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_7)
        self.dateEdit.setGeometry(QtCore.QRect(120, 50, 110, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.Method_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Method_lbl.setGeometry(QtCore.QRect(410, 10, 52, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Method_lbl.setFont(font)
        self.Method_lbl.setObjectName("Method_lbl")
        self.Method_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Method_combo.setGeometry(QtCore.QRect(470, 10, 75, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Method_combo.setFont(font)
        self.Method_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Method_combo.setObjectName("Method_combo")
        self.Method_combo.addItem("")
        self.FIle_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.FIle_combo.setGeometry(QtCore.QRect(470, 50, 75, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FIle_combo.setFont(font)
        self.FIle_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FIle_combo.setObjectName("FIle_combo")
        self.FIle_combo.addItem("")
        self.Milk_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Milk_lbl.setGeometry(QtCore.QRect(4, 10, 34, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Milk_lbl.setFont(font)
        self.Milk_lbl.setObjectName("Milk_lbl")
        self.Apply_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Apply_lbl.setGeometry(QtCore.QRect(250, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Apply_lbl.setFont(font)
        self.Apply_lbl.setObjectName("Apply_lbl")
        self.Base_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Base_combo.setGeometry(QtCore.QRect(310, 10, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Base_combo.setFont(font)
        self.Base_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Base_combo.setObjectName("Base_combo")
        self.Base_combo.addItem("")
        self.Base_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Base_lbl.setGeometry(QtCore.QRect(250, 10, 41, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Base_lbl.setFont(font)
        self.Base_lbl.setObjectName("Base_lbl")
        self.Date_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Date_lbl.setGeometry(QtCore.QRect(4, 50, 105, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Date_lbl.setFont(font)
        self.Date_lbl.setObjectName("Date_lbl")
        self.File_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.File_lbl.setGeometry(QtCore.QRect(430, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.File_lbl.setFont(font)
        self.File_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.File_lbl.setObjectName("File_lbl")
        self.Shift_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.Shift_lbl.setGeometry(QtCore.QRect(110, 10, 34, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Shift_lbl.setFont(font)
        self.Shift_lbl.setObjectName("Shift_lbl")
        self.Shift_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Shift_combo.setGeometry(QtCore.QRect(150, 10, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Shift_combo.setFont(font)
        self.Shift_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Shift_combo.setObjectName("Shift_combo")
        self.Shift_combo.addItem("")
        self.Shift_combo.addItem("")
        self.Shift_combo.addItem("")
        self.Apply_combo = QtWidgets.QComboBox(self.groupBox_7)
        self.Apply_combo.setGeometry(QtCore.QRect(310, 50, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Apply_combo.setFont(font)
        self.Apply_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Apply_combo.setObjectName("Apply_combo")
        self.Apply_combo.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Rate_Chart_Setting_Groupbox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 661, 191))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.Fat_Group_box = QtWidgets.QGroupBox(self.groupBox_3)
        self.Fat_Group_box.setGeometry(QtCore.QRect(10, 10, 201, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Fat_Group_box.setFont(font)
        self.Fat_Group_box.setObjectName("Fat_Group_box")
        self.Fat_From_lbl = QtWidgets.QLabel(self.Fat_Group_box)
        self.Fat_From_lbl.setGeometry(QtCore.QRect(10, 20, 35, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Fat_From_lbl.setFont(font)
        self.Fat_From_lbl.setObjectName("Fat_From_lbl")
        self.Fat_From_txt = QtWidgets.QLineEdit(self.Fat_Group_box)
        self.Fat_From_txt.setGeometry(QtCore.QRect(60, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fat_From_txt.setFont(font)
        self.Fat_From_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fat_From_txt.setObjectName("Fat_From_txt")
        self.Fat_upto_lbl = QtWidgets.QLabel(self.Fat_Group_box)
        self.Fat_upto_lbl.setGeometry(QtCore.QRect(10, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Fat_upto_lbl.setFont(font)
        self.Fat_upto_lbl.setObjectName("Fat_upto_lbl")
        self.Fat_upto_txt = QtWidgets.QLineEdit(self.Fat_Group_box)
        self.Fat_upto_txt.setGeometry(QtCore.QRect(60, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fat_upto_txt.setFont(font)
        self.Fat_upto_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fat_upto_txt.setObjectName("Fat_upto_txt")
        self.Fat_rate_txt = QtWidgets.QLineEdit(self.Fat_Group_box)
        self.Fat_rate_txt.setGeometry(QtCore.QRect(130, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fat_rate_txt.setFont(font)
        self.Fat_rate_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fat_rate_txt.setObjectName("Fat_rate_txt")
        self.label_5 = QtWidgets.QLabel(self.Fat_Group_box)
        self.label_5.setGeometry(QtCore.QRect(130, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Lacto_Group_box = QtWidgets.QGroupBox(self.groupBox_3)
        self.Lacto_Group_box.setGeometry(QtCore.QRect(270, 10, 181, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Lacto_Group_box.setFont(font)
        self.Lacto_Group_box.setObjectName("Lacto_Group_box")
        self.Lacto_Rate_txt = QtWidgets.QLineEdit(self.Lacto_Group_box)
        self.Lacto_Rate_txt.setGeometry(QtCore.QRect(80, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lacto_Rate_txt.setFont(font)
        self.Lacto_Rate_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Lacto_Rate_txt.setObjectName("Lacto_Rate_txt")
        self.Lacto1_txt = QtWidgets.QLineEdit(self.Lacto_Group_box)
        self.Lacto1_txt.setGeometry(QtCore.QRect(10, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lacto1_txt.setFont(font)
        self.Lacto1_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Lacto1_txt.setObjectName("Lacto1_txt")
        self.Lacto2_txt = QtWidgets.QLineEdit(self.Lacto_Group_box)
        self.Lacto2_txt.setGeometry(QtCore.QRect(10, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lacto2_txt.setFont(font)
        self.Lacto2_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Lacto2_txt.setObjectName("Lacto2_txt")
        self.Lacto_Rate_lbl = QtWidgets.QLabel(self.Lacto_Group_box)
        self.Lacto_Rate_lbl.setGeometry(QtCore.QRect(80, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lacto_Rate_lbl.setFont(font)
        self.Lacto_Rate_lbl.setObjectName("Lacto_Rate_lbl")
        self.Fill_range_combo = QtWidgets.QCheckBox(self.groupBox_3)
        self.Fill_range_combo.setGeometry(QtCore.QRect(510, 20, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Fill_range_combo.setFont(font)
        self.Fill_range_combo.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.Fill_range_combo.setObjectName("Fill_range_combo")
        self.Add_range_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.Add_range_btn.setGeometry(QtCore.QRect(510, 60, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Add_range_btn.setFont(font)
        self.Add_range_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.Add_range_btn.setObjectName("Add_range_btn")
        self.Manual_Rate_Groupbox = QtWidgets.QGroupBox(self.groupBox_3)
        self.Manual_Rate_Groupbox.setGeometry(QtCore.QRect(10, 100, 441, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Manual_Rate_Groupbox.setFont(font)
        self.Manual_Rate_Groupbox.setObjectName("Manual_Rate_Groupbox")
        self.Manual_rate_SNF_txt = QtWidgets.QLineEdit(self.Manual_Rate_Groupbox)
        self.Manual_rate_SNF_txt.setGeometry(QtCore.QRect(250, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Manual_rate_SNF_txt.setFont(font)
        self.Manual_rate_SNF_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Manual_rate_SNF_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.Manual_rate_SNF_txt.setObjectName("Manual_rate_SNF_txt")
        self.Manual_rate_lct_txt = QtWidgets.QLineEdit(self.Manual_Rate_Groupbox)
        self.Manual_rate_lct_txt.setGeometry(QtCore.QRect(130, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Manual_rate_lct_txt.setFont(font)
        self.Manual_rate_lct_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Manual_rate_lct_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.Manual_rate_lct_txt.setObjectName("Manual_rate_lct_txt")
        self.Manual_rate_Rate_txt = QtWidgets.QLineEdit(self.Manual_Rate_Groupbox)
        self.Manual_rate_Rate_txt.setGeometry(QtCore.QRect(250, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Manual_rate_Rate_txt.setFont(font)
        self.Manual_rate_Rate_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Manual_rate_Rate_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.Manual_rate_Rate_txt.setObjectName("Manual_rate_Rate_txt")
        self.Manual_rate_Fat_txt = QtWidgets.QLineEdit(self.Manual_Rate_Groupbox)
        self.Manual_rate_Fat_txt.setGeometry(QtCore.QRect(130, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Manual_rate_Fat_txt.setFont(font)
        self.Manual_rate_Fat_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Manual_rate_Fat_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.Manual_rate_Fat_txt.setObjectName("Manual_rate_Fat_txt")
        self.Manual_rate_Fat_lbl = QtWidgets.QLabel(self.Manual_Rate_Groupbox)
        self.Manual_rate_Fat_lbl.setGeometry(QtCore.QRect(70, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Manual_rate_Fat_lbl.setFont(font)
        self.Manual_rate_Fat_lbl.setObjectName("Manual_rate_Fat_lbl")
        self.Manual_rate_lct_lbl = QtWidgets.QLabel(self.Manual_Rate_Groupbox)
        self.Manual_rate_lct_lbl.setGeometry(QtCore.QRect(70, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Manual_rate_lct_lbl.setFont(font)
        self.Manual_rate_lct_lbl.setObjectName("Manual_rate_lct_lbl")
        self.Manual_rate_Rate_lbl = QtWidgets.QLabel(self.Manual_Rate_Groupbox)
        self.Manual_rate_Rate_lbl.setGeometry(QtCore.QRect(200, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Manual_rate_Rate_lbl.setFont(font)
        self.Manual_rate_Rate_lbl.setObjectName("Manual_rate_Rate_lbl")
        self.Manual_rate_SNF_lbl = QtWidgets.QLabel(self.Manual_Rate_Groupbox)
        self.Manual_rate_SNF_lbl.setGeometry(QtCore.QRect(200, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Manual_rate_SNF_lbl.setFont(font)
        self.Manual_rate_SNF_lbl.setObjectName("Manual_rate_SNF_lbl")
        self.Update_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.Update_btn.setGeometry(QtCore.QRect(510, 100, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Update_btn.setFont(font)
        self.Update_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.Update_btn.setObjectName("Update_btn")
        self.SaveChart_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.SaveChart_btn.setGeometry(QtCore.QRect(510, 130, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SaveChart_btn.setFont(font)
        self.SaveChart_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.SaveChart_btn.setObjectName("SaveChart_btn")
        self.Transmit_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.Transmit_btn.setGeometry(QtCore.QRect(510, 160, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Transmit_btn.setFont(font)
        self.Transmit_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"")
        self.Transmit_btn.setObjectName("Transmit_btn")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 381, 41))
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
        self.fat_fatrate_table = QtWidgets.QTableWidget(self.groupBox)
        self.fat_fatrate_table.setGeometry(QtCore.QRect(290, 420, 191, 251))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.fat_fatrate_table.setFont(font)
        self.fat_fatrate_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(191, 191, 191);\n"
"border: 1px solid black;")
        self.fat_fatrate_table.setRowCount(1)
        self.fat_fatrate_table.setColumnCount(2)
        self.fat_fatrate_table.setObjectName("fat_fatrate_table")
        item = QtWidgets.QTableWidgetItem()
        self.fat_fatrate_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fat_fatrate_table.setHorizontalHeaderItem(1, item)
        self.fat_fatrate_table.horizontalHeader().setCascadingSectionResizes(True)
        self.Fat_Lacto_SNF_table = QtWidgets.QTableWidget(self.groupBox)
        self.Fat_Lacto_SNF_table.setGeometry(QtCore.QRect(490, 420, 231, 251))
        self.Fat_Lacto_SNF_table.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border: 1px solid black;")
        self.Fat_Lacto_SNF_table.setRowCount(1)
        self.Fat_Lacto_SNF_table.setColumnCount(4)
        self.Fat_Lacto_SNF_table.setObjectName("Fat_Lacto_SNF_table")
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Fat_Lacto_SNF_table.setHorizontalHeaderItem(3, item)
        self.Fat_Lacto_SNF_table.horizontalHeader().setDefaultSectionSize(55)
        self.Fat_Lacto_SNF_table.horizontalHeader().setMinimumSectionSize(41)
        self.Data_Table = QtWidgets.QPushButton(self.groupBox)
        self.Data_Table.setGeometry(QtCore.QRect(40, 680, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Data_Table.setFont(font)
        self.Data_Table.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
        self.Data_Table.setObjectName("Data_Table")
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
        self.Excel_btn.setStyleSheet("background-color: rgb(171, 196, 255);\n"
"border: 1px solid black;")
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
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(40, 420, 241, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Rate_Chart_Setting_Groupbox.setTitle(_translate("Form", "Rate Chart Setting"))
        self.label.setText(_translate("Form", "Rate Chart Name :"))
        self.Ratechart_combo.setItemText(0, _translate("Form", "Cmb_RtChartName"))
        self.AddRtNm_btn.setText(_translate("Form", "AddRtNm"))
        self.Milk_combo.setItemText(0, _translate("Form", "Cow"))
        self.Milk_combo.setItemText(1, _translate("Form", "Bufellow"))
        self.Method_lbl.setText(_translate("Form", "Method:"))
        self.Method_combo.setItemText(0, _translate("Form", "Cmb_RtMB"))
        self.FIle_combo.setItemText(0, _translate("Form", "Cmb_RtFT"))
        self.Milk_lbl.setText(_translate("Form", "Milk:"))
        self.Apply_lbl.setText(_translate("Form", "Apply:"))
        self.Base_combo.setItemText(0, _translate("Form", "Fat/Lact"))
        self.Base_lbl.setText(_translate("Form", "Base:"))
        self.Date_lbl.setText(_translate("Form", "Apply From Date:"))
        self.File_lbl.setText(_translate("Form", "File:"))
        self.Shift_lbl.setText(_translate("Form", "Shift:"))
        self.Shift_combo.setItemText(0, _translate("Form", "Moning"))
        self.Shift_combo.setItemText(1, _translate("Form", "Noon"))
        self.Shift_combo.setItemText(2, _translate("Form", "Night"))
        self.Apply_combo.setItemText(0, _translate("Form", "Cmb_RtApply"))
        self.Fat_Group_box.setTitle(_translate("Form", "Fat"))
        self.Fat_From_lbl.setText(_translate("Form", "From"))
        self.Fat_From_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.Fat_upto_lbl.setText(_translate("Form", "Up To"))
        self.Fat_upto_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.Fat_rate_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.label_5.setText(_translate("Form", "Rate"))
        self.Lacto_Group_box.setTitle(_translate("Form", "Lacto"))
        self.Lacto_Rate_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.Lacto1_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.Lacto2_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.Lacto_Rate_lbl.setText(_translate("Form", "Rate"))
        self.Fill_range_combo.setText(_translate("Form", "Fill Range"))
        self.Add_range_btn.setText(_translate("Form", "Add Range"))
        self.Manual_Rate_Groupbox.setTitle(_translate("Form", "Manual Rate"))
        self.Manual_rate_SNF_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.Manual_rate_lct_txt.setPlaceholderText(_translate("Form", "0.00"))
        self.Manual_rate_Rate_txt.setPlaceholderText(_translate("Form", "00.00"))
        self.Manual_rate_Fat_txt.setPlaceholderText(_translate("Form", "00.0"))
        self.Manual_rate_Fat_lbl.setText(_translate("Form", "Fat"))
        self.Manual_rate_lct_lbl.setText(_translate("Form", "Lct"))
        self.Manual_rate_Rate_lbl.setText(_translate("Form", "Rate"))
        self.Manual_rate_SNF_lbl.setText(_translate("Form", "SNF"))
        self.Update_btn.setText(_translate("Form", "Update"))
        self.SaveChart_btn.setText(_translate("Form", "Save Chart"))
        self.Transmit_btn.setText(_translate("Form", "Transmit"))
        self.label_3.setText(_translate("Form", "Company Information"))
        item = self.fat_fatrate_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Upto Fat"))
        item = self.fat_fatrate_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fat Rate"))
        item = self.Fat_Lacto_SNF_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", " Fat"))
        item = self.Fat_Lacto_SNF_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Lacto"))
        item = self.Fat_Lacto_SNF_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "SNF"))
        item = self.Fat_Lacto_SNF_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Rate"))
        self.Data_Table.setText(_translate("Form", "New"))
        self.Cancel_btn.setText(_translate("Form", "Cancel"))
        self.Export_btn.setText(_translate("Form", "Export RtChrt"))
        self.Import_RtChrt_btn.setText(_translate("Form", "Import RtChrt"))
        self.Excel_btn.setText(_translate("Form", "Excel "))
        self.Text_btn.setText(_translate("Form", "Text"))
        self.Exit_btn.setText(_translate("Form", "Exit"))
