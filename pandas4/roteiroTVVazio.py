
"""
TVs e Precos
"""

import pandas as pd
import matplotlib.pyplot as plt

''' Crie uma series (srTVs) a partir do arquivo excel PrecoTV.xlxs disponibilizado. Nesse arquivo sao encontrados os modelos de TV existententes em uma determinada loja e seus respectivos precos
'''
srTVs = pd.read_excel("pandas4/PrecoTV.xlsx", header=None,
                      index_col=0, squeeze=True)
'''  Exiba a series criada  '''
# print(srTVs)
'''  Elimine da series os dados sem valor (NaN). Não esqueca de atualizar a series srTVS '''
srTVs.dropna(inplace=True)
''' Exiba a series '''
# print(srTVs)
''' Exiba a tv mais cara e seu valor '''
tv = srTVs.idxmax()
preco = srTVs.max()
print("{} - {}".format(tv, preco))
''' Exiba a tv mais barata e seu valor '''
tv = srTVs.idxmin()
preco = srTVs.min()
print("{} - {}".format(tv, preco))
''' Crie uma nova series (srFaixaDePreco) com as categorias de preco 
[(0.0, 1500.0] < (1500.0, 2500.0] < (2500.0, 3500.0] < (3500.0, srTvs.max()]] '''

''' Crie uma nova series (srFreq) correspondente a tabela de frequencias das categorias 
de preco a partir da series das categorias (srFaixaDePreco). Utilize o metodo value_counts() '''

''' Exiba a tabela de frequencias (srFreq) '''

'''  Na series original (srTVS) cada indice e´ um  nome de modelo de TV, que tem sempre incluido
o tamanho da tela. Por exemplo se o modelo e´ JG49HD5000 o tamanho da tela e´ 49 polegadas. 
No arquivo so ha TVs de 40,43,49 e 55.
Os dados devem ser  agrupados pelo tamanho da tela. Para isso deve primeiro ser escrita a 
funcao tela que sera utilizada pelo metodo groupby. Essa funcao recebe (implicitamente) o 
indice (nome do modelo) da series e retorna um inteiro correspondente ao tamanho da tela.  '''
'''   Escreva a funcao tela como descrita   '''

'''  Crie agora um agrupamento (grTela) pelo tamanho da tela a partir da series original (srTVs).
Deve ser utilizado o metodo groupby, passando a funcao tela como argumento  '''

'''  Exiba os grupos criados (grTela.groups)  '''

'''  Exiba os indices dos grupos criados (grTela.indices)  '''

'''  Para cada grupo criado  exiba: quantidade de elementos no grupo (count), preco minimo (min), 
modelo com preco minimo (idxmin), preco maximo (max), modelo com preco maximo (idxmax)
Para obter essas informacoes  a partir do agrupamento criado (grTela) deve ser utilizado o metodo
agg, sendo fornecida a lista com as funcoes de agregacao relacionadas acima['count','min','idxmin', 'max', 'idxmax'] )
'''

'''
Leia do teclado o tamanho da tela desejada (inteiro)
'''

''' Crie uma series (srTelaDesejada) com modelos e precos da tela desejada. Para isso a partir 
do agrupamento criado (grTela) utilize o metodo get_group, fornecendo a tela desejada '''

''' Exiba a series criada '''

''' Exiba a series criada ordenada pelo preco (use sort_values()) '''

''' Leia do teclado um limite superior de preco (limPreco)  '''

'''  Fazendo uso de um filtro exiba todos os modelos e precos da tela desejada com precos abaixo
de limPreco'''
