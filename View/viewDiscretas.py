# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewDiscretas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.setEnabled(True)
        Principal.resize(852, 552)
        Principal.setStyleSheet("background-color: rgba(18,18,18,1);")
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(False)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgba(18,18,18,1);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(710, 190, 91, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.textDesviacion = QtWidgets.QLineEdit(self.frame)
        self.textDesviacion.setEnabled(False)
        self.textDesviacion.setGeometry(QtCore.QRect(710, 310, 113, 21))
        self.textDesviacion.setStyleSheet("color: rgb(255, 255, 255);")
        self.textDesviacion.setObjectName("textDesviacion")
        self.textVarianza = QtWidgets.QLineEdit(self.frame)
        self.textVarianza.setEnabled(False)
        self.textVarianza.setGeometry(QtCore.QRect(580, 310, 113, 21))
        self.textVarianza.setStyleSheet("color: rgb(255, 255, 255);")
        self.textVarianza.setObjectName("textVarianza")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(580, 190, 111, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.TextMediaArtimetica = QtWidgets.QLineEdit(self.frame)
        self.TextMediaArtimetica.setEnabled(False)
        self.TextMediaArtimetica.setGeometry(QtCore.QRect(580, 160, 113, 21))
        self.TextMediaArtimetica.setStyleSheet("color: rgb(255, 255, 255);")
        self.TextMediaArtimetica.setObjectName("TextMediaArtimetica")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(580, 240, 91, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(580, 290, 111, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.TextMediaTruncada = QtWidgets.QLineEdit(self.frame)
        self.TextMediaTruncada.setEnabled(False)
        self.TextMediaTruncada.setGeometry(QtCore.QRect(580, 210, 113, 21))
        self.TextMediaTruncada.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.TextMediaTruncada.setObjectName("TextMediaTruncada")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(710, 290, 121, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(710, 140, 91, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(580, 140, 81, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.TextMediaGeometrica = QtWidgets.QLineEdit(self.frame)
        self.TextMediaGeometrica.setEnabled(False)
        self.TextMediaGeometrica.setGeometry(QtCore.QRect(710, 160, 113, 21))
        self.TextMediaGeometrica.setStyleSheet("color: rgb(255, 255, 255);")
        self.TextMediaGeometrica.setObjectName("TextMediaGeometrica")
        self.TextMediana = QtWidgets.QLineEdit(self.frame)
        self.TextMediana.setEnabled(False)
        self.TextMediana.setGeometry(QtCore.QRect(710, 210, 113, 21))
        self.TextMediana.setStyleSheet("color: rgb(255, 255, 255);")
        self.TextMediana.setObjectName("TextMediana")
        self.TextModa = QtWidgets.QLineEdit(self.frame)
        self.TextModa.setEnabled(False)
        self.TextModa.setGeometry(QtCore.QRect(580, 260, 113, 21))
        self.TextModa.setStyleSheet("color: rgb(255, 255, 255);")
        self.TextModa.setObjectName("TextModa")
        self.tableDiscretas = QtWidgets.QTableWidget(self.frame)
        self.tableDiscretas.setGeometry(QtCore.QRect(10, 20, 125, 501))
        self.tableDiscretas.setStyleSheet("background-color: rgb(198, 198, 198);\n"
"color: rgb(50, 50, 50);")
        self.tableDiscretas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableDiscretas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableDiscretas.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableDiscretas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableDiscretas.setRowCount(0)
        self.tableDiscretas.setObjectName("tableDiscretas")
        self.tableDiscretas.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableDiscretas.setHorizontalHeaderItem(0, item)
        self.tableDiscretas.horizontalHeader().setCascadingSectionResizes(False)
        self.tableDiscretas.horizontalHeader().setDefaultSectionSize(100)
        self.tableDiscretas.horizontalHeader().setHighlightSections(False)
        self.tableDiscretas.horizontalHeader().setMinimumSectionSize(10)
        self.tableDiscretas.horizontalHeader().setSortIndicatorShown(False)
        self.tableDiscretas.horizontalHeader().setStretchLastSection(True)
        self.tableDiscretas.verticalHeader().setVisible(True)
        self.tableDiscretas.verticalHeader().setCascadingSectionResizes(True)
        self.tableDiscretas.verticalHeader().setDefaultSectionSize(25)
        self.tableDiscretas.verticalHeader().setHighlightSections(True)
        self.tableDiscretas.verticalHeader().setMinimumSectionSize(10)
        self.tableDiscretas.verticalHeader().setSortIndicatorShown(True)
        self.tableDiscretas.verticalHeader().setStretchLastSection(False)
        self.MplWidget = MplWidget(self.frame)
        self.MplWidget.setGeometry(QtCore.QRect(150, 260, 411, 261))
        self.MplWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MplWidget.setObjectName("MplWidget")
        self.tableFrecuencia = QtWidgets.QTableWidget(self.frame)
        self.tableFrecuencia.setGeometry(QtCore.QRect(150, 20, 411, 211))
        self.tableFrecuencia.setStyleSheet("background-color: rgb(198, 198, 198);\n"
"color: rgb(50, 50, 50);")
        self.tableFrecuencia.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableFrecuencia.setObjectName("tableFrecuencia")
        self.tableFrecuencia.setColumnCount(3)
        self.tableFrecuencia.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableFrecuencia.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFrecuencia.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFrecuencia.setHorizontalHeaderItem(2, item)
        self.tableFrecuencia.horizontalHeader().setDefaultSectionSize(130)
        self.tableFrecuencia.horizontalHeader().setSortIndicatorShown(False)
        self.tableFrecuencia.horizontalHeader().setStretchLastSection(True)
        self.tableFrecuencia.verticalHeader().setVisible(False)
        self.tableFrecuencia.verticalHeader().setHighlightSections(True)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(580, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.Volver = QtWidgets.QPushButton(self.frame)
        self.Volver.setGeometry(QtCore.QRect(700, 20, 121, 21))
        self.Volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Volver.setStyleSheet("background-color: rgba(30, 215, 96,0.65);\n"
"color: white;\n"
"font:bold;\n"
"\n"
"")
        self.Volver.setCheckable(False)
        self.Volver.setChecked(False)
        self.Volver.setDefault(True)
        self.Volver.setFlat(False)
        self.Volver.setObjectName("Volver")
        self.horizontalLayout.addWidget(self.frame)
        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Probabilidad_Estaditica"))
        self.label_4.setText(_translate("Principal", "Mediana:"))
        self.label_3.setText(_translate("Principal", "Media Truncada 10%:"))
        self.label_5.setText(_translate("Principal", "Moda:"))
        self.label_6.setText(_translate("Principal", "Varianza"))
        self.label_8.setText(_translate("Principal", "Desviación Estandar"))
        self.label_2.setText(_translate("Principal", "Media Geometrica:"))
        self.label.setText(_translate("Principal", "Media Aritmetica:"))
        item = self.tableDiscretas.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "Discretos"))
        item = self.tableFrecuencia.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "Valor"))
        item = self.tableFrecuencia.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "Frecuencia Absoluta"))
        item = self.tableFrecuencia.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "Frecuencia Relativa"))
        self.label_7.setText(_translate("Principal", "Datos obtenidos"))
        self.Volver.setText(_translate("Principal", "Volver"))
from Model.mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
