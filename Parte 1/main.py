from PyQt5 import uic, QtWidgets

def enviando():
    primTela.label_2.setText('')
    user = primTela.lineEdit.text()
    password = primTela.lineEdit_3.text()
    if user == 'admin_Luca' and password == '12345678':
        primTela.close()
        segTela.show()
    else:
        primTela.label_2.setText('Usuário ou senha errado(s). Tente novamente')


def saindo():
    segTela.close()
    primTela.show()


app = QtWidgets.QApplication([])
primTela = uic.loadUi('primeiraJanela.ui')
segTela = uic.loadUi('segundaJanela.ui')

primTela.pushButton.clicked.connect(enviando)
segTela.pushButton.clicked.connect(saindo)

primTela.show()
app.exec()
