# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:31:45 2019
@author: claudia ferlin
"""
import pandas as pd
import matplotlib.pyplot as plt
'''
O arquivo Excel sonopaiemae registra as horas de sono do pai e da mãe de um bebê durante 
8 semanas, diariamente.
Na planilha mae, estão os registros de horas de sono da mãe e na planilha pai, estão os 
registros de horas de sono do pai.
As planilhas têm cabeçalho (linha 1) e possuem o seguinte formato:
               Dia da semana  e  horas de sono
Na planilha maeSem estão os registros de horas de sono da mãe diariamente durante 8 semanas.
        Esta planilha não têm cabeçalho e possue o seguinte formato:
               Dia da semana+numero da semana  e  horas de sono
               Exemplo: seg2 que significa segunda-feira da segunda semana
'''
#============================================
# Construindo  Series a partir de um arquivo excel
#============================================
# 
#============================================
#       Manipulando a series 
#============================================
#   Utilizar a planilha Mae para criar a Series sMae
#   Utilizar a planilha Pai para criar a Series sPai
#       índice: coluna 0
#		nao tem linha de cabeçalho
#   Observe os 10ºs elementos
#   Observe as medidas princiapis (.describe)
# 
#I.	Criar as series sMae e sPai respectivamente
sPai=pd.read_excel("pandas7/sonopaiemae.xlsx",sheet_name="pai",index_col=0,header=None,squeeze=True)
sMae=pd.read_excel("pandas7/sonopaiemae.xlsx",sheet_name="mae",index_col=0,header=None,squeeze=True)

sPaiS=pd.read_excel("pandas7/sonopaiemae.xlsx",sheet_name="paiSem",index_col=0,header=0,squeeze=True)
sMaeS=pd.read_excel("pandas7/sonopaiemae.xlsx",sheet_name="maeSem",index_col=0,header=0,squeeze=True)
#II. Há repetição nos índices, como saber quais os valores possíveis (metodo unique)
print('-----------------------------------------------------')
print("\n Valores dos Índices sem repetição\n")
lInd=sMae.index.unique()
print("{}".format(list(lInd)))
print('-----------------------------------------------------')
#============================================
#      APENAS PARA A SERIES sMae:
#============================================
#**********************************************
#III.	Responder as seguintes perguntas:
#**********************************************
#a.	O maior tempo, o menor tempo, o mais frequente e o tempo médio 
maiorT = sMae.max()
menorT = sMae.min()
mediaT = sMae.mean()
freqT  = sMae.mode()
print('-----------------------------------------------------')
print("\na. O maior tempo:{}, o menor tempo:{},  o tempo médio:{:.2f}".format(maiorT, menorT, mediaT))
print("\nO mais frequente:\n{}".format(freqT))
print('-----------------------------------------------------')
#b.	O maior tempo, o menor tempo, o mais frequente e o tempo médio por dia da semana 
maiorT = sMae.max(level=0)
menorT = sMae.min(level=0)
mediaT = sMae.mean(level=0)
print('-----------------------------------------------------')
print("\nPor dia da semana:")
print(maiorT)
print("b. O maior tempo:\n{}\no menor tempo:\n{}\ntempo médio:\n{}\n".format(maiorT, menorT, mediaT))
#Exibindo graficamente em ordem de dia (reindex) as 3 informaçoes
#Use graficos diferentes para cada uma das informações
# TODO: Tirar comentario do show
maiorT.plot()
# plt.show()
menorT.plot()
# plt.show()
mediaT.plot()
# plt.show()
print('-----------------------------------------------------')
#c.	Qual o dia da semana com menor tempo médio de sono (e se houver mais de um?)
print('-----------------------------------------------------')
print("\nc.Qual o dia da semana com menor tempo médio de sono ")
print("\nUm deles: \n")
print('{}'.format(mediaT.idxmin()))
print("\nTodos: \n") #TODO: Fazer

print('-----------------------------------------------------')
# #**********************************************
# # d.	Filtrando:
# #**********************************************
# #i.	Consertar os valores negativos, isto e, torna-los positivos. Exibir a 
# #########################
# #  Versão 1) - pelo apply
# #########################

def ajuste(x):
      if x < 0:
            return x*(-1)
      else:
            return x
sMae = sMae.apply(ajuste)
print('-----------------------------------------------------')
print("\nc.Por apply: Consertando os valores negativos\n{}")
print(sMae)
print('-----------------------------------------------------')
# #########################
# #  Versão 2) - por filtro
# #########################

# TODO:
# print('-----------------------------------------------------')
# print("\nc.Por filtro: Consertando os valores negativos\n{}")
# print('-----------------------------------------------------')
# #ii.	O maior tempo, o menor tempo (ambos com os dias que os registraram))
print('-----------------------------------------------------')
print("\nii.O maior tempo: {} - Nos dias: {}".format(sMae.max(), sMae.idxmax()))
print("\nii.O menor tempo: {} - Nos dias: {}".format(sMae.min(), sMae.idxmin()))
print('-----------------------------------------------------')
# #iii.	Quantos dias com menos horas de sono que a média?
# print('-----------------------------------------------------')

# print("\niii.	Quantos dias com menos  horas de sono que a média?\n{}")
# print('-----------------------------------------------------')
# #iv.Comparando com a sPai, quantos dias o pai teve mais horas de sono que a mãe?
# print('-----------------------------------------------------')

# print("\niv.Quantos dias o pai teve mais horas de sono que a mãe?\n{}")
# print('-----------------------------------------------------')
# #v.	Comparando com a sPai, em quais dias da semana, o pai teve, em média, 
# #mais horas de sono que a mãe?
# print('-----------------------------------------------------')

# print("\nv.Em quais dias da semana, o pai teve, em média, mais horas de sono " \
#       "que a mãe?\n{}")
# print('-----------------------------------------------------')
# #**********************************************
# # e.	Categorizando:
# #**********************************************
# '''
# e.	Categorizando:
# i.	Quais dias com menos de 4 horas de sono? (pouco)
# ii.	Quais dias com 4 a 6 horas de sono (inclusive)? (abaixo) 
# iii.Quais dias com 6 a 8 horas de sono (inclusive)? (normal)
# iv.	Quais dias com mais de 8 horas de sono? (acima)
# '''

# #Exiba a tabela de frequência por categoria e o percentual de dias por categoria
# print('-----------------------------------------------------')
# print("\ne.Tabela de Frequência em cada categoria:\n{}")
# print("\ne.Tabela de Frequência com índices na ordem correta em cada categoria:\n{}")
# print("\ne. Percentual de dias por categoria:\n{}")
# print('-----------------------------------------------------')
# #**********************************************
# # f.	Agrupando por dia da semana
# #**********************************************

# #i.Qual O maior tempo, o menor tempo e o tempo médio por dia da semana? 
# print('-----------------------------------------------------')
# print("\ni.Qual O maior tempo, o menor tempo e o tempo médio por dia da semana? \n")

# print('-----------------------------------------------------')
# #ii Qual a diferença, por dia da semana, entre o tempo médio e o tempo mínimo da semana?
# print('-----------------------------------------------------')
# print("\nii.Qual a diferença, por dia da semana, entre o tempo médio e o tempo " \
#       "mínimo da semana?\n")

# print('-----------------------------------------------------')
# #iii Qual a diferença, entre dias úteis e fds, do tempo médio e o tempo mínimo?
# print('-----------------------------------------------------')

# print("\niii.Qual a diferença, entre dias úteis e fds, do tempo médio e o tempo mínimo?\n")

# print('-----------------------------------------------------')
# #iv.Exiba a lista de tempos de sono inferiores a 5h, por dia da semana
# print('-----------------------------------------------------')
# print("\niv.Exiba a lista de tempos de sono inferiores a 5h, por dia da semana\n")

# print('-----------------------------------------------------')
# #v.Exiba a diferença no sábado, em cada semana, entre o tempo de sono da mãe e do pai
# print('-----------------------------------------------------')
# print("\nv.diferença no sábado, em cada semana, entre o tempo de sono da mãe e do pai\n")

# print('-----------------------------------------------------')   
# #vi.Em qual semana houve a menor média de horas de sono? (usar a planilha maeSem)
# print('-----------------------------------------------------')   
# print("\nvi.Em qual semana houve a menor média de horas de sono?\n")

# print('-----------------------------------------------------')   
