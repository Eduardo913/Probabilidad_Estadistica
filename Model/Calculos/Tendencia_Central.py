import math
class Tendencia_Central:

    def mediaAritmetica(self, datos=None):
        media = None
        if(datos != None):
            suma = 0.0
            for valor in datos:
                suma = suma + valor
            media = suma/len(datos)
        return media

    def mediaRecortada(self,datos ,porcentaje = 10):
        media = None
        if(datos!= None):
            datos.sort()
            eliminar = round((len(datos) * porcentaje)/100)
            for i in range(eliminar):
                datos.remove(datos[0])
                datos.remove(datos[(len(datos)-1)])
            media =self.mediaAritmetica(datos)
        return media

    def mediaGeometica(self, datos=None):
        media = None
        if datos != None:
            multiplicacion = 1.0
            for valor in datos:
                multiplicacion = multiplicacion * valor
            media = round(math.pow(multiplicacion,(1/datos.__len__())),2)
        return media

    def mediana(self,datos = None):
        mediana = None
        if datos != None:
            datos.sort()
            index = round((len(datos) / 2) - 1)
            mediana = datos[index] if (len(datos) % 2) else datos[index] + datos[index+1]/2
        return mediana

    def moda(self, datos = None):
        maximo = 0
        moda = None
        multimodal = []
        if datos != None:

            for valor in datos:
                temp =  datos.count(valor)
                if temp > maximo and temp > 1 :
                    maximo = temp
                    moda = valor

            for valor in datos:
                temp = datos.count(valor)
                if temp == maximo:
                    if(valor != moda and multimodal.count(valor) == 0):
                        multimodal.append(valor)

            multimodal.append(moda)

        return multimodal if multimodal.__len__() > 1 else moda
