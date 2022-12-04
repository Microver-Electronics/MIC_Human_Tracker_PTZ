from PyQt5 import uic

with open("./gui/mainwindow.py", "w", encoding="utf-8") as fout:
    uic.compileUi('./gui/mainwindow.ui', fout)