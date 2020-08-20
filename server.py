from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QPushButton, QLabel, QLineEdit, QPlainTextEdit, QFileDialog, QAction , QMessageBox
import sys
import socket

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.title = "EBF Remote access controle"
        self.top = 200
        self.left = 500
        self.width = 631
        self.height = 229
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.label = QtWidgets.QLabel("No connection found", self)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton("config", self)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton("Start", self)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(0,0 ,self)
        self.tableWidget.setGeometry(QtCore.QRect(5, 30, 621, 121))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Ip address")
        self.pushButton.clicked.connect(self.config_server)
        self.pushButton_2.clicked.connect(self.sck)

        self.show()

    def config_server(self):
        self.host = "192.168.145.134"
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter port number:')
        if ok:
            self.port = int(text)
            self.label.setText("Configuration success | Port :" + text)

    def sck(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen()
        self.c, self.addr = self.s.accept()
        self.label.setText("connected")
        item = self.tableWidget.item(0, 0)
        item.setText(str(self.addr))

    def ter(self):
        self.next = Second()
    def th(self):
        self.n = third()
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        newAct = contextMenu.addAction("Terminal")
        openAct = contextMenu.addAction("File manager")
        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == newAct:
            self.c.send("1".encode())
            self.ter()
        if action == openAct:
            self.c.send("2".encode())
            self.th()
        if action == quitAct:
            self.close()
class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.title="Terminal"
        self.initWindow()
    def initWindow(self):

        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.setPlaceholderText("Commande Line")
        self.nameTextbox.setGeometry(QtCore.QRect(10, 10, 411, 31))
        self.button=QPushButton("Send", self)
        self.button.setGeometry(QtCore.QRect(440, 10, 75, 31))
        self.b = QPlainTextEdit(self)
        self.b.setGeometry(QtCore.QRect(10, 50, 521, 291))
        self.button.clicked.connect(self.terminal)
        self.setWindowTitle(self.title)
        self.resize(540, 383)
        self.show()

    def terminal(self):
        self.mssg = self.nameTextbox.text()
        window.c.sendall((self.mssg).encode())
        self.data = window.c.recv(1024)
        print(self.data.decode())
        self.b.insertPlainText(self.data.decode() +"\n")
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            self.commande_boocle = "False"
            window.c.sendall(self.commande_boocle.encode())
            event.accept()
        else:
            event.ignore()    
class third(QMainWindow):
    def __init__(self, parent=None):
        super(third, self).__init__(parent)
        self.title="filemanager"
        self.initWindow()
    def initWindow(self):
        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.setPlaceholderText("File path")
        self.nameTextbox.setGeometry(QtCore.QRect(10, 30, 301, 20))
        
        self.nameTextbox_2 = QLineEdit(self)
        self.nameTextbox_2.setPlaceholderText("File path")
        self.nameTextbox_2.setGeometry(QtCore.QRect(10, 91, 221, 21))
        
        
        self.button=QPushButton("Open", self)
        self.button.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.button.clicked.connect(self.saveFileDialog)
        
        self.label = QtWidgets.QLabel("Target computer", self)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 16))
        self.label.setObjectName("label")
        
        self.button2=QPushButton("Download it", self)
        self.button2.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.button2.clicked.connect(self.filemanager)
        
        
        self.label2 = QtWidgets.QLabel("My computer", self)
        self.label2.setGeometry(QtCore.QRect(10, 70, 301, 16))
        self.label2.setObjectName("label")
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)
        self.setWindowTitle(self.title)
        self.resize(322, 217)
        self.show()
    def filemanager(self):
        self.f_p = self.nameTextbox.text()
        window.c.send(self.f_p.encode())
        self.f = window.c.recv(1024)
        self.f_n = self.nameTextbox_2.text()
        self.n_f = open(self.f_n, 'wb')
        self.n_f.write(self.f)
        self.n_f.close()
        print("Done !")

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.nameTextbox_2.insert(fileName)
            print(fileName)
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            self.filemanager_boocle = "False"
            window.c.sendall(self.filemanager_boocle.encode())
            event.accept()
        else:
            event.ignore()    
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
