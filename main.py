# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
#import PyQt5
from PyQt5 import QtWidgets, QtCore

import untitled


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # app = QtWidgets.QApplication(sys.argv)
    # widget = QtWidgets.QWidget()
    # widget.resize(400, 200)
    # widget.setWindowTitle("This is PyQt Widget example")
    # widget.show()
    # exit(app.exec_())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = untitled.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
