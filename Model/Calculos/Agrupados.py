class Agrupados:

    def __init__(self, clases, marcaClase, frecuenciaAbsoluta):
        self._marcaClase = marcaClase
        self._noClases = clases
        self._frecuenciaAbsoluta = frecuenciaAbsoluta
        self.__media = self.__media_aritmetica()
        self.__mediana = self.__mediana()
        self.__moda = self.__moda()
        self.__varianza = self.__varianza()
        self.__desviacionEstandar = self.__desviacion_estandar()

    def __media_aritmetica(self):
        suma = 0

        for valor in self._marcaClase:
            suma = suma + valor
        noDatos = 0
        for valor in self._frecuenciaAbsoluta:
            noDatos = noDatos + valor

        media = suma / noDatos

        return media

    def __mediana(self):
        if self._noClases % 2 == 0:
            valor1 = self._noClases / 2
            valor2 = (self._noClases / 2) + 1
            valor3 = int(valor1 + valor2)
            mediana = self._frecuenciaAbsoluta[valor3]
        else:
            valor = int((self._noClases + 1) / 2)
            mediana = self._frecuenciaAbsoluta[valor]
        return mediana

    def __moda(self):
        return max(self._frecuenciaAbsoluta)

    def __varianza(self):
        suma = 0

        for i in range(len(self._frecuenciaAbsoluta)):
            suma = self._frecuenciaAbsoluta[i] * pow(self._marcaClase[i], 2)
        noDatos = 0
        for valor in self._frecuenciaAbsoluta:
            noDatos = noDatos + valor

        varianza = (suma - (noDatos * pow(self.__media_aritmetica(), 2))) / (noDatos - 1)
        return varianza

    def __desviacion_estandar(self):
        varianza = self.__varianza
        return pow(varianza, (1 / 2))

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
