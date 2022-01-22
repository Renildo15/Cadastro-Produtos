from PyQt5 import uic,QtWidgets

def main():
	telaMenu.show()
	telaCadastro.close()


def op_Cadastrar():
	telaCadastro.show()
	telaMenu.close()

def op_Listar():
	print("Listar")

def op_Editar():
	print("Editar")

def op_Excluir():
	print("Excluir")

def op_Imprimir():
	print("Imprimir")

app = QtWidgets.QApplication([])
telaMenu = uic.loadUi("telamenu.ui")
telaCadastro = uic.loadUi("telaCadastro.ui")


#Menu principal
telaMenu.pushButton.clicked.connect(op_Cadastrar)
telaMenu.pushButton_2.clicked.connect(op_Listar)
telaMenu.pushButton_3.clicked.connect(op_Editar)
telaMenu.pushButton_4.clicked.connect(op_Excluir)
telaMenu.pushButton_5.clicked.connect(op_Imprimir)

#Tela de cadastro

telaCadastro.pushButton_2.clicked.connect(main)

telaMenu.show()
app.exec()