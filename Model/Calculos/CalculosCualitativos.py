
class CalculosCualitativos():

    def __init__(self,datos):
        self._datos = datos.copy() if datos is not None else None
        self.__frecuenciaAbsoluta = self.__frecuencia_absoluta_datos()
        self.__frecuenciaAbsRel = self.__frecuencia_relativa_absoluta_datos()

    def __frecuencia_absoluta_datos(self):
        listaDatos = self._datos if self._datos is not None else None
        listFrecuencia = []
        suma = 0
        if listaDatos != None:
            listNoRepetidos = self.__eliminar_repetidos(listaDatos.copy())
            for i in listNoRepetidos:
                listFrecuencia.append((i,listaDatos.count(i)))
                suma+=listaDatos.count(i)
        return listFrecuencia

    def __frecuencia_relativa_absoluta_datos(self):
        frecuencia = []
        if self._datos != None:
            cantidadDatos = len(self._datos)
            frecuenciaAbsoluta = self.__frecuenciaAbsoluta
            for valor in frecuenciaAbsoluta:
                frecuencia.append([valor[0], valor[1], f'{round(valor[1] * 100 / cantidadDatos, 2)} %'])
        return frecuencia

    def __eliminar_repetidos(self,datos):
        lista = []
        if datos != None:
            for valor in datos:
                if not valor in lista:
                    lista.append(valor)
        return lista

    def get_frecuencia_absoluta(self):
        return self.__frecuenciaAbsoluta

    def get_frecuencia_absoluta_relativa(self):
        return self.__frecuenciaAbsRel