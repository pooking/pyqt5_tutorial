"""操作信号"""
import sys
from PyQt5.QtCore import pyqtSignal, QCoreApplication, QObject


class SignalAndSlot(QObject):
    # 定义信号
    data_changed = pyqtSignal(str, str, name='data_changed')

    # 更新信号
    def update(self):
        self.data_changed.emit('old signal', 'new signal')

    # 定义槽函数
    def on_data_changed(self, old, new):
        print(old, new)


if __name__ == '__main__':
    app = QCoreApplication(sys.argv)

    item = SignalAndSlot()
    # 信息 - 槽
    item.data_changed.connect(item.on_data_changed)
    item.update()

    sys.exit(app.exec_())