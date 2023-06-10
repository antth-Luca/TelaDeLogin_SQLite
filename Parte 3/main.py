from PyQt5 import uic, QtWidgets
import sqlite3 as sql


def logar():
    login = primTela.login.text()
    senha = primTela.senha.text()
    try:            # Tentando conectar ao banco
        banco = sql.connect('banco_cadastro.db')
        cursor = banco.cursor()
    except:
        primTela.msg_erro.setText('Sem conexão com o banco de dados')
    else:
        try:     # Validando usuário
            cursor.execute(f'SELECT senha FROM cadastro WHERE login = "{login}" IF EXISTS login = "{login}"')
            senha_bd = cursor.fetchall()

            banco.close()
        except:
            primTela.msg_erro.setText('Usuário incorreto')
        else:
            try:   # Validando senha
                senha == senha_bd[0][0]
            except:
                primTela.msg_erro.setText('Senha incorreta')
            else:       # Abrindo segunda tela
                segTela.msg_logado.setText(f'{login} está logado')
                primTela.close()
                segTela.show()


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
    # Pegando dados digitados pelo usuário
    nome = telaCadastro.dado_nome.text()
    sobrenome = telaCadastro.dado_sobrenome.text()
    login = telaCadastro.login.text()
    senha = telaCadastro.senha.text()
    c_senha = telaCadastro.confirma_senha.text()
    # Validando senha
    if senha == c_senha:
        try:
            # Tentando conexão com o banco
            banco = sql.connect('banco_cadastro.db')
            cursor = banco.cursor()
            # Verificando existencia da tabela, se existir faz o registro e se não cria a tabela e faz o registro
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
    else:     # Falha na confirmação da senha
        telaCadastro.msg_for_user.setText('As senhas digitadas estão diferentes. Verifique e tente novamente')
        telaCadastro.msg_for_user.move(81, 320)
        telaCadastro.msg_for_user.resize(322, 21)


# Preparando para a execução
app = QtWidgets.QApplication([])
telaCadastro = uic.loadUi('janelaCadastro.ui')
primTela = uic.loadUi('primeiraJanela.ui')
segTela = uic.loadUi('segundaJanela.ui')

# Configuração dos elementos da primeira tela
primTela.senha.setEchoMode(QtWidgets.QLineEdit.Password)
primTela.botao_entrar.clicked.connect(logar)
primTela.botao_cadastre.clicked.connect(abrir_tela_cadastro)
# Configuração dos elementos da segunda tela
segTela.botao_sair.clicked.connect(deslogar)
# Configuração dos elementos da tela de cadastro
telaCadastro.senha.setEchoMode(QtWidgets.QLineEdit.Password)
telaCadastro.confirma_senha.setEchoMode(QtWidgets.QLineEdit.Password)
telaCadastro.botao_voltar.clicked.connect(voltar_home)
telaCadastro.enviar_dados.clicked.connect(cadastrar)

# Execução
primTela.show()
app.exec()
