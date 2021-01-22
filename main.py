from mainwindow import *

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = main_window("生成目录")
    window.show()
    sys.exit(app.exec_())

