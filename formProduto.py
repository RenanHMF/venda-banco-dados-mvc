# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formProduto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Controller.ProdutoController import ProdutoController

class Ui_MainWindow(object):

    def __init__(self):
        self.produtoController = ProdutoController()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcluir.setGeometry(QtCore.QRect(250, 170, 75, 23))
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(90, 170, 75, 23))
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.btnConsultar.setObjectName("btnConsultar")
        self.edtValor = QtWidgets.QLineEdit(self.centralwidget)
        self.edtValor.setGeometry(QtCore.QRect(60, 70, 381, 21))
        self.edtValor.setObjectName("edtValor")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.label_4.setObjectName("label_4")
        self.edtTipoSetor = QtWidgets.QLineEdit(self.centralwidget)
        self.edtTipoSetor.setGeometry(QtCore.QRect(60, 100, 171, 20))
        self.edtTipoSetor.setObjectName("edtTipoSetor")
        self.btnAtualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtualizar.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.edtDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.edtDescricao.setGeometry(QtCore.QRect(60, 40, 381, 20))
        self.edtDescricao.setObjectName("edtDescricao")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.edtId = QtWidgets.QLineEdit(self.centralwidget)
        self.edtId.setGeometry(QtCore.QRect(60, 10, 111, 20))
        self.edtId.setObjectName("edtId")
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
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnCadastrar.clicked.connect(self.cadastrar)
        self.btnAtualizar.clicked.connect(self.atualizar)
        self.btnExcluir.clicked.connect(self.excluir)

    def consultar(self):
        dados = self.produtoController.consultar(int(self.edtId.text()))
        if dados:
            self.edtDescricao.setText(dados[1])
            self.edtValor.setText(dados[2])
            self.edtTipoSetor.setText(dados[3])
            print("Consultado valores!")
        else:
            self.edtId.setText('')
            self.edtDescricao.setText('')
            self.edtValor.setText('')
            self.edtTipoSetor.setText('')
            print("Não foi possivel consultar!")

    def cadastrar(self):
        if self.produtoController.cadastrar(int(self.edtId.text()),
                                         self.edtDescricao.text(),
                                         float(self.edtValor.text()),
                                         self.edtTipoSetor.text()):
            print('Produto cadastrado!')
            self.edtId.setText('')
            self.edtDescricao.setText('')
            self.edtValor.setText('')
            self.edtTipoSetor.setText('')
        else:
            self.edtId.setText('')
            print('Erro ao cadastrar Produto!')

    def atualizar(self):
        if self.produtoController.atualizar(str(self.edtId.text()),
                                            self.edtDescricao.text(),
                                            str(self.edtValor.text()),
                                            self.edtTipoSetor.text()):
            print('Produto atualizado!')

            self.edtId.setText('')
            self.edtDescricao.setText('')
            self.edtValor.setText('')
            self.edtTipoSetor.setText('')
        else:
            print('Erro ao atualizar Produto!')

    def excluir(self):
        if self.produtoController.excluir(self.edtId.text()):
            print('Produto excluído!')
            self.edtId.setText('')
            self.edtDescricao.setText('')
            self.edtValor.setText('')
            self.edtTipoSetor.setText('')
        else:
            print('Erro ao excluir Produto!')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnExcluir.setText(_translate("MainWindow", "Excluir"))
        self.btnCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.btnConsultar.setText(_translate("MainWindow", "Consultar"))
        self.label_4.setText(_translate("MainWindow", "Tipo Setor"))
        self.btnAtualizar.setText(_translate("MainWindow", "Atualizar"))
        self.label.setText(_translate("MainWindow", "Código"))
        self.label_3.setText(_translate("MainWindow", "Valor"))
        self.label_2.setText(_translate("MainWindow", "Descrição"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
