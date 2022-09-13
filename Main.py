from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
cartao= uic.loadUi('loto.ui')


cartao.show()
app.exec()