"""
Pandas1: Gastos do Final de Semana
"""

import pandas as pd
import matplotlib.pyplot as plt
# import os

# diret = os.path.dirname(os.path.realpath(__file__))
# nArq = 'GastosFimDeSemana.xlsx'
# path = os.path.join(diret, nArq)

'''Criar series a partir do arquivo excel '''
srGFS1= pd.read_excel('pandas2/GastosFimDeSemana.xlsx', index_col=0, squeeze=True, header=None, decimal='.')

print('Gastos lidos do arquivo:')
print(srGFS1)

print('\nQuantidade de gastos: (usando size)')
print(srGFS1.size)

print('\nNova series eliminando valor NaN (usando dropna)')
print(srGFS1.dropna())

print('\nQuantidade de gastos validos: (usando size)')
print(srGFS1.dropna().size)

print('\nCriando uma nova series so com gastos de sabado:(usando loc)')
print(srGFS1.loc['SAB'])

print('\nCriando uma nova series SEM os gastos de sabado:(usando drop)')
print(srGFS1.drop(labels=['SAB']))

'''Funcao ajusta: a ser APLICADA sobre cada valor da series. No caso
 do valor ser 'dez' ou 'cem', a nova series retornada terá o valor 
 numérico 10  ou 100. Demais valores serão os mesmos
 '''
def ajusta(x):
  if x == 'dez':
    return 10
  if x == 'cem':
    return 100
  else:
    return x
 
print('\nCria nova series com valores nao numericos ajustados (usando apply com a funcao ajusta)')
srGFS1Ajustada = srGFS1.apply(ajusta)
print(srGFS1Ajustada)

print('\nMEDIDAS INTERESSANTES\n')

print('Total gasto no fim de semana: (usando sum)')
print(srGFS1Ajustada.sum())

print('\nGasto Medio: (usando mean)' )
print(srGFS1Ajustada.mean())

print('\nGasto Maximo: (usando max)')
print(srGFS1Ajustada.max())

print('\nGasto Minimo: (usando min)')
print(srGFS1Ajustada.min())

print('\nGrafico com os gastos do fim de semana (bar)')
srGFS1Ajustada.plot.bar()
plt.title('Gastos')
plt.savefig('pandas2/gastosBar.png')
plt.close()

print('\nMEDIDAS INTERESSANTES POR DIA')

print('\nTotal gasto POR DIA: (usando sum(level=0))')
print(srGFS1Ajustada.sum(level=0))

print('\nGasto Medio POR DIA: (usando mean(level=0))' )
print(srGFS1Ajustada.mean(level=0))

print('\nGasto Maximo POR DIA: (usando max)')
print(srGFS1Ajustada.max(level=0))

print('\nGasto Minimo POR DIA: (usando min)')
print(srGFS1Ajustada.min(level=0))

print('\nTrabalhando com a series do total gasto por dia')

print('\nGrafico do total de gastos por dia (pie)')
plt.title('Gastos por dias')
srGFS1Ajustada.dropna().sum(level=0).plot.pie()
plt.savefig('pandas2/gastosPie.png')
plt.close()