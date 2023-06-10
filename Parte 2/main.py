from PyQt5 import uic, QtWidgets
import sqlite3 as sql

def logar():
    primTela.msg_erro.setText('')
    user = primTela.login.text()
    password = primTela.senha.text()
    if user == 'admin_Luca' and password == '12345678':
        primTela.close()
        segTela.show()
    else:
        primTela.msg_erro.setText('Usuário ou senha errado(s). Tente novamente')


def deslogar():
    segTela.close()
    primTela.show()


def abrir_tela_cadastro():
    primTela.msg_erro.setText('')
    primTela.close()
    telaCadastro.show()


def voltar_home():
    telaCadastro.close()
    primTela.show()


def cadastrar():
    nome = telaCadastro.dado_nome.text()
    sobrenome = telaCadastro.dado_sobrenome.text()
    login = telaCadastro.login.text()
    senha = telaCadastro.senha.text()
    c_senha = telaCadastro.confirma_senha.text()

    if senha == c_senha:
        try:
            banco = sql.connect('banco_cadastro.db')
            cursor = banco.cursor()

            cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, sobrenome text, login text, senha text)')
            cursor.execute(f'INSERT INTO cadastro VALUES ("{nome}", "{sobrenome}", "{login}", "{senha}")')

            banco.commit()
            banco.close()

            telaCadastro.msg_for_user.setText('Cadastro bem sucedido!')
            telaCadastro.msg_for_user.move(182, 320)
            telaCadastro.msg_for_user.resize(121, 21)

        except sql.Error as erro:
            print(f'Erro ao inserir os dados: {erro}')
            telaCadastro.msg_for_user.setText('Cadastro mal sucedido!')
            telaCadastro.msg_for_user.move(182, 320)
            telaCadastro.msg_for_user.resize(121, 21)
    else:
        telaCadastro.msg_for_user.setText('As senhas digitadas estão diferentes. Verifique e tente novamente')
        telaCadastro.msg_for_user.move(81, 320)
        telaCadastro.msg_for_user.resize(322, 21)


app = QtWidgets.QApplication([])
telaCadastro = uic.loadUi('janelaCadastro.ui')
primTela = uic.loadUi('primeiraJanela.ui')
segTela = uic.loadUi('segundaJanela.ui')

primTela.senha.setEchoMode(QtWidgets.QLineEdit.Password)
primTela.botao_entrar.clicked.connect(logar)
primTela.botao_cadastre.clicked.connect(abrir_tela_cadastro)

segTela.botao_sair.clicked.connect(deslogar)

telaCadastro.senha.setEchoMode(QtWidgets.QLineEdit.Password)
telaCadastro.confirma_senha.setEchoMode(QtWidgets.QLineEdit.Password)
telaCadastro.botao_voltar.clicked.connect(voltar_home)
telaCadastro.enviar_dados.clicked.connect(cadastrar)

primTela.show()
app.exec()
