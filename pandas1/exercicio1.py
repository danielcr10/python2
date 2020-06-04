# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:55:36 2017

@author: claudia ferlin
"""
import pandas as pd

sF1_l=pd.Series([9217, 1118, 665, 3348, 3599])

df1Paint={'jpg':665,'png':3348,'bmp':9217,'gif':1118,'tif':3599}
sF1_d=pd.Series(df1Paint)

dInsc={'33A':40,'33C':40,'33F':16,'33B':15,'33E':None,'A44':None,'A33':25}
sInsc=pd.Series(dInsc)

sGnum = pd.Series([10.0,23.0,22.4,10.0,15.0,12.0,25.0])
sGdia = pd.Series([10.0,23.0,22.4,10.0,15.0,12.0,25.0], 
                  index=['Seg','Ter','Qua','Qui','Sex','Sab','Dom'])

l=[('Pão',40),('Leite',5),('Café',1.0),('Frios',1.5),('Queijo',2.0),('Ovos',12)]
dCompras=dict(l)
sCompras=pd.Series(dCompras)

sGastos = pd.Series([10,11,10,20,21,20,31,30,30,40,44,45,51,50,54],
                    index=['s','t','q','s','t','q','s','t','q','s','d','q','s','t','d'])


# Selecionando itens
# Series sGnum
# Mostrar 3º elemento

#Mostrar os 2 primeiros elementos

#Mostrar o 1º e o 3º elementos


# Series sGdia
#Usando os índices
# Mostrar 3º elemento

#Mostrar os 2 primeiros elementos

#Mostrar o 1º e o 3º elementos

#Usando as posições
#Mostrar 3º elemento

#Mostrar os 2 primeiros elementos

#Mostrar o 1º e o 3º elementos


#Iterando sobre a Series
#Mostrar todos os elementos da Series sCompras por linha,formatado em ordem
# crescente de nome de produto 

#Alterando/incluindo/ordenando elementos nas Series sInsc
#O número de inscritos na 33E agora são 18

#Há uma nova turma 33G, com 9 matriculados

#Eliminar turmas sem alunos

#Mostrar a Series sInsc em ordem decrescente de quantidade de alunos matriculados


#Exibir graficamente as Series sCompras e sGastos, em formatos distintos


#Exibir numericamente o total, a média, mediana, moda, maior e menor valores das Series sCompras e sGastos
