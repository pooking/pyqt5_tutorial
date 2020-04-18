"""通过装饰符绑定事件"""
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        button1 = QPushButton('Button1', self)
        button2 = QPushButton('Button2', self)
        button1.setObjectName('Button1')
        button2.setObjectName('Button2')

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)

        self.setWindowTitle('装饰符绑定事件')
        self.resize(400, 300)

        # 设置窗口中的所有元素，通过name连接槽函数
        QtCore.QMetaObject.connectSlotsByName(self)

    """
    这里是修饰符的用法
    如：
    @foo()
    def bar(): pass
    表示如下：
    bar = foo()(bar)
    
    所以下面的可以写成：
    def on_Button1_clicked(self):
        print('Button1 is clicked.')
    on_Button1_clicked = QtCore.pyqtSlot()(on_Button1_clicked)
    """
    @QtCore.pyqtSlot()
    def on_Button1_clicked(self):
        print('Button1 is clicked.')

    @QtCore.pyqtSlot()
    def on_Button2_clicked(self):
        print('Button2 is clicked.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())