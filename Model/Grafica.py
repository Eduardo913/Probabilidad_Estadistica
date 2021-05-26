

def generarListaBarras(datos = []):
    label = []
    values = []
    datos = datos.copy() if datos is not None else None

    for i in range(len(datos)):
        label.append(datos[i][0])
        values.append(datos[i][1])
    return label,values

def __eliminar_repetidos(datos = []):
    lista = []
    if datos != None:
        for valor in datos:
            if not valor in lista:
                lista.append(valor)
    return lista