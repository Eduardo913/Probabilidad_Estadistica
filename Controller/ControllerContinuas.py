from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from View.viewContinuas import Ui_Principal
from Model.Calculos.Tendencia_Central import Tendencia_Central
from Model.Calculos.Dispersion import Dispersion
from Model.Calculos.DistribucionFrecuencia import DistribucionFrecuencia
from Model.Calculos.Agrupados import Agrupados

class ControllerContinuas(QMainWindow):
    def __init__(self,datos=[]):
        super(ControllerContinuas, self).__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.tables = [self.ui.tableContinuos, self.ui.tableAgrupados]
        self.datos = datos
        self.inicializar_vista()
        self.grafica()
        self.ui.Volver.clicked.connect(self.close)


    def inicializar_vista(self):
        self.llenar_tablas(self.ui.tableContinuos,self.datos)
        tendencia = Tendencia_Central(self.datos)
        self.ui.TextMediaArtimetica.setText(str(tendencia.mediaAritmetica()))
        self.ui.TextMediaGeometrica.setText(str(tendencia.mediaGeometica()))
        self.ui.TextMediaTruncada.setText(str(tendencia.mediaRecortada()))
        self.ui.TextMediana.setText(str(tendencia.mediana()))
        self.ui.TextModa.setText(str(tendencia.moda()))
        self.ui.Sesgo.setText(str(tendencia.sesgo()))
        dispersion = Dispersion(self.datos,tendencia.mediaAritmetica())
        self.ui.textVarianzaM.setText(str(dispersion.get_varianza_muestra()))
        self.ui.textVarianzaP.setText(str(dispersion.get_varianza_poblacional()))
        self.ui.textDesviacionM.setText(str(dispersion.get_desviacion_muestra()))
        self.ui.textDesviacionP.setText(str(dispersion.get_varianza_poblacional()))
        self.distribucion = DistribucionFrecuencia(self.datos)
        self.llenar_tablas_Agrupada(self.ui.tableAgrupados,self.distribucion.generar_lista())

        agrupado = Agrupados(clases=self.distribucion.get_no_clase(),
                             marcaClase=self.distribucion.get_marca_clase(),
                             frecuenciaAbsoluta=self.distribucion.get_frecuencia_absoluta_clases())
        self.ui.TextMediaArtimeticaAgrupado.setText(str(agrupado.get_media_aritmetica()))
        self.ui.TextMedianaAgrupado.setText(str(agrupado.get_mediana()))
        self.ui.TextModaAgrupado.setText(str(agrupado.get_moda()))
        self.ui.textVarianzaAgrupado.setText(str(agrupado.get_varianza()))
        self.ui.textDesviacionAgrupado.setText(str(agrupado.get_desviacion_estandar()))

    def llenar_tablas(self, table, datos = []):
        if datos is not None and len(datos) > 1:
            fila = 0
            columna = 0
            for registro in datos:
                self.tables[self.tables.index(table)].insertRow(fila)
                celda = QTableWidgetItem(str(registro))
                self.tables[self.tables.index(table)].setItem(fila, columna, celda)
                fila += 1

    def llenar_tablas_Agrupada(self, table, datos = []):
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
        values, labels = self.distribucion.get_frecuencia_absoluta_clases(), \
                         [str(valor) for valor in self.distribucion.get_marca_clase()]

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(labels, values,edgecolor ='black', width=1)
        self.ui.MplWidget.canvas.axes.set_title("Histograma",fontsize=12)
        self.ui.MplWidget.canvas.axes.set_xlabel("Marca de Clase",fontsize=12)
        self.ui.MplWidget.canvas.axes.set_ylabel("Frecuencia Absoluta",fontsize=12)
        self.ui.MplWidget.canvas.draw()

        # self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        # self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')