import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import editText.mainUi as mainUi

"""
说明：
1 mainCode继承了两个类
2 分别执行了父类的初始化
"""

class mainCode(QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self):
        # 执行父类初始化
        QMainWindow.__init__(self)
        mainUi.Ui_MainWindow.__init__(self)

        # 执行继承的setupUi方法
        self.setupUi(self)

        # 绑定信号
        self.btn_save.clicked.connect(self.on_save)
        self.btn_open.clicked.connect(self.on_open)

    def on_save(self):
        print('on_save')
        FullFileName,_ = QFileDialog.getSaveFileName(self, '文件另存为', r'./', 'TXT (*.txt)')
        set_text = self.txt_view.toPlainText()
        with open(FullFileName, 'wt') as f:
            print(set_text, file=f)

    def on_open(self):
        print('on_open')
        txtStr = ''
        FullFileName, _ = QFileDialog.getOpenFileName(self, '打开', r'./', 'TXT (*.txt)')
        with open(FullFileName, 'rt') as f:
            lines = f.readlines()
            for line in lines:
                txtStr += line
        self.txt_view.setText(txtStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = mainCode()
    md.show()
    sys.exit(app.exec_())
