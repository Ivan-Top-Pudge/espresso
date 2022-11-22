import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 700, 400))
        self.tableWidget.setObjectName("tablewidget")

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(275, 475, 250, 100))
        font = QtGui.QFont('', 16)
        self.pushButton.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        con = sqlite3.connect('data/coffee.db')
        cur = con.cursor()

        result = cur.execute("""
        select
        coffee.id,
        sorts.sort,
        roast.degree,
        ground,
        taste,
        price,
        volume
        from
        coffee
        left join sorts on coffee.sort = sorts.id
        left join roast on coffee.roast = roast.id
        """).fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'sort', 'roast', 'ground', 'taste', 'price', 'volume'])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Режим Изменений"))


class Ui_addEditCoffee(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(736, 605)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 681, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.verticalLayout.addWidget(self.spinBox)
        self.loadButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.loadButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 16, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 170, 681, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_3.setGeometry(QtCore.QRect(250, 475, 250, 100))
        font = QtGui.QFont('', 16)
        self.pushButton_3.setFont(font)

        self.sortsButton = QtWidgets.QPushButton(Form)
        self.sortsButton.setObjectName("sortsButton")
        self.sortsButton.setGeometry(QtCore.QRect(100, 475, 100, 100))
        self.sortsButton.setFont(font)
        self.roastButton = QtWidgets.QPushButton(Form)
        self.roastButton.setObjectName("sortsButton")
        self.roastButton.setGeometry(QtCore.QRect(550, 475, 100, 100))
        self.roastButton.setFont(font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'sort', 'roast', 'ground', 'taste', 'price', 'volume'])
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loadButton.setText(_translate("Form", "Загрузить"))
        self.pushButton_2.setText(_translate("Form", "Сохранить"))
        self.label.setText(_translate("Form", "ID:"))
        self.pushButton_3.setText(_translate("Form", "Режим Просмотра"))
        self.sortsButton.setText(_translate("Form", "Сорта"))
        self.roastButton.setText(_translate("Form", "Обжарка"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.secondWindow = None
        self.pushButton.clicked.connect(self.enter_edit_mode)

    def enter_edit_mode(self):
        self.close()
        self.secondWindow = addEditCoffeeForm()
        self.secondWindow.show()


class addEditCoffeeForm(QtWidgets.QWidget, Ui_addEditCoffee):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.secondWindow = None
        self.pushButton_3.clicked.connect(self.enter_view_mode)
        self.loadButton.clicked.connect(self.loadItem)
        self.sortsButton.clicked.connect(self.msg_sorts)
        self.roastButton.clicked.connect(self.msg_roast)

        self.modified = dict()
        self.tableWidget.itemChanged.connect(self.edit_item)
        self.pushButton_2.clicked.connect(self.save_result)


    def enter_view_mode(self):
        self.close()
        self.secondWindow = MyWidget()
        self.secondWindow.show()

    def loadItem(self):
        self.tableWidget.clearContents()
        con = sqlite3.connect("data/coffee.db")
        cur = con.cursor()
        result = cur.execute(f"""
        select * from coffee     
        where coffee.id = {self.spinBox.value()}
        """).fetchall()
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))
        cur.close()
        con.close()

    def msg_sorts(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Sorts")
        msg.setText(
        """
        1 - Экцельса
        2 - Либерика
        3 - Робуста
        4 - Арабика
        """
        )
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def msg_roast(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Ground")
        msg.setText(
        """
        1 - Лёгкая
        2 - Средняя
        3 - Тёмная
        4 - Высшая
        """
        )
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def edit_item(self, item):
        colums = ('id', 'sort', 'roast', 'ground', 'taste', 'price', 'volume')
        self.modified[colums[item.column()]] = item.text()

    def save_result(self):
        if self.modified:
            con = sqlite3.connect('data/coffee.db')
            cur = con.cursor()
            changes = ", ".join([f"{key}='{self.modified.get(key)}'" for key in self.modified.keys()])
            cur.execute(f"""UPDATE coffee SET\n
            {changes}
            WHERE id = {self.spinBox.value()}
            """)
            con.commit()
            cur.close()
            con.close()
            self.modified.clear()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
