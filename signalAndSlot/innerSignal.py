"""内置信号与槽函数"""
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class InnerSignal(QWidget):
    # 自定义关闭的信号
    close_signal = pyqtSignal()

    # 初始化这个类
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('测试内置槽函数')
        self.resize(400, 300)

        # 定义一个按钮
        btn = QPushButton("关闭", self)
        # 连接内置信号与自定义槽函数
        btn.clicked.connect(self.on_close)
        # 连接自定义信号与内置槽self.close
        self.close_signal.connect(self.close)

    # 自定义的槽函数
    def on_close(self):
        # 发送信号
        self.close_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 实例化一个类
    my_btn_window = InnerSignal()
    my_btn_window.show()

    # close
    sys.exit(app.exec_())