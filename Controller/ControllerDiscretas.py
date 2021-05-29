from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from View.viewDiscretas import Ui_Principal
from Model.Calculos.Tendencia_Central import Tendencia_Central
from Model.Calculos.Dispersion import Dispersion
from Model.Calculos.DistribucionFrecuencia import DistribucionFrecuencia
from Model.Grafica import *


class ControllerDiscretas(QMainWindow):
    def __init__(self, datos=[]):
        super(ControllerDiscretas, self).__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.tables = [self.ui.tableDiscretas,self.ui.tableFrecuencia]
        self.datos = datos
        self.inicializar_vista()
        self.grafica()

    def inicializar_vista(self):
        self.llenar_tablas(self.ui.tableDiscretas, self.datos)
        tendencia = Tendencia_Central(self.datos)
        self.ui.TextMediaArtimetica.setText(str(tendencia.mediaAritmetica()))
        self.ui.TextMediaGeometrica.setText(str(tendencia.mediaGeometica()))
        self.ui.TextMediaTruncada.setText(str(tendencia.mediaRecortada()))
        self.ui.TextMediana.setText(str(tendencia.mediana()))
        self.ui.TextModa.setText(str(tendencia.moda()))

        dispersion = Dispersion(self.datos, tendencia.mediaAritmetica())
        self.ui.textVarianza.setText(str(dispersion.get_varianza_poblacional()))
        self.ui.textDesviacion.setText(str(dispersion.get_desviacion_poblacional()))

        self.distribucion = DistribucionFrecuencia(self.datos)
        self.llenar_tabla_frecuencia(self.ui.tableFrecuencia,self.distribucion.get_frecuencia_absoluta_relatva_datos())

    def llenar_tablas(self, table, datos=[]):
        if datos is not None and len(datos) > 1:
            fila = 0
            columna = 0
            for registro in datos:
                # self.tables[self.tables.index(table)].insertRow(fila)
                self.ui.tableDiscretas.insertRow(fila)
                celda = QTableWidgetItem(str(registro))
                # self.tables[self.tables.index(table)].setItem(fila, columna, celda)
                self.ui.tableDiscretas.setItem(fila,columna,celda)
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
        labels, values = generarListaBarras(self.distribucion.get_frecuencia_absoluta_datos())
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.barh(labels, values)
        self.ui.MplWidget.canvas.axes.set_title("grafica de barras", fontsize=12)
        self.ui.MplWidget.canvas.axes.set_xlabel("Frecuencia Absoluta (cantidad de  canciones por persona)",
                                                 fontsize=12)
        self.ui.MplWidget.canvas.axes.set_ylabel("No de canciones", fontsize=12)
        self.ui.MplWidget.canvas.draw()

        # self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        # self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
