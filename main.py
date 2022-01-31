from PyQt5 import uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas


banco = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "CADASTRO_PRODUTOS"
)

def gerar_pdf():
	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM PRODUTOS"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()
	y = 0
	pdf = canvas.Canvas("Cadastro_Produtos.pdf")
	pdf.setFont("Times-Bold", 25)
	pdf.drawString(130,800, "PRODUTOS CADASTRADOS:")
	pdf.setFont("Times-Bold", 10)

	pdf.drawString(30,750,"ID")
	pdf.drawString(70,750,"CÓDIGO")
	pdf.drawString(130,750,"NOME")
	pdf.drawString(210,750,"PREÇO")
	pdf.drawString(270,750,"QUANT")
	pdf.drawString(320,750,"D.VALIDADE")
	pdf.drawString(400,750,"D.CADASTRO")
	pdf.drawString(480,750,"CATEGORIA")

	for i in range(0, len(dados_lidos)):
		y = y + 50
		pdf.drawString(30,750 - y, str(dados_lidos[i][0]))
		pdf.drawString(70,750 - y, str(dados_lidos[i][1]))
		pdf.drawString(130,750 - y, str(dados_lidos[i][2]))
		pdf.drawString(210,750 - y, str(dados_lidos[i][3]))
		pdf.drawString(270,750 - y, str(dados_lidos[i][4]))
		pdf.drawString(320,750 - y, str(dados_lidos[i][5]))
		pdf.drawString(400,750 - y, str(dados_lidos[i][6]))
		pdf.drawString(480,750 - y, str(dados_lidos[i][7]))

	pdf.save()
	pdfmensagem.show()

def fechar_Tela():
	pdfmensagem.close()


def main():
	telaMenu.show()
	telaCadastro.close()
	listarDados.close()
	TelaImprimir.close()
	telaEditar.close()
	TelaBusca.close()

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


def op_Buscar():
	TelaBusca.show()
	telaMenu.close()

def Buscar():
	nome =TelaBusca.lineEdit.text()

	if nome == "":
		print("ERRO")

	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE NOME = '{}'".format(nome))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)

		for i in range(0, len(dados_lidos)):
			for j in range(0, 8):
				TelaBusca.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

		TelaBusca.lineEdit.setText("")

def op_Editar():
	telaEditar.show()
	telaMenu.close()

	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM PRODUTOS ORDER BY ID"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()

	telaEditar.tableWidget.setRowCount(len(dados_lidos))
	telaEditar.tableWidget.setColumnCount(8)
	telaEditar.tableWidget.setColumnWidth(0,20)
	telaEditar.tableWidget.setColumnWidth(1,115)
	telaEditar.tableWidget.setColumnWidth(2,125)
	telaEditar.tableWidget.setColumnWidth(3,50)
	telaEditar.tableWidget.setColumnWidth(4,20)
	telaEditar.tableWidget.setColumnWidth(5,125)
	telaEditar.tableWidget.setColumnWidth(6,125)
	telaEditar.tableWidget.setColumnWidth(7,135)


	telaEditar.tableWidget.verticalHeader().setVisible(False)
	telaEditar.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
	telaEditar.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
	telaEditar.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

	for i in range(0, len(dados_lidos)):
		for j in range(0, 8):
			telaEditar.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def Editar():

	global num_id
	edicao.label_10.setText("")
	linha = telaEditar.tableWidget.currentRow()
	id_Produto = telaEditar.tableWidget.item(linha,0).text()

	cursor = banco.cursor()
	cursor.execute("SELECT * FROM PRODUTOS WHERE ID = "+ id_Produto)
	produto = cursor.fetchall()
	edicao.show()

	num_id = id_Produto

	edicao.lineEdit.setText(str(produto[0][0]))
	edicao.lineEdit_2.setText(str(produto[0][1]))
	edicao.lineEdit_3.setText(str(produto[0][2]))
	edicao.lineEdit_4.setText(str(produto[0][3]))
	edicao.lineEdit_5.setText(str(produto[0][4]))
	edicao.lineEdit_6.setText(str(produto[0][5]))
	edicao.lineEdit_7.setText(str(produto[0][6]))
	edicao.lineEdit_8.setText(str(produto[0][7]))

def Salvar():
	global num_id
	codigo = edicao.lineEdit_2.text()
	nome = edicao.lineEdit_3.text()
	preco = edicao.lineEdit_4.text()
	qtd = edicao.lineEdit_5.text()
	dta_val = edicao.lineEdit_6.text()
	dta_cad = edicao.lineEdit_7.text()
	categoria = edicao.lineEdit_8.text()


	if codigo == "" or nome == "" or preco == "" or qtd == "" or categoria == "" or dta_val =="" or dta_cad == "":
		edicao.label_10.setText("*PREENCHA TODOS OS CAMPOS")
	else:
		edicao.label_10.setText("")

		cursor = banco.cursor()
		cursor.execute("UPDATE PRODUTOS SET CODIGO = '{}', NOME = '{}', PRECO = '{}', QUANTIDADE = '{}', DAT_VALIDADE = '{}', DAT_CADASTRO = '{}', CATEGORIA = '{}' WHERE ID  = '{}'".format(codigo, nome, preco, qtd, dta_val, dta_cad, categoria, num_id))
		edicao.close()
		telaEditar.close()
		op_Editar()


def op_Excluir():
	print("Excluir")

def op_Imprimir():
	TelaImprimir.show()
	telaMenu.close()

	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM PRODUTOS"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()

	TelaImprimir.tableWidget.setRowCount(len(dados_lidos))
	TelaImprimir.tableWidget.setColumnCount(8)

	for i in range(0, len(dados_lidos)):
		for j in range(0, 8):
			TelaImprimir.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def Busca_Categoria():
	test =TelaBusca.lineEdit.text()

	if test == "":
		print("ERRO")

	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE CATEGORIA = '{}'".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)

		for i in range(0, len(dados_lidos)):
			for j in range(0, 8):
				TelaBusca.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
		TelaBusca.lineEdit.setText("")
	print("Categoria")

def Busca_dtaVal():
	test =TelaBusca.lineEdit.text()

	if test == "":
		print("ERRO")

	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE DAT_VALIDADE = '{}'".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)

		for i in range(0, len(dados_lidos)):
			for j in range(0, 8):
				TelaBusca.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
		TelaBusca.lineEdit.setText("")
	print("Data Validade")

def Busca_dtaCad():

	test =TelaBusca.lineEdit.text()

	if test == "":
		print("ERRO")

	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE DAT_CADASTRO = '{}'".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)

		for i in range(0, len(dados_lidos)):
			for j in range(0, 8):
				TelaBusca.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
		TelaBusca.lineEdit.setText("")
	print("Data Cadastro")


app = QtWidgets.QApplication([])
telaMenu = uic.loadUi("./Telas/telamenu.ui")
telaCadastro = uic.loadUi("./Telas/telaCadastro.ui")
listarDados = uic.loadUi("./Telas/listarDados.ui")
TelaImprimir = uic.loadUi("./Telas/TelaImprimir.ui")
pdfmensagem = uic.loadUi("./Telas/pdfmensagem.ui")
TelaBusca = uic.loadUi("./Telas/TelaBusca.ui")
telaEditar = uic.loadUi("./Telas/telaEditar.ui")
edicao = uic.loadUi("./Telas/edicao.ui")


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

#Tela imprimir

TelaImprimir.pushButton_3.clicked.connect(main)
TelaImprimir.pushButton_2.clicked.connect(gerar_pdf)
pdfmensagem.pushButton_3.clicked.connect(fechar_Tela)


#Tela Busca

TelaBusca.pushButton.clicked.connect(Buscar)
TelaBusca.pushButton_2.clicked.connect(main)
TelaBusca.pushButton_3.clicked.connect(Busca_Categoria)
TelaBusca.pushButton_4.clicked.connect(Busca_dtaVal)
TelaBusca.pushButton_5.clicked.connect(Busca_dtaCad)


telaMenu.show()
app.exec()