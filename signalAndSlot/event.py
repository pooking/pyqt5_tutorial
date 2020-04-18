"""重新实现事件处理函数"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    # 重新实现keyPressEvent
    def keyPressEvent(self, event):
        print(event.key())
        if event.key() != Qt.Key_Escape:
            QDialog.keyPressEvent(self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.exec_()

    sys.exit(app.exec_())
