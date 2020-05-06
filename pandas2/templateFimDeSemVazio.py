"""
Pandas1: Gastos do Final de Semana
"""

import pandas as pd
import matplotlib.pyplot as plt

'''Criar series a partir do arquivo excel '''
srGFS1= pd.read_excel('GastosFimDeSemana.xlsx',index_col=0,squeeze=True,
                       header=None, decimal='.')

print('Gastos lidos do arquivo:')


print('\nQuantidade de gastos: (usando size)')


print('\nNova series eliminando valor NaN (usando dropna)')


print('\nQuantidade de gastos validos: (usando size)')


print('\nCriando uma nova series so com gastos de sabado:(usando loc)')


print('\nCriando uma nova series SEM os gastos de sabado:(usando drop)')


'''Funcao ajusta: a ser APLICADA sobre cada valor da series. No caso
 do valor ser 'dez' ou 'cem', a nova series retornada terá o valor 
 numérico 10  ou 100. Demais valores serão os mesmos
 '''
 
print('\nCria nova series com valores nao numericos ajustados (usando apply com a funcao ajusta)')


print('\nMEDIDAS INTERESSANTES\n')

print('Total gasto no fim de semana: (usando sum)')


print('\nGasto Medio: (usando mean)' )


print('\nGasto Maximo: (usando max)')


print('\nGasto Minimo: (usando min)')


print('\nGrafico com os gastos do fim de semana (bar)')


print('\nMEDIDAS INTERESSANTES POR DIA')

print('\nTotal gasto POR DIA: (usando sum(level=0))')


print('\nGasto Medio POR DIA: (usando mean(level=0))' )


print('\nGasto Maximo POR DIA: (usando max)')


print('\nGasto Minimo POR DIA: (usando min)')


print('\nTrabalhando com a series do total gasto por dia')


print('\nGrafico do total de gastos por dia (pie)')

