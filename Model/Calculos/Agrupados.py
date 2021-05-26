class Agrupados:

    def __init__(self, clases=None, marcaClase=None, frecuenciaAbsoluta=None):
        self._marcaClase = marcaClase
        self._noClases = clases
        self._frecuenciaAbsoluta = frecuenciaAbsoluta.copy() if frecuenciaAbsoluta is not None else None
        self.__media = self.__media_aritmetica()
        self.__mediana = self.__mediana()
        self.__moda = self.__moda()
        self.__varianza = self.__varianza()
        self.__desviacionEstandar = self.__desviacion_estandar()

    def __media_aritmetica(self):
        suma = 0
        media = None
        if self._marcaClase is not None and len(self._marcaClase) >1 :
            for i in range(len(self._marcaClase)):
                suma += (self._marcaClase[i]*self._frecuenciaAbsoluta[i])
            noDatos = 0
            for valor in self._frecuenciaAbsoluta:
                noDatos+= valor
            media = round(suma / noDatos,2)
        return media

    def __mediana(self):
        mediana = None
        if self._noClases is not None :
            if self._noClases % 2 == 0:
                valor1 = self._noClases / 2
                valor2 = (self._noClases / 2) + 1
                valor3 = (self._marcaClase[int(valor1-1)]+self._marcaClase[int(valor2-1)])/2
                mediana = round(valor3,2)
            else:
                valor = int((self._noClases + 1) / 2)
                mediana = self._marcaClase[valor-1]
        return mediana

    def __moda(self):
        if self._frecuenciaAbsoluta is not None and len(self._frecuenciaAbsoluta) >1 :
            return self._marcaClase[self._frecuenciaAbsoluta.index(max(self._frecuenciaAbsoluta))]
        return None

    def __varianza(self):
        suma = 0
        varianza = None
        if self._frecuenciaAbsoluta is not None and len(self._frecuenciaAbsoluta) >1 :
            for i in range(len(self._frecuenciaAbsoluta)) :
                suma += self._frecuenciaAbsoluta[i] * pow(self._marcaClase[i], 2)
            noDatos = 0
            for valor in self._frecuenciaAbsoluta:
                noDatos += valor
            varianza = round((suma - (noDatos * pow(self.__media_aritmetica(), 2))) / (noDatos - 1),2)
        return varianza

    def __desviacion_estandar(self):
        varianza = self.__varianza
        if varianza is not None:
            return round(pow(varianza, (1 / 2)),2)
        return None

    def get_media_aritmetica(self):
        return self.__media

    def get_mediana(self):
        return self.__mediana

    def get_moda(self):
        return self.__moda

    def get_varianza(self):
        return self.__varianza

    def get_desviacion_estandar(self):
        return self.__desviacionEstandar
