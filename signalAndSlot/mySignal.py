"""自定义信号与自定义槽函数"""
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


# 类名用驼峰
class MySignalMySlot(QWidget):
    # 自定义信号
    close_signal = pyqtSignal()

    # 构造函数
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('测试自定义信号与自定义槽函数')
        self.resize(500, 200)

        # 1-定义一个按钮
        my_btn = QPushButton('关闭', self)
        # 2-连接信号与自定义的槽
        my_btn.clicked.connect(self.click_btn)
        # 5-close_signal这个绑定了一个自定义槽
        self.close_signal.connect(self.close_btn)

    # 3-点击了按钮
    def click_btn(self):
        # 4-按钮去发送信号
        self.close_signal.emit()

    # 自定义槽函数
    def close_btn(self):
        # 6-这个自定义的槽再发起关闭
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_signal_window = MySignalMySlot()
    my_signal_window.show()

    sys.exit(app.exec_())


