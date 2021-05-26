import  pandas as pd
from numpy import double


class ReadingFiles:

    def leer(self,ruta):
        archivo = open(ruta,'r')
        datos = archivo.read()
        return self.generarLista(datos)

    def generarLista(self,datos):
        lista = []
        valor = ""
        for i in range(len(datos)):
            if datos[i] != ' ' and datos[i] != ',':
                valor = valor + datos[i]

            if datos[i] == ',' or i == len(datos)-1:
                lista.append(float(valor))
                valor = ''
        return lista

    def leerCsv(self,ruta):
        self._archivo_csv = pd.read_csv(ruta,header = 0)
        return self.generar_lista_cualitativa(),self.generar_lista_cuantitativa(),self.generar_lista_discreta()

    def generar_lista_cualitativa(self):
        return [valor for valor in self._archivo_csv['Genero de musica más escuchado']]

    def generar_lista_cuantitativa(self):
        return [double("{0:.3f}".format(valor))for valor in self._archivo_csv['tiempo dedicado a escuchar música (Horas)']]

    def generar_lista_discreta(self):
        return [double("{0:.3f}".format(valor))for valor in self._archivo_csv['Canciones escuchadas al día']]

