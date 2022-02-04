from PyQt5 import uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

num_id = 0

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
	telaExcluir.close()
	telaEditar.close()
	TelaBusca.close()


def tela_Cadastrar():
	telaCadastro.show()
	telaMenu.close()

	telaCadastro.label_9.setText("")
	telaCadastro.label_10.setText("")
	telaCadastro.label_11.setText("")
	telaCadastro.label_12.setText("")

	telaCadastro.label_13.setText("")

def op_Cadastrar():
	codigo = telaCadastro.lineEdit.text()
	nome = telaCadastro.lineEdit_2.text()
	preco = telaCadastro.lineEdit_3.text()
	quantidade = telaCadastro.lineEdit_4.text()
	data_Val = telaCadastro.dateEdit.text()
	data_cad = telaCadastro.dateEdit_2.text()

	categoria = ""

	if codigo == "" or  nome == "" or preco == "" or quantidade == "":
		telaCadastro.label_9.setText("*INFORME O CÓDIGO!")
		telaCadastro.label_10.setText("*INFORME O NOME!")
		telaCadastro.label_11.setText("*INFORME O PREÇO!")
		telaCadastro.label_12.setText("*INFORME A QUANTIDADE!")
		print("ERRO!")
	else:

		telaCadastro.label_9.setText("")
		telaCadastro.label_10.setText("")
		telaCadastro.label_11.setText("")
		telaCadastro.label_12.setText("")

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
		elif telaCadastro.radioButton_4.isChecked():
			print("Categoria: Bebidas")
			categoria = "Bebidas"
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

		telaCadastro.label_13.setText("CADASTRADO COM SUCESSO!")

def op_Listar():
	listarDados.show()
	telaMenu.close()

	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM PRODUTOS ORDER BY ID"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()

	listarDados.tableWidget.setRowCount(len(dados_lidos))
	listarDados.tableWidget.setColumnCount(8)
	listarDados.tableWidget.setColumnWidth(0,20)
	listarDados.tableWidget.setColumnWidth(1,115)
	listarDados.tableWidget.setColumnWidth(2,125)
	listarDados.tableWidget.setColumnWidth(3,50)
	listarDados.tableWidget.setColumnWidth(4,20)
	listarDados.tableWidget.setColumnWidth(5,125)
	listarDados.tableWidget.setColumnWidth(6,125)
	listarDados.tableWidget.setColumnWidth(7,135)

	listarDados.tableWidget.verticalHeader().setVisible(False)
	listarDados.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
	listarDados.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
	listarDados.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

	for i in range(0, len(dados_lidos)):
		for j in range(0, 8):
			listarDados.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

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

########################Função Excluir##############################
def op_Excluir():

	telaExcluir.show()
	telaMenu.close()

	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM PRODUTOS ORDER BY ID"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()

	telaExcluir.tableWidget.setRowCount(len(dados_lidos))
	telaExcluir.tableWidget.setColumnCount(8)
	telaExcluir.tableWidget.setColumnWidth(0,20)
	telaExcluir.tableWidget.setColumnWidth(1,115)
	telaExcluir.tableWidget.setColumnWidth(2,125)
	telaExcluir.tableWidget.setColumnWidth(3,50)
	telaExcluir.tableWidget.setColumnWidth(4,20)
	telaExcluir.tableWidget.setColumnWidth(5,125)
	telaExcluir.tableWidget.setColumnWidth(6,125)
	telaExcluir.tableWidget.setColumnWidth(7,135)


	telaExcluir.tableWidget.verticalHeader().setVisible(False)
	telaExcluir.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
	telaExcluir.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
	telaExcluir.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

	for i in range(0, len(dados_lidos)):
		for j in range(0, 8):
			telaExcluir.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def Excluir():
	linha = telaExcluir.tableWidget.currentRow()
	id_Produto = telaExcluir.tableWidget.item(linha,0).text()
	cursor = banco.cursor()
	cursor.execute("DELETE FROM PRODUTOS WHERE ID = "+ id_Produto)
	telaExcluir.tableWidget.removeRow(linha)

#####################################################################################

#############################Função Imprimir#########################################

def op_Imprimir():
	TelaImprimir.show()
	telaMenu.close()

	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM PRODUTOS ORDER BY ID"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()

	TelaImprimir.tableWidget.setRowCount(len(dados_lidos))
	TelaImprimir.tableWidget.setColumnCount(8)
	TelaImprimir.tableWidget.setColumnWidth(0,20)
	TelaImprimir.tableWidget.setColumnWidth(1,115)
	TelaImprimir.tableWidget.setColumnWidth(2,125)
	TelaImprimir.tableWidget.setColumnWidth(3,50)
	TelaImprimir.tableWidget.setColumnWidth(4,20)
	TelaImprimir.tableWidget.setColumnWidth(5,125)
	TelaImprimir.tableWidget.setColumnWidth(6,125)
	TelaImprimir.tableWidget.setColumnWidth(7,135)


	TelaImprimir.tableWidget.verticalHeader().setVisible(False)
	TelaImprimir.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
	TelaImprimir.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
	TelaImprimir.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

	for i in range(0, len(dados_lidos)):
		for j in range(0, 8):
			TelaImprimir.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

###########################################################################################################

#############################################Função Buscar###################################################

def op_Buscar():
	TelaBusca.show()
	telaMenu.close()


def Buscar():
	test =TelaBusca.lineEdit.text()

	if test == "":
		print("ERRO")

	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE NOME LIKE '{}%' ORDER BY ID".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)
		TelaBusca.tableWidget.setColumnWidth(0,20)
		TelaBusca.tableWidget.setColumnWidth(1,115)
		TelaBusca.tableWidget.setColumnWidth(2,125)
		TelaBusca.tableWidget.setColumnWidth(3,50)
		TelaBusca.tableWidget.setColumnWidth(4,20)
		TelaBusca.tableWidget.setColumnWidth(5,125)
		TelaBusca.tableWidget.setColumnWidth(6,125)
		TelaBusca.tableWidget.setColumnWidth(7,135)


		TelaBusca.tableWidget.verticalHeader().setVisible(False)
		TelaBusca.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		TelaBusca.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		TelaBusca.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

		for i in range(0, len(dados_lidos)):
			for j in range(0, 8):
				TelaBusca.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

		TelaBusca.lineEdit.setText("")

def Buscar_Tela_Editar():
	test =telaEditar.lineEdit.text()

	if test == "":
		print("ERRO")

	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE ID = '{}'".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

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

		telaEditar.lineEdit.setText("")

def Buscar_Tela_Excluir():
	id_produto = telaExcluir.lineEdit.text()
	if id_produto == "":
		print("ERRO!")
	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID, CODIGO, NOME, PRECO, QUANTIDADE, DAT_VALIDADE, DAT_CADASTRO, CATEGORIA FROM PRODUTOS WHERE ID ='{}'".format(id_produto))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)


		telaExcluir.tableWidget.setRowCount(len(dados_lidos))
		telaExcluir.tableWidget.setColumnCount(8)
		telaExcluir.tableWidget.setColumnWidth(0,20)
		telaExcluir.tableWidget.setColumnWidth(1,115)
		telaExcluir.tableWidget.setColumnWidth(2,125)
		telaExcluir.tableWidget.setColumnWidth(3,50)
		telaExcluir.tableWidget.setColumnWidth(4,20)
		telaExcluir.tableWidget.setColumnWidth(5,125)
		telaExcluir.tableWidget.setColumnWidth(6,125)
		telaExcluir.tableWidget.setColumnWidth(7,135)


		telaExcluir.tableWidget.verticalHeader().setVisible(False)
		telaExcluir.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		telaExcluir.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		telaExcluir.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

		for i in range(0, len(dados_lidos)):
			for j in range(0, 8):
				telaExcluir.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
				valor_id = id_produto




def Busca_Categotia():
	test =TelaBusca.lineEdit.text()

	if test == "":
		print("ERRO")

	else:
		cursor = banco.cursor()
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE CATEGORIA LIKE '{}%' ORDER BY ID".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)
		TelaBusca.tableWidget.setColumnWidth(0,20)
		TelaBusca.tableWidget.setColumnWidth(1,115)
		TelaBusca.tableWidget.setColumnWidth(2,125)
		TelaBusca.tableWidget.setColumnWidth(3,50)
		TelaBusca.tableWidget.setColumnWidth(4,20)
		TelaBusca.tableWidget.setColumnWidth(5,125)
		TelaBusca.tableWidget.setColumnWidth(6,125)
		TelaBusca.tableWidget.setColumnWidth(7,135)


		TelaBusca.tableWidget.verticalHeader().setVisible(False)
		TelaBusca.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		TelaBusca.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		TelaBusca.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

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
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE DAT_VALIDADE LIKE '{}%' ORDER BY ID".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)
		TelaBusca.tableWidget.setColumnWidth(0,20)
		TelaBusca.tableWidget.setColumnWidth(1,115)
		TelaBusca.tableWidget.setColumnWidth(2,125)
		TelaBusca.tableWidget.setColumnWidth(3,50)
		TelaBusca.tableWidget.setColumnWidth(4,20)
		TelaBusca.tableWidget.setColumnWidth(5,125)
		TelaBusca.tableWidget.setColumnWidth(6,125)
		TelaBusca.tableWidget.setColumnWidth(7,135)


		TelaBusca.tableWidget.verticalHeader().setVisible(False)
		TelaBusca.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		TelaBusca.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		TelaBusca.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")
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
		comando_SQL = ("SELECT ID,CODIGO,NOME,PRECO,QUANTIDADE,DAT_VALIDADE,DAT_CADASTRO,CATEGORIA FROM PRODUTOS WHERE DAT_CADASTRO LIKE '{}%' ORDER BY ID".format(test))
		cursor.execute(comando_SQL)
		dados_lidos = cursor.fetchall()
		print(dados_lidos)

		TelaBusca.tableWidget.setRowCount(len(dados_lidos))
		TelaBusca.tableWidget.setColumnCount(8)
		TelaBusca.tableWidget.setColumnWidth(0,20)
		TelaBusca.tableWidget.setColumnWidth(1,115)
		TelaBusca.tableWidget.setColumnWidth(2,125)
		TelaBusca.tableWidget.setColumnWidth(3,50)
		TelaBusca.tableWidget.setColumnWidth(4,20)
		TelaBusca.tableWidget.setColumnWidth(5,125)
		TelaBusca.tableWidget.setColumnWidth(6,125)
		TelaBusca.tableWidget.setColumnWidth(7,135)

		
		TelaBusca.tableWidget.verticalHeader().setVisible(False)
		TelaBusca.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		TelaBusca.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		TelaBusca.tableWidget.setStyleSheet("QTableView {selection-background-color:black;background-color:white;}")

		for i in range(0, len(dados_lidos)):
			for j in range(0, 8):
				TelaBusca.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
		TelaBusca.lineEdit.setText("")
	print("Data Cadastro")


###################################################################################################################################


app = QtWidgets.QApplication([])
telaMenu = uic.loadUi("./Telas/telamenu.ui")
telaCadastro = uic.loadUi("./Telas/telaCadastro.ui")
listarDados = uic.loadUi("./Telas/listarDados.ui")
TelaImprimir = uic.loadUi("./Telas/TelaImprimir.ui")
pdfmensagem = uic.loadUi("./Telas/pdfmensagem.ui")
telaExcluir = uic.loadUi("./Telas/telaExcluir.ui")
telaEditar = uic.loadUi("./Telas/telaEditar.ui")
edicao = uic.loadUi("./Telas/edicao.ui")
TelaBusca = uic.loadUi("./Telas/TelaBusca.ui")


#Menu principal
telaMenu.pushButton_1.clicked.connect(tela_Cadastrar)
telaMenu.pushButton_2.clicked.connect(op_Listar)
telaMenu.pushButton_3.clicked.connect(op_Editar)
telaMenu.pushButton_4.clicked.connect(op_Excluir)
telaMenu.pushButton_5.clicked.connect(op_Imprimir)
telaMenu.pushButton_6.clicked.connect(op_Buscar)

#Tela de cadastro

telaCadastro.pushButton_2.clicked.connect(main)
telaCadastro.pushButton.clicked.connect(op_Cadastrar)

#Tela Listar

listarDados.pushButton_2.clicked.connect(main)

#Tela imprimir

TelaImprimir.pushButton_3.clicked.connect(main)
TelaImprimir.pushButton_2.clicked.connect(gerar_pdf)
pdfmensagem.pushButton_3.clicked.connect(fechar_Tela)

#Tela excluir

telaExcluir.pushButton_3.clicked.connect(main)
telaExcluir.pushButton_2.clicked.connect(Excluir)
telaExcluir.pushButton.clicked.connect(Buscar_Tela_Excluir)

#Tela editar

telaEditar.pushButton_3.clicked.connect(main)
telaEditar.pushButton_2.clicked.connect(Editar)
edicao.pushButton.clicked.connect(Salvar)
telaEditar.pushButton.clicked.connect(Buscar_Tela_Editar)

#Tela Busca

TelaBusca.pushButton.clicked.connect(Buscar)
TelaBusca.pushButton_2.clicked.connect(main)
TelaBusca.pushButton_3.clicked.connect(Busca_Categotia)
TelaBusca.pushButton_4.clicked.connect(Busca_dtaVal)
TelaBusca.pushButton_5.clicked.connect(Busca_dtaCad)

telaMenu.show()
app.exec()