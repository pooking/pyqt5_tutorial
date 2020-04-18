"""使用lambda、partial传递参数"""
import sys
from functools import partial
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


class LambdaOrPartial(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 定义两个按钮
        btn1 = QPushButton('Button 1', self)
        btn2 = QPushButton('Button 2', self)
        btn11 = QPushButton('Button 11', self)
        btn21 = QPushButton('Button 21', self)

        # 设置布局
        layout = QHBoxLayout()
        # 添加到布局
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn11)
        layout.addWidget(btn21)
        # 把布局添加到窗口
        self.setLayout(layout)

        # 设置窗口
        self.setWindowTitle('使用lambda, partial来传递参数')
        self.resize(400, 300)

        # lambda
        btn1.clicked.connect(lambda: self.on_button_clicked(1))
        btn2.clicked.connect(lambda: self.on_button_clicked(2))

        # partial
        btn11.clicked.connect(partial(self.on_button_clicked, 11))
        btn21.clicked.connect(partial(self.on_button_clicked, 21))

    def on_button_clicked(self, n):
        print("Button{0} is clicked.".format(n))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    my_lambda_partial_window = LambdaOrPartial()
    my_lambda_partial_window.show()

    sys.exit(app.exec_())