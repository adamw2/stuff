# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataRecordDestroyer(object):
    def setupUi(self, DataRecordDestroyer):
        DataRecordDestroyer.setObjectName("DataRecordDestroyer")
        DataRecordDestroyer.resize(962, 559)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DataRecordDestroyer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(DataRecordDestroyer)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.apiline1 = QtWidgets.QLineEdit(self.widget)
        self.apiline1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apiline1.setObjectName("apiline1")
        self.gridLayout.addWidget(self.apiline1, 0, 1, 1, 1)
        self.listpushButton = QtWidgets.QPushButton(self.widget)
        self.listpushButton.setObjectName("listpushButton")
        self.gridLayout.addWidget(self.listpushButton, 0, 2, 1, 1)
        self.deletepushButton = QtWidgets.QPushButton(self.widget)
        self.deletepushButton.setObjectName("deletepushButton")
        self.gridLayout.addWidget(self.deletepushButton, 0, 3, 1, 1)
        self.apiline2 = QtWidgets.QLineEdit(self.widget)
        self.apiline2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apiline2.setObjectName("apiline2")
        self.gridLayout.addWidget(self.apiline2, 1, 1, 1, 1)
        self.checkpushButton = QtWidgets.QPushButton(self.widget)
        self.checkpushButton.setObjectName("checkpushButton")
        self.gridLayout.addWidget(self.checkpushButton, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)
        self.multipushButton = QtWidgets.QPushButton(self.widget)
        self.multipushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.multipushButton.setObjectName("multipushButton")
        self.gridLayout.addWidget(self.multipushButton, 4, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(DataRecordDestroyer)
        QtCore.QMetaObject.connectSlotsByName(DataRecordDestroyer)

    def retranslateUi(self, DataRecordDestroyer):
        _translate = QtCore.QCoreApplication.translate
        DataRecordDestroyer.setWindowTitle(_translate("DataRecordDestroyer", "Data Record Destroyer"))
        self.label.setText(_translate("DataRecordDestroyer", "API Key"))
        self.listpushButton.setText(_translate("DataRecordDestroyer", "Login"))
        self.deletepushButton.setText(_translate("DataRecordDestroyer", "Delete Record"))
        self.checkpushButton.setText(_translate("DataRecordDestroyer", "load table"))
        self.label_2.setText(_translate("DataRecordDestroyer", "Password"))
        self.multipushButton.setText(_translate("DataRecordDestroyer", "DELETE \n"
"  SELECTED \n"
" RECORDS"))
