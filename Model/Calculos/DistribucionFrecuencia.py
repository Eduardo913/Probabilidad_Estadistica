import math

class DistribucionFrecuencia:
    def __init__(self,listDatos = None):
        if(listDatos != None):
            listDatos.sort()
            self.__listDatos = listDatos
            self.__rango = self.__rango()
            self.__noClase = self.__no_clases()
            self.__anchoClase = self.__ancho_clase()
            self.__limitesClases = self.__limite_clases()
            self.__marcaClase = self.__marca_clase()
            self.__frecuenciaAbsolutaDatos = self.__frecuencia_absoluta_datos()
            self.__frecuenciaAbsolutaClases = self.__frecuencia_absoluta_clases()
            self.__frecuenciaRelatica = self.__frecuencia_relativa_clases()

    def __rango(self):
        listDatos = self.__listDatos
        maximo = listDatos[len(self.__listDatos)-1]
        minimo = listDatos[0]
        return round(maximo-minimo,1)

    def __no_clases(self):
        return round(1 + 3.3 * math.log(len(self.__listDatos),10))

    def __ancho_clase(self):
        rango = self.__rango
        noClase = self.__noClase
        if(rango != None and noClase != None):
            return round(rango/noClase,2)

    def __limite_clases(self):
        inicial =self.__listDatos[0]
        incremento = self.__anchoClase
        listLimites = []
        for i in range(self.__noClase):
            final = round(inicial + incremento,2)
            listLimites.append((inicial,final))
            inicial=final
        return listLimites

    def __marca_clase(self):
        marcaClase = []
        listlimites=self.__limitesClases
        for i in range(len(listlimites)):
            limites = listlimites[i]
            marcaClase.append(round((limites[0]+limites[1])/2,3))
        return marcaClase

    def __frecuencia_absoluta_datos(self):
        listaDatos = self.__listDatos
        listNoRepetidos = self.__eliminar_repetidos(listaDatos)
        listFrecuencia =[]
        for i in listNoRepetidos:
            listFrecuencia.append((i,listaDatos.count(i)))

        return listFrecuencia

    def __frecuencia_absoluta_clases(self):
        listFrecuenciaDatos = self.__frecuenciaAbsolutaDatos
        listLimites = self.__limitesClases
        listFrecuencia = []
        aux =0
        anterior = 0
        for limites in listLimites:
            superio = limites[1]
            acumulativo = 0
            for frecuencia in listFrecuenciaDatos:
                valor = frecuencia[0]
                if valor<= superio:
                    acumulativo = acumulativo + frecuencia[1]
            listFrecuencia.append(acumulativo-anterior)
            anterior=acumulativo
        return listFrecuencia

    def __frecuencia_relativa_clases(self):
        cantidadDatos = len(self.__listDatos)
        frecuenciaAbsoluta = self.__frecuenciaAbsolutaClases
        frecuenciarelativa = []

        for valor in frecuenciaAbsoluta:
            frecuenciarelativa.append(f'{round(valor*100/cantidadDatos,2)} %')
        return frecuenciarelativa



    def __eliminar_repetidos(self,datos):
        lista = []
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
        return self.__frecuenciaRelatica