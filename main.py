from PyQt5 import uic,QtWidgets


def op_Cadastrar():
	print("Cadastrar")

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
telaMenu.pushButton.clicked.connect(op_Cadastrar)
telaMenu.pushButton_2.clicked.connect(op_Listar)
telaMenu.pushButton_3.clicked.connect(op_Editar)
telaMenu.pushButton_4.clicked.connect(op_Excluir)
telaMenu.pushButton_5.clicked.connect(op_Imprimir)

telaMenu.show()
app.exec()