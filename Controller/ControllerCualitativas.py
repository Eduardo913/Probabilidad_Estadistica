from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from View.viewCualitativas import Ui_Principal
from Model.Grafica import *
from Model.Calculos.CalculosCualitativos import CalculosCualitativos


class ControllerCualitativas(QMainWindow):
    def __init__(self, datos=[]):
        super(ControllerCualitativas, self).__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.tables = [self.ui.tableCualitativas,self.ui.tableFrecuencia]
        self.datos = datos
        self.inicializar_vista()
        self.grafica()

    def inicializar_vista(self):
        self.llenar_tablas(self.ui.tableCualitativas, self.datos)
        self.cualitativos = CalculosCualitativos(self.datos)
        self.llenar_tabla_frecuencia(self.ui.tableFrecuencia,self.cualitativos.get_frecuencia_absoluta_relativa())

    def llenar_tablas(self, table, datos=[]):
        if datos is not None and len(datos) > 1:
            fila = 0
            columna = 0
            for registro in datos:
                self.tables[self.tables.index(table)].insertRow(fila)
                celda = QTableWidgetItem(str(registro))
                self.tables[self.tables.index(table)].setItem(fila, columna, celda)
                fila += 1

    def llenar_tabla_frecuencia(self, table, datos = []):
        if datos is not None and len(datos) > 1:
            fila = 0
            for registo in datos:
                columna = 0
                self.tables[self.tables.index(table)].insertRow(fila)
                for elemento in registo:
                    celda = QTableWidgetItem(str(elemento))
                    self.tables[self.tables.index(table)].setItem(fila, columna, celda)
                    columna +=1
                fila += 1

    def grafica(self):
        labels, values = generarListaPastel(self.cualitativos.get_frecuencia_absoluta())
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.pie(values,labels=labels,autopct="%1.1f%%",labeldistance=1.2,
                                          shadow=True,rotatelabels=True,startangle=120)
        self.ui.MplWidget.canvas.axes.set_title("Grafica de Pastel", fontsize=14,loc="right")
        self.ui.MplWidget.canvas.axes.axis("equal")

        self.ui.MplWidget.canvas.draw()