# -*- coding: utf-8 -*-
"""
DataFrame Corredores
"""

import pandas as pd
import matplotlib.pyplot as plt
dfCorredores = pd.read_excel('corredores.xlsx',index_col=0,header =0,decimal ='.') 

print('\n1- DataFrame dfCorredores')


print('\n2-index renomeado para num')


print('\n3- Nome do(s) vencedor(es) da corrida e melhor tempo')


print('\n4- Nomes dos corredores com melhor desempenho na corrida do que no melhor treino')


print('\n5-Dataframe so com os que tiveram desempenho na corrida pior ou igual a media dos treinos')


print('\n6-Nome dos corredores que tiveram a maior diferenca entre o seu melhor treino e a corrida')
print('(para mais ou para menos)')




