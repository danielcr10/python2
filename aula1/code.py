# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
def areaRetangulo(lado1, lado2):
    return lado1*lado2

def hipotenusa(cat1, cat2):
    return (cat1**2+cat2**2)**0.5

def areaTotal(ladoA, ladoB, ladoC, ladoD, ladoE):
    hipo = hipotenusa(ladoA, ladoD)
    aRet1 = areaRetangulo(ladoA, ladoB)
    aRet2 = areaRetangulo(ladoC, ladoD)
    aRet3 = areaRetangulo(hipo, ladoE)
    aTriangulo = areaRetangulo(ladoA, ladoD)/2
    print("Area retangulo 1: ", aRet1)
    print("Area retangulo 2: ", aRet2)
    print("Area retangulo 3: ", aRet3)
    print("Area trianglo: ", aTriangulo)
    print("Area total: ", aRet1 + aRet2 + aRet3 + aTriangulo)
    return

def areaTotalInput():
    ladoA = float(input("Entre com o lado A: "))
    ladoB = float(input("Entre com o lado B: "))
    ladoC = float(input("Entre com o lado C: "))
    ladoD = float(input("Entre com o lado D: "))
    ladoE = float(input("Entre com o lado E: "))
    areaTotal(ladoA, ladoB, ladoC, ladoD, ladoE)
    return

def concatena(s):
    conc = s[0]+s[1]+s[-1]+s[-2]
    return s + 4*conc

def ehMultiplo(n1, n2):
    return (n1%n2 == 0) and True or False

def algarismoDigitoVerificador(PB):
    if(ehMultiplo(PB, 2)):
        return PB % 8
    else:
        return PB % 7
'''def digitosVerificadores(intN)'''
Área de anexos

