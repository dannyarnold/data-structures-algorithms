# vectorshell = [77, 74, 35, 99, 21, 60, 71, 11]


# def shellsort(vectorshell):
#     print("Vector a ordenar: ", vectorshell)

#     largo = 0
#     for i in vectorshell:
#         largo += 1

#     distancia = largo // 2

#     while distancia > 0:
#         for i in range(distancia, largo):
#             val = vectorshell[i]
#             j = i
#             while j >= distancia and vectorshell[j-distancia] > val:
#                 j -= distancia
#             vectorshell[j] = val
#         distancia //= 2
#     print("Vector ordenado con shell es: ", vectorshell)


# shellsort(vectorshell)

# SIN ERRORES
vectorshell = [77, 74, 35, 99, 21, 60, 71, 11]


def shellsort(vectorshell):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Shell Sort"""

    print("El vector a ordenar con shell es:", vectorshell)

    largo = 0

    for i in vectorshell:
        largo += 1

    distancia = largo // 2

    # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = val
        distancia //= 2  # Acotamos la distancia nuevamente y continua el ciclo
    print("El vector ordenado con shell es: ", vectorshell)


shellsort(vectorshell)
