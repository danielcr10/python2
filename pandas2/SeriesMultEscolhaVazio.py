"""
Series: resultados de multipla escolha
"""

import pandas as pd
import os

diret = os.path.dirname(os.path.realpath(__file__))
nArq = 'resMultiplaEscolha.xlsx'
path = os.path.join(diret, nArq)

srResp = pd.read_excel(path, index_col=0, header=None, squeeze=True, decimal='.')

#index_col=0 - indica que a primeira coluna serve de indice
#header=None - nao tem cabeçalho
#squeeze=true - cria como series pq o normal seria cirar um Dataframe

print('---------------- 1 - srResp ----------------------')
print(srResp)

print('---------------- 2 - Eliminando NaN ----------------------')
srRespClean = srResp.dropna()
print(srRespClean)

print('-------------- 3 - Conhecendo a serie --------------------')
print('NUMERO DE LINHAS:')
print(srResp.value_counts())
print('\nVALORES:')

print('\nINDICE:')
print(srResp.index)

print('LISTA DE INDICES:')
print(list(srResp.index))

print('\nOs 4 primeiros:')
print(srResp.head(4))

print('\nOs 3 últimos:')
print(srResp.tail(3))

print('---------------- 4 - Exibindo ordenadamente ----------------------')
print('Ordenada por valores (notas):')    #nao ordena a series, apenas exibe a copia criada ordenada
print(srResp.sort_values())

print('Ordenada DECRESCENTEMENTE por valor:')
print(srResp.sort_values(ascending=False))

print('Ordenada por INDICES (matriculas)')
print(srResp.sort_index())

print('A series propriamente dita não está ordenada:')
print(srResp)

print('---------------- 5 - Tabela de Frequencia ----------------------')
#criar uma series com valor (nota) - quantidade de ocorrencias do valor (nota)
sNova = srResp.value_counts()
sRel = sNova/sNova.sum()*100

print('---------------- 6 - Tabela de Frequencia Relativa/Percentual ----------------------')

print('---------------- 7 - Medidas importantes ----------------------')
print('NOTA MAXIMA:')

print('Tirou nota maxima (apenas 1):')

print('NOTA MINIMA:')

print('Tirou nota minima (apenas 1)')

print('MEDIA:')

print('MODA (MAIS FREQUENTE)')

print('---------------- 8 - Aplicando funcao sobre os valores ----------------------')
# toda nota 2 deve passar a ser 3 e toda nota 4 deve passar a ser 4.5

