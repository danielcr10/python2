def minmax(lInteiros):
    minimo = lInteiros[0]
    maximo = lInteiros[0]
    qMin = 1
    qMax = 1

    for num in lInteiros[1:]:
        if num < minimo:
            minimo = num
            qMin = 1
        elif num == minimo:
            qMin += 1
        elif num > maximo:
            maximo = num
            qMax = 1
        else:
            qMax += 1

    return ((minimo, maximo), (qMin, qMax))


teste = [1, 3, 4, 4, 14, 23, 5, 5, 4, 12, 1, 1, 1, 14, 4, 23, 23, 23]
((minimo, qMin), (maximo, qMax)) = minmax(teste)
