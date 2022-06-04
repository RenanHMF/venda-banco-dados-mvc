# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formPedido.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

from Controller.PedidoController import PedidoController

class Ui_MainWindow(object):

    def __init__(self):
        self.pedidoController = PedidoController()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcluir.setGeometry(QtCore.QRect(250, 190, 75, 23))
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(90, 190, 75, 23))
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.btnConsultar.setObjectName("btnConsultar")
        self.edtQuantidade = QtWidgets.QLineEdit(self.centralwidget)
        self.edtQuantidade.setGeometry(QtCore.QRect(80, 70, 381, 21))
        self.edtQuantidade.setObjectName("edtQuantidade")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.label_4.setObjectName("label_4")
        self.edtValorTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.edtValorTotal.setGeometry(QtCore.QRect(80, 100, 171, 20))
        self.edtValorTotal.setObjectName("edtValorTotal")
        self.btnAtualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtualizar.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.edtId = QtWidgets.QLineEdit(self.centralwidget)
        self.edtId.setGeometry(QtCore.QRect(80, 10, 111, 20))
        self.edtId.setObjectName("edtId")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_5.setObjectName("label_5")
        self.edtProduto = QtWidgets.QLineEdit(self.centralwidget)
        self.edtProduto.setGeometry(QtCore.QRect(80, 130, 171, 20))
        self.edtProduto.setObjectName("edtProduto")
        self.edtCliente = QtWidgets.QLineEdit(self.centralwidget)
        self.edtCliente.setGeometry(QtCore.QRect(80, 160, 171, 20))
        self.edtCliente.setText("")
        self.edtCliente.setObjectName("edtCliente")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.label_6.setObjectName("label_6")
        self.edtData = QtWidgets.QDateEdit(self.centralwidget)
        self.edtData.setGeometry(QtCore.QRect(80, 40, 110, 22))
        self.edtData.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 6, 4), QtCore.QTime(0, 0, 0)))
        self.edtData.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 5, 30), QtCore.QTime(0, 0, 0)))
        self.edtData.setMinimumDate(QtCore.QDate(2022, 5, 30))
        self.edtData.setObjectName("edtData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.edtValorTotal.setEnabled(False)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnCadastrar.clicked.connect(self.cadastrar)
        self.btnAtualizar.clicked.connect(self.atualizar)
        self.btnExcluir.clicked.connect(self.excluir)

    def consultar(self):
        dados = self.pedidoController.consultar(int(self.edtId.text()))
        if dados:
            ano, mes, dia = dados[1].split('-')
            self.edtData.setDateTime(QtCore.QDateTime(QtCore.QDate(int(ano), int(mes), int(dia)), QtCore.QTime(0, 0, 0)))
            self.edtQuantidade.setText(dados[2])
            self.edtValorTotal.setText(dados[3])
            self.edtProduto.setText(dados[4])
            self.edtCliente.setText(dados[5])
            self.edtProduto.setEnabled(False)
            self.edtCliente.setEnabled(False)
            print("Consultado valores!")
        else:
            diaAtual = str(datetime.date.today())
            ano, mes, dia = diaAtual.split('-')
            self.edtData.setDateTime(QtCore.QDateTime(QtCore.QDate(int(ano), int(mes), int(dia)), QtCore.QTime(0, 0, 0)))
            self.edtQuantidade.setText('')
            self.edtValorTotal.setText('')
            self.edtProduto.setText('')
            self.edtCliente.setText('')
            self.edtProduto.setEnabled(True)
            self.edtCliente.setEnabled(True)
            print("Não foi possivel consultar Pedido!")

    def cadastrar(self):
        if self.pedidoController.cadastrar(int(self.edtId.text()),
                                           self.edtData.date().toPyDate(),
                                           int(self.edtQuantidade.text()),
                                           int(self.edtProduto.text()),
                                           int(self.edtCliente.text())):
            diaAtual = str(datetime.date.today())
            ano, mes, dia = diaAtual.split('-')
            print('Pedido cadastrado!')

            self.edtId.setText('')
            self.edtData.setDateTime(QtCore.QDateTime(QtCore.QDate(int(ano), int(mes), int(dia)), QtCore.QTime(0, 0, 0)))
            self.edtQuantidade.setText('')
            self.edtValorTotal.setText('')
            self.edtProduto.setText('')
            self.edtCliente.setText('')

        else:
            self.edtId.setText('')
            print('Erro ao cadastrar Pedido!')

    def atualizar(self):
        if self.pedidoController.atualizar(str(self.edtId.text()),
                                           self.edtData.date().toPyDate(),
                                           str(self.edtQuantidade.text()),
                                           str(self.edtValorTotal.text())):
            print('Pedido atualizado!')
            diaAtual = str(datetime.date.today())
            ano, mes, dia = diaAtual.split('-')
            self.edtId.setText('')
            self.edtData.setDateTime(QtCore.QDateTime(QtCore.QDate(int(ano), int(mes), int(dia)), QtCore.QTime(0, 0, 0)))
            self.edtQuantidade.setText('')
            self.edtValorTotal.setText('')
            self.edtProduto.setText('')
            self.edtCliente.setText('')
        else:
            print('Erro ao atualizar Pedido!')

    def excluir(self):
        if self.pedidoController.excluir(self.edtId.text()):
            print('Cliente excluído!')
            diaAtual = str(datetime.date.today())
            ano, mes, dia = diaAtual.split('-')
            self.edtId.setText('')
            self.edtData.setDateTime(QtCore.QDateTime(QtCore.QDate(int(ano), int(mes), int(dia)), QtCore.QTime(0, 0, 0)))
            self.edtQuantidade.setText('')
            self.edtValorTotal.setText('')
            self.edtProduto.setText('')
            self.edtCliente.setText('')
        else:
            print('Erro ao excluir Pedido!')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnExcluir.setText(_translate("MainWindow", "Excluir"))
        self.btnCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.btnConsultar.setText(_translate("MainWindow", "Consultar"))
        self.label_4.setText(_translate("MainWindow", "Valor Total"))
        self.btnAtualizar.setText(_translate("MainWindow", "Atualizar"))
        self.label.setText(_translate("MainWindow", "Código"))
        self.label_3.setText(_translate("MainWindow", "Quantidade"))
        self.label_2.setText(_translate("MainWindow", "Data"))
        self.label_5.setText(_translate("MainWindow", "Produto"))
        self.label_6.setText(_translate("MainWindow", "Cliente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
