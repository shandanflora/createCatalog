# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 356)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_src = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_src.setObjectName("edit_src")
        self.gridLayout.addWidget(self.edit_src, 0, 1, 1, 1)
        self.gen_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gen_btn.setFont(font)
        self.gen_btn.setObjectName("gen_btn")
        self.gridLayout.addWidget(self.gen_btn, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout.addWidget(self.clear_btn, 3, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edit_obj = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_obj.setObjectName("edit_obj")
        self.gridLayout.addWidget(self.edit_obj, 1, 1, 1, 1)
        self.obj_file_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.obj_file_btn.setFont(font)
        self.obj_file_btn.setObjectName("obj_file_btn")
        self.gridLayout.addWidget(self.obj_file_btn, 1, 2, 1, 1)
        self.edit_file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_file_name.setObjectName("edit_file_name")
        self.gridLayout.addWidget(self.edit_file_name, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.src_file_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.src_file_btn.setFont(font)
        self.src_file_btn.setObjectName("src_file_btn")
        self.gridLayout.addWidget(self.src_file_btn, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "生成目录文件"))
        self.gen_btn.setText(_translate("MainWindow", "生成"))
        self.label_2.setText(_translate("MainWindow", "路径："))
        self.clear_btn.setText(_translate("MainWindow", "清空"))
        self.label.setText(_translate("MainWindow", "源文件："))
        self.obj_file_btn.setText(_translate("MainWindow", "选择"))
        self.label_3.setText(_translate("MainWindow", "文件名："))
        self.src_file_btn.setText(_translate("MainWindow", "选择"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
