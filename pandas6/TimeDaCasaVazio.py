# -*- coding: utf-8 -*-
"""
   Time da Casa
"""

import pandas as pd
import matplotlib.pyplot as plt

'''Considere as informações dos componentes de um time: o nome, altura e idade '''
lnomes=['Nena','Dudu','Lala','Pepa','Gugu', 'Gege','Didi','Gina','Kadu']
lalturas=[1.34, 2.55, 1.52, 1.63, 1.75, 1.66, 2.58,1.75, 1.73]
lidades=[14, 14, 16, 15, 17, 15, 14, 17, 16]

'''Considere a Series das alturas dos componentes de um time: srAltTime '''
srAltTime= pd.Series(lalturas, lnomes)
print('\nSerie Alturas:')


print('\nUma visualizacao da srAltTimes (Barras)')


print('\nAltura da Pepa:')


'''Considere a Series das idades dos componentes de um time: srIdadTime '''
srIdadTime= pd.Series(lidades, lnomes)
print('\nSeries Idades:')


print('\nUma visualizacao da srIdadTime (Barras)')


print('\nIdade da Pepa:')


''' Crie e exiba a tabela de frequencia das idades: tabFreqIdade '''
print('\nTabela de Frequencia das idades')

 
print('\nUma visualizacao da tabFreqIdade (Barras)')


print('\nUma outra visualizacao da tabFreqIdade (Pizza)')


print('Tabela de Frequencia Relativa das Idades (Percentual)')


'''
Trabalhando com series das alturas. Corrigir alturas acima de 2m. Diminua 1m
'''

print('\nAlturas (corrigidas):')


print('\nMaior Altura:')


print('\nTODOS os Individuos com a maior altura: ')


print('\nTodos com altura menor que 1.60')


'''
Crie a Series srFaixaAlt com as seguintes categorias de altura: 
    (0-1.55],(1.55-1.70], (1.70,...]
'''

print('\nFaixas (categorias) de altura')

print('\nTabela de Frequencia das faixas de altura:')


''' Deseja-se saber as seguintes medidas por grupo: quant de elem, alt max, 
alt min, alt media. O grupo é determinado de acordo o nome da seguinte forma:
Considerando: nomes terminados em A - feminino
              nomes terminados em I ou U - masculino
              outros: indeterminado
'''
   
print('\nMedidas: quant de elem, alt max, alt min, alt media por grupo')


''' Deseja-se saber as seguintes medidas por idade: quant de elem, alt max, 
alt min, alt media. Dica: agrupe pela Series srIdadTime
'''
print('\nMedidas: quant de elem, alt max, alt min, alt media por cada uma das idades')

