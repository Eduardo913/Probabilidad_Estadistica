class Dispersion:

    def __init__(self,listDatos,mediaAritmetica):
        self.__listaDeDatos = listDatos.copy() if listDatos is not None else None
        self.__mediaAritmetica = mediaAritmetica
        self.__rango = self.__rango()
        self.__error = self.__error()
        self.__varianzaPoblacional , self.__varianzaMuestra  = self.__varianza_poblacional_muestra()
        self.__desviacionPoblacional, self.__desviacionMuestra = self.__desviacion_Centralizada()

    def __rango(self ,):
        rango = None
        listDatos = self.__listaDeDatos
        if listDatos != None:
            listDatos.sort()
            if(len(listDatos) > 1):
                rango = round(listDatos[len(listDatos)-1] - listDatos[0],1)

        return rango

    def __error(self):
        error = None
        listDatos = self.__listaDeDatos
        if listDatos != None:
            media = self.__mediaAritmetica
            error = []
            for valor in listDatos:
                error.append(round(valor-media,2))
        return error


    def __varianza_poblacional_muestra(self):
        errores = self.__error
        varianzaP = None
        varianzaM = None
        if errores != None:
            sumatoria = 0
            for valor in errores:
                sumatoria = sumatoria + pow(valor,2)

            varianzaP = round(sumatoria/len(errores),2)
            varianzaM = round(sumatoria/(len(errores) - 1),2)
        return varianzaP,varianzaM

    def __desviacion_Centralizada(self):
        desviacionP, desviacionM = None, None
        if self.__varianzaMuestra != None and self.__varianzaPoblacional != None:
            desviacionP = round(pow(self.__varianzaPoblacional,1/2),2)
            desviacionM = round(pow(self.__varianzaMuestra,1/2),2)
        return desviacionP,desviacionM

    def get_rango(self):
        return self.__rango

    def get_varianza_poblacional(self):
        return self.__varianzaPoblacional

    def get_varianza_muestra(self):
        return self.__varianzaMuestra

    def get_desviacion_poblacional(self):
        return self.__desviacionPoblacional

    def get_desviacion_muestra(self):
        return self.__desviacionMuestra

    def get_errores(self):
        return self.__error