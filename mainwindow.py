from button import *
from PyQt5.QtWidgets import *
from createCatalog import *

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
        self.label.setText("正在生成：")
        self.statusBar().addPermanentWidget(self.label)
        self.statusBar().addPermanentWidget(self.progressBar)
        # This is simply to show the bar
        self.progressBar.setGeometry(0, 0, 100, 5)
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
            file = self.ui.edit_obj.text() + "/" + self.ui.edit_file_name.text()
            create_catalog.write_excel(file, create_catalog.read_excel(self.ui.edit_src.text()))
            self.ui.statusbar.showMessage("已生成目录文件！！！！")

    def clear_btn_clicked(self):
        self.ui.statusbar.setStyleSheet("0;")
        self.ui.statusbar.setStyleSheet("font-size:15pt;")
        self.ui.statusbar.showMessage("清空编辑框")
        self.ui.edit_src.setText("")
        self.ui.edit_obj.setText("")
        self.ui.edit_file_name.setText("")
