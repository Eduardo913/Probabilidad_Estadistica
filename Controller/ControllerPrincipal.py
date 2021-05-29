from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QApplication
from View.viewPrincipal import Ui_Principal
from getpass import getuser
from Model.ReadingFiles import ReadingFiles
from Controller.ControllerContinuas import ControllerContinuas
from Controller.ControllerDiscretas import ControllerDiscretas
from Controller.ControllerCualitativas import ControllerCualitativas

class ControllerPrincipal(QMainWindow):
    def __init__(self):
        super(ControllerPrincipal, self).__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.tables = [self.ui.tableCualitativos, self.ui.tableContinuos, self.ui.tableDiscretos]
        self.datos_cualitativos, self.datos_Continuos, self.datos_Discretos= None ,None ,None
        self.conect_metodos()

    def conect_metodos(self):
        self.ui.ElegirArchivo.clicked.connect(self.archivo)
        self.ui.buttonDiscretos.clicked.connect(self.viewDiscretas)
        self.ui.buttonContinuos.clicked.connect(self.viewContinuas)
        self.ui.buttonCualitativos.clicked.connect(self.viewCualitativas)

    def inicializar_datos(self):
        self.cleanTable()
        reading = ReadingFiles()
        self.datos_cualitativos , self.datos_Continuos , self.datos_Discretos = reading.leerCsv(self.__path)
        self.datos_Continuos.sort()
        self.datos_Discretos.sort()
        self.datos_cualitativos.sort()
        self.llenar_tablas(self.ui.tableContinuos, self.datos_Continuos)
        self.llenar_tablas(self.ui.tableCualitativos, self.datos_cualitativos)
        self.llenar_tablas(self.ui.tableDiscretos, self.datos_Discretos)

    def llenar_tablas(self, table, datos):
        if datos is not None and len(datos) > 1:
            fila = 0
            columna = 0
            for registro in datos:
                self.tables[self.tables.index(table)].insertRow(fila)
                celda = QTableWidgetItem(str(registro))
                self.tables[self.tables.index(table)].setItem(fila, columna, celda)
                fila += 1

    def cleanTable(self):
        for table in self.tables:
            table.clearContents()
            table.update()

    def archivo(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona tu Archivo", f'C:/Users/{getuser()}/Documents',
                                                  "All Files (*);;CSV (*.csv)",
                                                  options=options)
        if fileName:
            self.__path = fileName
            self.ui.TextFieldPath.setText(self.__path)
            self.inicializar_datos()

    def viewContinuas(self):
        self.view = ControllerContinuas(self.datos_Continuos)
        self.view.show()

    def viewDiscretas(self):
        self.view = ControllerDiscretas(self.datos_Discretos)
        self.view.show()

    def viewCualitativas(self):
        self.view = ControllerCualitativas(self.datos_cualitativos)
        self.view.show()