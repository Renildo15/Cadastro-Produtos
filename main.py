from PyQt5 import uic,QtWidgets
import mysql.connector

def main():
	telaMenu.show()
	telaCadastro.close()


def op_Cadastrar():
	telaCadastro.show()
	telaMenu.close()

	codigo = telaCadastro.lineEdit.text()
	nome = telaCadastro.lineEdit_2.text()
	preco = telaCadastro.lineEdit_3.text()
	quantidade = telaCadastro.lineEdit_4.text()
	data_Val = telaCadastro.dateEdit.text()
	data_cad = telaCadastro.dateEdit_2.text()


	print("Codigo:",codigo)
	print("Nome:",nome)
	print("Preço:",preco)
	print("Quantidade:",quantidade)
	print("Data de Validade:",data_Val)
	print("Data do Cadastro:",data_cad)


	if telaCadastro.radioButton.isChecked():
		print("Categoria: Produtos de Limpeza")
	elif telaCadastro.radioButton_2.isChecked():
		print("Categoria: Alimento")
	elif telaCadastro.radioButton_3.isChecked():
		print("Categoria: Produtos Diversos")
	else:
		print("Categoria: Não informado")

	

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
telaMenu.pushButton_1.clicked.connect(op_Cadastrar)
telaMenu.pushButton_2.clicked.connect(op_Listar)
telaMenu.pushButton_3.clicked.connect(op_Editar)
telaMenu.pushButton_4.clicked.connect(op_Excluir)
telaMenu.pushButton_5.clicked.connect(op_Imprimir)

#Tela de cadastro

telaCadastro.pushButton_2.clicked.connect(main)
telaCadastro.pushButton.clicked.connect(op_Cadastrar)


telaMenu.show()
app.exec()