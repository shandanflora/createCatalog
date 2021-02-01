from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from button import *
from createCatalog import *


class WorkThread(QThread):
    signal_info = pyqtSignal()
    signal_bar = pyqtSignal(int)

    def __init__(self, dict_para):
        super().__init__()
        self.dict = dict_para

    def run(self):
        create_catalog.write_excel(self.dict, self.signal_bar)
        self.signal_info.emit()
        pass

# noinspection PyArgumentList


class main_window(QMainWindow):
    # constructor
    def __init__(self, name='Dlg'):
        super().__init__()
        self.label = QLabel()
        self.progressBar = QProgressBar()
        self.ui = Ui_MainWindow()
        self.initUI(name)

    # init function
    def initUI(self, name):
        self.ui.setupUi(self)
        self.statusBar().addPermanentWidget(self.label)
        self.statusBar().addPermanentWidget(self.progressBar)
        # This is simply to show the bar
        # self.progressBar.setGeometry(0, 0, 50, 15)
        self.progressBar.setRange(0, 100)  # 设置进度条的范围
        self.progressBar.setValue(0)
        self.setWindowTitle(name)
        self.initConnect()

    # initial slot and connect
    def initConnect(self):
        self.ui.obj_file_btn.clicked.connect(self.obj_btn_clicked)
        self.ui.src_file_btn.clicked.connect(self.src_btn_clicked)
        self.ui.gen_btn.clicked.connect(self.gen_btn_clicked)
        self.ui.clear_btn.clicked.connect(self.clear_btn_clicked)
        pass

    # ###########################################
    #        slot function
    # ###########################################
    def obj_btn_clicked(self):
        file_name = QFileDialog.getExistingDirectory(self.ui.centralwidget, 'open folder', '/')
        self.ui.edit_obj.setText(file_name)
        # reset style sheet
        self.ui.statusbar.setStyleSheet("0;")
        self.ui.statusbar.setStyleSheet("font-size:15pt;")
        if file_name != "":
            self.ui.statusbar.showMessage("已选择目标路径")

    def src_btn_clicked(self):
        file_name = QFileDialog.getOpenFileName(self.ui.centralwidget, 'open file', '/')
        self.ui.edit_src.setText(file_name[0])
        namelist = file_name[0].split('/')
        file = namelist[len(namelist) - 1]
        if file != "":
            new_file = file[0:file.rfind('.')] + "_目录.xlsx"
            self.ui.edit_file_name.setText(new_file)
            self.ui.statusbar.setStyleSheet("0;")
            self.ui.statusbar.setStyleSheet("font-size:15pt;")
            self.ui.statusbar.showMessage("已选择源文件")

    def gen_btn_clicked(self):
        if self.ui.edit_src.text() == "":
            self.ui.statusbar.setStyleSheet("font-size:15pt;""background-color:#FF0000;")
            self.ui.statusbar.showMessage("源文件不能为空！！！")
        elif self.ui.edit_obj.text() == "":
            self.ui.statusbar.setStyleSheet("font-size:15pt;""background-color:#FF0000;")
            self.ui.statusbar.showMessage("目标路径不能为空！！！")
        elif self.ui.edit_file_name.text() == "":
            self.ui.statusbar.setStyleSheet("font-size:15pt;""background-color:#FF0000;")
            self.ui.statusbar.showMessage("目标文件名不能为空！！！")
        else:
            obj_file = self.ui.edit_obj.text() + "/" + self.ui.edit_file_name.text()
            src_file = self.ui.edit_src.text()
            dict_para = {'src_file': src_file, 'obj_file': obj_file,
                         'bar': self.progressBar, 'label': self.label}
            self.label.setText("正在生成:")
            self.thread = WorkThread(dict_para)
            self.thread.signal_info.connect(self.update_info)
            self.thread.signal_bar.connect(self.update_bar)
            self.thread.start()

    def update_info(self):
        self.label.setText("")
        self.ui.statusbar.showMessage("已生成目录文件")
        self.progressBar.setValue(100)

    def update_bar(self, value):
        self.progressBar.setValue(value)
        pass

    def clear_btn_clicked(self):
        self.ui.statusbar.setStyleSheet("0;")
        self.ui.statusbar.setStyleSheet("font-size:15pt;")
        self.ui.statusbar.showMessage("清空编辑框")
        self.ui.edit_src.setText("")
        self.ui.edit_obj.setText("")
        self.ui.edit_file_name.setText("")
