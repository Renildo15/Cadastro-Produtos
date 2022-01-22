from PyQt5 import uic,QtWidgets
import mysql.connector


banco = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "CADASTRO_PRODUTOS"
)

def main():
	telaMenu.show()
	telaCadastro.close()
	listarDados.close()

def tela_Cadastrar():
	telaCadastro.show()
	telaMenu.close()

def op_Cadastrar():
	codigo = telaCadastro.lineEdit.text()
	nome = telaCadastro.lineEdit_2.text()
	preco = telaCadastro.lineEdit_3.text()
	quantidade = telaCadastro.lineEdit_4.text()
	data_Val = telaCadastro.dateEdit.text()
	data_cad = telaCadastro.dateEdit_2.text()

	categoria = ""


	print("Codigo:",codigo)
	print("Nome:",nome)
	print("Preço:",preco)
	print("Quantidade:",quantidade)
	print("Data de Validade:",data_Val)
	print("Data do Cadastro:",data_cad)


	if telaCadastro.radioButton.isChecked():
		print("Categoria: Produtos de Limpeza")
		categoria = "Produtos de Limpeza"
	elif telaCadastro.radioButton_2.isChecked():
		print("Categoria: Alimento")
		categoria = "Alimento"
	elif telaCadastro.radioButton_3.isChecked():
		print("Categoria: Produtos Diversos")
		categoria = "Produtos Diversos"
	else:
		print("Categoria: Não informado")
		categoria = "Não informado"


	cursor = banco.cursor()
	comando_SQL = "INSERT INTO PRODUTOS(CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA) VALUES(%s,%s,%s,%s,%s,%s,%s)"
	dados = (str(codigo), str(nome), str(preco), str(quantidade), str(data_Val), str(data_cad), categoria)
	cursor.execute(comando_SQL,dados)
	banco.commit()

	telaCadastro.lineEdit.setText("")
	telaCadastro.lineEdit_2.setText("")
	telaCadastro.lineEdit_3.setText("")
	telaCadastro.lineEdit_4.setText("")

	telaCadastro.radioButton.setCheckable(False)
	telaCadastro.radioButton_2.setCheckable(False)
	telaCadastro.radioButton_3.setCheckable(False)

def op_Listar():
	listarDados.show()
	telaMenu.close()

	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM PRODUTOS"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()

	listarDados.tableWidget.setRowCount(len(dados_lidos))
	listarDados.tableWidget.setColumnCount(8)

	for i in range(0, len(dados_lidos)):
		for j in range(0, 8):
			listarDados.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def op_Editar():
	print("Editar")

def op_Excluir():
	print("Excluir")

def op_Imprimir():
	print("Imprimir")

app = QtWidgets.QApplication([])
telaMenu = uic.loadUi("telamenu.ui")
telaCadastro = uic.loadUi("telaCadastro.ui")
listarDados = uic.loadUi("listarDados.ui")


#Menu principal
telaMenu.pushButton_1.clicked.connect(tela_Cadastrar)
telaMenu.pushButton_2.clicked.connect(op_Listar)
telaMenu.pushButton_3.clicked.connect(op_Editar)
telaMenu.pushButton_4.clicked.connect(op_Excluir)
telaMenu.pushButton_5.clicked.connect(op_Imprimir)

#Tela de cadastro

telaCadastro.pushButton_2.clicked.connect(main)
telaCadastro.pushButton.clicked.connect(op_Cadastrar)

#Tela Listar

listarDados.pushButton_2.clicked.connect(main)


telaMenu.show()
app.exec()