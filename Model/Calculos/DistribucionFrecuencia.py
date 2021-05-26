import math

class DistribucionFrecuencia:
    def __init__(self,listDatos = None):
        if(listDatos != None):
            listDatos.sort()
        self.__listDatos = listDatos.copy() if listDatos is not None else None
        self.__rango = self.__rango()
        self.__noClase = self.__no_clases()
        self.__anchoClase = self.__ancho_clase()
        self.__limitesClases = self.__limite_clases()
        self.__marcaClase = self.__marca_clase()
        self.__frecuenciaAbsolutaDatos = self.__frecuencia_absoluta_datos()
        self.__frecuenciaAbsolutaClases = self.__frecuencia_absoluta_clases()
        self.__frecuenciaRelativa_clases = self.__frecuencia_relativa_clases()
        self.__frecuenciaAbsRelDatos = self.__frecuencia_relativa_absoluta_datos()

    def __rango(self):
        rango = None
        listDatos = self.__listDatos
        if listDatos != None :
            maximo = listDatos[len(self.__listDatos)-1]
            minimo = listDatos[0]
            rango = maximo-minimo
        return rango

    def __no_clases(self):
        clases = None
        if self.__listDatos != None:
            clases= round(1 + 3.3 * math.log(len(self.__listDatos),10))
        return clases

    def __ancho_clase(self):
        rango = self.__rango
        noClase = self.__noClase
        if(rango != None and noClase != None):
            return rango/noClase

    def __limite_clases(self):
        listLimites = []
        if self.__listDatos != None:
            inicial =self.__listDatos[0]
            incremento = self.__anchoClase
            for i in range(self.__noClase):
                final = inicial + incremento
                listLimites.append((round(inicial,2),round(final,2)))
                inicial=final
        return listLimites

    def __marca_clase(self):
        marcaClase = []
        if self.__listDatos != None:
            listlimites=self.__limitesClases
            for i in range(len(listlimites)):
                limites = listlimites[i]
                marcaClase.append(round((limites[0]+limites[1])/2,3))
        return marcaClase

    def __frecuencia_absoluta_datos(self):
        listaDatos = self.__listDatos.copy() if self.__listDatos is not None else None
        listFrecuencia = []
        suma = 0
        if listaDatos != None:
            listNoRepetidos = self.__eliminar_repetidos(listaDatos.copy())
            for i in listNoRepetidos:
                listFrecuencia.append((i,listaDatos.count(i)))
                suma+=listaDatos.count(i)
        return listFrecuencia

    def __frecuencia_absoluta_clases(self):
        listFrecuencia = []
        if self.__listDatos != None:
            listFrecuenciaDatos = self.__frecuenciaAbsolutaDatos.copy()
            listLimites = self.__limitesClases
            anterior = 0
            for limites in listLimites:
                superio = limites[1]
                acumulativo = 0
                for frecuencia in listFrecuenciaDatos:
                    valor = frecuencia[0]
                    if valor<= superio:
                        acumulativo += frecuencia[1]
                listFrecuencia.append(acumulativo-anterior)
                anterior=acumulativo
        return listFrecuencia

    def __frecuencia_relativa_absoluta_datos(self):
        frecuencia = []
        if self.__listDatos != None:
            cantidadDatos = len(self.__listDatos)
            frecuenciaAbsoluta = self.__frecuenciaAbsolutaDatos
            for valor in frecuenciaAbsoluta:
                frecuencia.append([valor[0],valor[1],f'{round(valor[1] * 100 / cantidadDatos, 2)} %'])
        return frecuencia

    def __frecuencia_relativa_clases(self):
        frecuenciarelativa = []
        if self.__listDatos != None:
            cantidadDatos = len(self.__listDatos)
            frecuenciaAbsoluta = self.__frecuenciaAbsolutaClases
            for valor in frecuenciaAbsoluta:
                frecuenciarelativa.append(f'{round(valor*100/cantidadDatos,2)} %')
        return frecuenciarelativa

    def generar_lista(self):
        lista = []
        if self.__listDatos != None:
            for i in range(self.__noClase):
                lista.append([i+1,self.__limitesClases[i][0],self.__limitesClases[i][1],self.__marcaClase[i],self.__frecuenciaAbsolutaClases[i],self.__frecuenciaRelativa_clases[i]])
        return lista

    def __eliminar_repetidos(self,datos):
        lista = []
        if datos != None:
            for valor in datos:
                if not valor in lista:
                    lista.append(valor)
        return lista

    def get_rango(self):
        return self.__rango

    def get_ancho_clase(self):
        return self.__anchoClase

    def get_no_clase(self):
        return self.__noClase

    def get_limites(self):
        return self.__limitesClases

    def get_marca_clase(self):
        return self.__marcaClase

    def get_frecuencia_absoluta_datos(self):
        return self.__frecuenciaAbsolutaDatos

    def get_frecuencia_absoluta_clases(self):
        return self.__frecuenciaAbsolutaClases

    def get_frecuencia_relativa_clases(self):
        return self.__frecuenciaRelativa_clases

    def get_frecuencia_absoluta_relatva_datos(self):
        return self.__frecuenciaAbsRelDatos
