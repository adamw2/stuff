import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_DataRecordDestroyer
import csv
from pandas.io.json import json_normalize
from flatten_json import flatten
import os
import requests
import pandas as pd
import json
from requests.auth import HTTPBasicAuth


class guitime(Ui_DataRecordDestroyer):
    def __init__(self, DataRecordDestroyer):
        Ui_DataRecordDestroyer.__init__(self)
        self.setupUi(DataRecordDestroyer)

        self.listpushButton.clicked.connect(self.apicheck)
        self.checkpushButton.clicked.connect(self.csvprint)
        self.deletepushButton.clicked.connect(self.deleter)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.multipushButton.clicked.connect(self.cells_are_selected)

    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.item(row, column)
        self.ID = item.text()
        print(self.ID)

    def cells_are_selected(self):
        items = self.tableWidget.selectedItems()
        x = []
        for i in list(items):
            x.append(str(i.text()))
        for i in list(x):
            print(i)
        for i in list(x):
            apikey = self.apiusername
            apipass = self.apipassword
            submissionid = i
            url = "https://api.prontoforms.com/api/1.1/data/" + submissionid + ".json"
            response = requests.delete(url, auth=HTTPBasicAuth(apikey, apipass))
            print("deleting " + str(submissionid))
            print(response)

    def apisave(self):
        self.apiusername = str(self.apiline1.text())
        self.apipassword = str(self.apiline2.text())
        print(self.apiusername, self.apipassword)

    def apicheck(self):
        self.apiusername = str(self.apiline1.text())
        self.apipassword = str(self.apiline2.text())
        apikey = self.apiusername
        apipass = self.apipassword
        print("Connecting using api key:" + apikey)
        response = requests.get(
            'https://api.prontoforms.com/api/1.1/data.json',
            auth=HTTPBasicAuth(apikey, apipass))
        data = response.json()
        data2 = json.dumps(data)
        data3 = json.loads(data2)
        print("total number of Data Records: " + str(data3["totalNumberOfResults"]))
        print("Number of Pages: " + str(data3["totalNumberOfPages"]))

    def deleter(self):
        apikey = self.apiusername
        apipass = self.apipassword
        submissionid = self.ID
        url = "https://api.prontoforms.com/api/1.1/data/" + submissionid + ".json"
        response = requests.delete(url, auth=HTTPBasicAuth(apikey, apipass))
        print("deleting " + str(submissionid))
        print(response)

    def csvprint(self):
        apikey = self.apiusername
        apipass = self.apipassword
        print("Connecting using api key:" + apikey)
        response = requests.get(
            'https://api.prontoforms.com/api/1.1/data.json',
            auth=HTTPBasicAuth(apikey, apipass))
        print(response)
        data = response.json()
        data2 = json.dumps(data)
        with open('json.txt', 'w') as f:
            print(data2, file=f)
        flatdata = data['pageData']
        dict_flattened = (flatten(record, '.') for record in flatdata)
        df = pd.DataFrame(dict_flattened)
        print(df)
        model = pandasModel(df)
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df.index))
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def list(self):
        apikey = self.apiusername
        apipass = self.apipassword
        print("Connecting using api key:" + apikey)
        response = requests.get(
            'https://api.prontoforms.com/api/1.1/data.json',
            auth=HTTPBasicAuth(apikey, apipass))
        print(response)
        data = response.json()
        data2 = json.dumps(data)
        with open('json.txt', 'w') as f:
            print(data2, file=f)
        flatdata = data['pageData']
        dict_flattened = (flatten(record, '.') for record in flatdata)
        df = pd.DataFrame(dict_flattened)
        print(df)
        dfs = df.to_string()
        self.listWidget.addItem(dfs)


class pandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    DataRecordDestroyer = QtWidgets.QDialog()

    prog = guitime(DataRecordDestroyer)

    DataRecordDestroyer.show()
    sys.exit(app.exec_())
