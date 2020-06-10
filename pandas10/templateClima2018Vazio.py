# -*- coding: utf-8 -*-
"""
Tempo Final de Semana
groupby
"""

"""
Perguntas:
a) Temperatura maxima no FDS em cada cidade.
b) Vento Medio em cada cidade
c) Cidade em que, na media, ha´ mais vento
d) Total de dias chuvosos por cidade
e) Cidade(s) com mais dias de chuva
f) Quantas e quais cidade(s) com  SOL no sabado

"""
import pandas as pd
import matplotlib.pyplot as plt

'''
Criar o dataframe dfTempo a partir do arquivo climaFDS2018.xlsx,
primeira coluna como indice e primeira linha como columns
''' 
print('\n-----------------------------------------------------')
dfTempo=pd.read_excel('climaFDS2018.xlsx',header=0,index_col=0)

print('\n-----------------------------------------------------')
print('1- DF  dfTempo:')


print('\n-----------------------------------------------------')
print('\nPara responder as perguntas a e b e´interessante agrupar dados por cidade')

print('\n-----------------------------------------------------')
print('\n')
print('\nExibir os grupo: cidade e o DF da cidade ')
print('\n2-Grupos criados')


    
print('\n-----------------------------------------------------')
print('\nExibir o grupo (DF) do rio de janeiro ')    
print('\n3-Rio de Janeiro')


print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta A (Temperatura Maxima por Cidade)')
print('\nAplicando funcao da agregacao no grupo. Exibir o DF obtido')
print('\n4-Temperatura maxima por cidade ')


print('\n-----------------------------------------------------')
print('\n6-So Temperatura maxima por cidade e o dia de maxima ')


print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta B (Vento Medio por Cidade)')
print('\n7-Vento Medio por cidade. Criar o dfVentoMd (df de vento medio por cid)')

print('\nExibir o DF dfVentoMd resultante')
print('\nExibir tambem as informacoes (info), colunas e index')


print('\nRenomear a coluna mean para VMedio. Exibir o DF dfVentoMd resultante')
print('\nExibir tambem as informacoes (info), colunas e index')



print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta C: cidade em que na media ha mais vento')
print('\n8-Cidade em que na media ha´ mais vento ')

#E se tivessem mais de uma cidade com o mesmo maximo?

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta D: Total de dias chuvosos por cidade')
print('\nDICA: crosstab')
print('\n9-Total de dias chuvosos por cidade')
print('\n9.1: usar crosstab e exibir o DF gerado')

print('\n9.2-RESPOSTA: Total de dias chuvosos por cidade')

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta E')
print('\n10-Cidade(s) com mais dias de chuva e quantos dias de chuva')

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta F')
print('\n11-Quantas e quais cidade(s) com  SOL no sabado ')

print('\nQuantidade de cidades com sol no sabado:')
print('\nCidade(s) com  SOL no sabado ')

