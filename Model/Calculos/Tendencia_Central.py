import statistics

from scipy import stats


class Tendencia_Central:

    def __init__(self, datos=None):
        self._datos = datos.copy() if datos is not None else None

    def mediaAritmetica(self, datos=None):
        datos = self._datos.copy() if self._datos is not None else None
        media = round(stats.tmean(datos), 2) if datos is not None else None
        return media

    def mediaRecortada(self, porcentaje=.10):
        datos = self._datos.copy() if self._datos is not None else None
        media = round(stats.trim_mean(datos, porcentaje), 2) if datos is not None else None
        return media

    def mediaGeometica(self):
        datos = self._datos.copy() if self._datos is not None else None
        media = round(stats.gmean(datos), 2) if datos is not None else None
        return media

    def mediana(self):
        datos = self._datos.copy() if self._datos is not None else None
        mediana = statistics.median(datos) if datos is not None else None
        return mediana

    def moda(self):
        datos = self._datos.copy() if self._datos is not None else None
        moda = statistics.multimode(datos) if datos is not None else None
        return moda

    def sesgo(self):
        media = self.mediaAritmetica()
        mediana = self.mediana()
        aux = self.moda()
        moda = stats.tmean(aux) if aux is not None else None
        sesgo = None
        if media is not None and mediana is not None and moda is not None:
            if media < mediana < moda:
                sesgo = "A la Izquierda"
            elif media == mediana == moda:
                sesgo = "Simetrico"
            else:
                if media > mediana > moda:
                    sesgo = "A la Derecha"
        return sesgo

