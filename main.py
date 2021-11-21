import sys
import sqlite3
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.printtt)
        self.pushButton_3.clicked.connect(self.a)
        self.pushButton_2.clicked.connect(self.e)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT name FROM cofe''').fetchall()
        b = []
        for i in result:
            b.append(i[0])
        self.comboBox.addItems(b)
        self.show()

    def e(self):
        ee.show()
        self.hide()

    def a(self):
        aa.show()
        self.hide()

    def o(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT name FROM cofe''').fetchall()
        b = []
        for i in result:
            b.append(i[0])
        self.comboBox.clear()
        self.comboBox.addItems(b)
            
    def printtt(self):
        print(self.comboBox.currentText())
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        a = self.comboBox.currentText()
        result = cur.execute('''SELECT * FROM cofe WHERE name = (?)''', (a,)).fetchall()
        self.plainTextEdit.setPlainText(':')
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText('название:')
        self.plainTextEdit.appendPlainText(str(str(result[0][1]) + '\n'))
        ee.setname(str(result[0][1]))
        self.plainTextEdit.appendPlainText('жарка:')
        self.plainTextEdit.appendPlainText(str(list(['сильная', 'нормальная'])[result[0][2] - 1] + '\n'))
        self.plainTextEdit.appendPlainText('состояние:')
        self.plainTextEdit.appendPlainText(str(list(['порошок', 'зёрна'])[result[0][3] - 1] + '\n'))
        self.plainTextEdit.appendPlainText('вкус:')
        self.plainTextEdit.appendPlainText(str(str(result[0][4]) + '\n'))
        self.plainTextEdit.appendPlainText('цена:')
        self.plainTextEdit.appendPlainText(str(str(result[0][5]) + '\n'))
        self.plainTextEdit.appendPlainText('размер:')
        self.plainTextEdit.appendPlainText(str(str(result[0][6]) + '\n'))
        con.commit()


class Ad(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.savee)
        self.comboBox.addItems(['сильная прожарка', 'обычная прожарка'])
        self.comboBox_2.addItems(['порошок', 'зёрна'])

    def savee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        a = self.lineEdit.text()
        b = ['сильная прожарка', 'обычная прожарка'].index(self.comboBox.currentText())
        c = ['порошок', 'зёрна'].index(self.comboBox_2.currentText()) + 1
        d = self.lineEdit_5.text()
        e = self.lineEdit_6.text()
        f = self.lineEdit_3.text()
        cur.execute('''INSERT INTO cofe (name, garka, sost, vkus, cena, razmer) VALUES (?, ?, ?, ?, ?, ?)''', (a, b, c, d, e, f))
        con.commit()
        ex.show()
        ex.o()
        self.lineEdit_5.setText('')
        self.lineEdit.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_6.setText('')
        self.hide()


class Ed(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.savee)
        self.comboBox.addItems(['сильная прожарка', 'обычная прожарка'])
        self.comboBox_2.addItems(['порошок', 'зёрна'])
        self.name = ''

    def savee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM cofe WHERE name = (?)''', (self.name,)).fetchall()
        a = self.lineEdit.text()
        b = ['сильная прожарка', 'обычная прожарка'].index(self.comboBox.currentText()) + 1
        c = ['порошок', 'зёрна'].index(self.comboBox_2.currentText()) + 1
        d = self.lineEdit_5.text()
        e = self.lineEdit_6.text()
        f = self.lineEdit_3.text()
        print('1')
        cur.execute('''UPDATE cofe SET name = (?), garka = (?), sost = (?), vkus = (?), cena = (?), razmer = (?) WHERE id = (?)''', (a, b, c, d, e, f, result[0][0]))
        print('2')
        con.commit()
        ex.show()
        ex.o()
        self.lineEdit_5.setText('')
        self.lineEdit.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_6.setText('')
        self.hide()
        
    def setname(self, name):
        self.name = name


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    aa = Ad()
    ee = Ed()
    sys.exit(app.exec_())
