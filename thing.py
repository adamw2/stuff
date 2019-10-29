import os
import requests
import pandas as pd
import json
from json2html import *
from requests.auth import HTTPBasicAuth
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import csv
from pandas.io.json import json_normalize

class App(QWidget):

    def clickbuttons(self):
        QMessageBox.about(self, "Success", "Exported data record")

#    def clickapi(self):
#        QMessageBox.about(self, "API information saved")

    def pushexcel(self):
        excelprint()

    def pushhtml(self):
        apicall()
        exporthtml()
        print("Datarecords exported")

    def __init__(self):
        super().__init__()
        self.title = 'Datarecord exporter'
        self.left = 600
        self.top = 300
        self.width = 320
        self.height = 200
        self.initUI()

    def pushcsv(self):
        csvprint(self)

    def initUI(self):

        # Create textboxes
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(140, 20)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox.setPlaceholderText("Insert API Key here")
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(100, 40)
        self.textbox2.resize(140, 20)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox2.setPlaceholderText("Insert Secret Key here")

        button3 = QPushButton('Apply API', self)
        button3.setToolTip('This saves your api to the program')
        button3.move(240, 20)
        button3.resize(40, 40)
#        button3.clicked.connect(self.clickapi)
        button3.clicked.connect(self.apisave)

        button1 = QPushButton('Export Data Record to CSV', self)
        button1.setToolTip('This creates a csv file')
        button1.move(100, 70)
        button1.clicked.connect(self.pushcsv)
        button1.clicked.connect(self.clickbuttons)

        button2 = QPushButton('Export Data Record to Excel', self)
        button2.setToolTip('This creates an excel file')
        button2.move(100, 100)
        button2.clicked.connect(self.pushexcel)
        button2.clicked.connect(self.clickbuttons)

        button4 = QPushButton('Export Data Record to html', self)
        button4.setToolTip('This dumps to html file')
        button4.move(100, 130)
        button4.clicked.connect(self.pushhtml)
        button4.clicked.connect(self.clickbuttons)

        self.show()

    def apisave(self):
        self.apiusername = str(self.textbox.text())
        self.apipassword = str(self.textbox2.text())
        print(self.apiusername, self.apipassword)


def apicall():
    response = requests.get(
        'https://api.url.com/api/1.1/data.json',
        auth=HTTPBasicAuth(self.apiusername, self.apipassword)).json()

    data_processed = json.dumps(response)
    formatted_table = json2html.convert(json = data_processed)


def exporthtml():
    export = open("output"+".html", "w")
    export.write(formatted_table)
    export.close()

    htmlout = 'output.html'


def jprint(response):
    text = json.dumps(response, sort_keys=True, indent=4)
    print(text)

def csvprint(self):
    apikey = self.apiusername
    apipass = self.apipassword
    print("Connecting using api key:" + apikey)
    response = requests.get(
        'https://api.prontoforms.com/api/1.1/data.json',
        auth=HTTPBasicAuth(apikey, apipass))
    print(response)
    data = response.json()
    formatted_table = json2html.convert(json=data)
    data2 = json.dumps(data)
    with open('json.txt', 'w') as f:
        print(data2, file=f)
    export = open("output"+".html", "w")
    export.write(formatted_table)
    export.close()
    normal = json_normalize(data, 'pageData', ['identifier'], errors = 'ignore')
    print(normal)

def excelprint():
    htmltable = "output.html"
    table = pd.read_html(htmltable)[0]
    table.to_excel("data.xlsx")
    os.system("start EXCEL.EXE data.xlsx")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


#jsondata = data
#with open("csvtest.csv", "w")
#wr = csv.writer(outfile)
#wr.writerow(["identifier", "referenceNumber", "state", "dataState",
#             "formId", "userId", "username"])
#wr.writerow([data["identifier"], data["referenceNumber"], data["state"]
#             data["dataState"], data["formId"], data["userId"]
#             data["username"]])
