# -*- coding: utf-8 -*-

"""
O desempenho dos jogadores de basquete do time RASMUS 
em um certo campeonato com 3 jogos foi registrado em uma planilha 
(arquivo) basquete.xlsx. A primeira coluna tem o nome do jogo (exemplo JOGO 1),
a segunda tem o nome do jogador e a terceira tem o numero de cestas do 
jogador nesse jogo.

Nesse exercicio estaremos interessados em avaliar o desempenho dos jogadores 
no campeonato todo. Sera entao criada uma Series onde o indice sera o nome do 
JOGADOR e o valor o numero de cestas.

Essa series sera criada a partir da planilha, considerando-se apenas as colunas 
1 e 2 da planilha. A coluna com o nome do jogo sera ignorada.

Para isso ao ser feita a leitura a partir do arquivo excel, deve ser informado 
que as colunas de interesse sao a 1 e 2. => usecols=[1,2]

Esse arquivo tambem tem uma linha de cabecalho, com os nomes das colunas. Por 
conta disso, na hora da leitura, ao inves de header=None, devemos indicar 
que a linha de cabecalho e´ a linha 0 => header=0

ATENCAO: sempre antes de exibir alguma resposta, deve ser exibida uma mensagem 
informando o que esta sendo exibido

"""

import pandas as pd
import matplotlib.pyplot as plt

'''
CRIANDO A SERIES 
'''
srCestas = pd.read_excel('basquete.xlsx', header=0,usecols=[1,2],index_col=0,squeeze=True)

'''
1- Exibir a series criada
'''
print('1 - Series criada')


print('*******************************************************************************')
'''
2- Exibir da series srCestas criada:
   tamanho (numero de linhas), numero de linhas validas, os indices, os valores
'''


print('*******************************************************************************')

'''
3- Eliminar da series as linhas sem valor. Exibir a series atualizada
'''


print('*******************************************************************************')
'''
4- A partir da series srCestas criar uma nova series so com as cestas de HANS.
Use o .loc().  Exibir a series do HANS.
'''

print('*******************************************************************************')
'''
5- A partir da series srCestas criar uma nova series (srSemHans) SEM  as cestas do HANS.
Exibir a series criada.
'''

print('*******************************************************************************')
'''
6- Valores como 10, 20 e 30 foram armazenados na planilha original como 'dez', 'vinte'
e 'trinta' . Para manipular os valores da series srCestas devemos ajustar esses valores, 
transformando-os em valores numéricos.
Ideia: fazer uma função para ser aplicada sobre cada valor da series e, caso o valor seja 
'dez', 'vinte' ou 'trinta', retornar o valor numérico correspondente. Caso contrário, 
retornar o próprio valor. Nome da função: ajusta
Aplicar(apply) a função ajusta sobre cada valor, atualizando a propria srCestas.
MAS ATENCAO, nesse caso "inplace=True" nao funciona. 
Fazer srCestas = srCestas.apply(blabla)
Exibir a srCestas ajustada. 
'''



print('*******************************************************************************')
'''
7- Exibir o numero total de cestas do time no campeonato 
'''

print('*******************************************************************************')
'''
8- Considerando todos os jogadores em todos os jogos, responda:
'''
'''
Qual  o maior numero de cestas feitas por um jogador em um unico jogo?
'''
print('8.1-Qual  o maior numero de cestas feitas por um jogador em um unico jogo?')


'''
E qual  foi o jogador com o maior numero de cestas feitas em um unico jogo?
'''
print('8.2-E qual  foi o jogador com o maior numero de cestas  em um unico jogo?')


'''
Qual  o menor numero de cestas  feitas por um jogador em um unico jogo?
'''
print('8.3-Qual  o menor numero de cestas  feitas por um jogador em um unico jogo?')


'''
E qual  foi o jogador com o menor numero de cestas  em um unico jogo?
'''
print('8.4-E qual foi o jogador com o menor numero de cestas em um unico jogo?')

'''
Qual o numero medio de cestas de um jogador por jogo?
'''
print('8.5-Qual o menor numero medio de um jogador por jogo?')


print('*******************************************************************************')
'''
9- Exibir agora medidas interessantes considerando as cestas por JOGADOR (level=0)
'''
'''
9.1 Exibir por JOGADOR: maior numero de cestas em um jogo, menor numero de cestas em 
um jogo, numero medio de cestas em um jogo
'''
print('9.1- Por Jogador: maior numero de cestas, menor numero de cestas e numero medio de cestas')

'''
9.2- A partir da srCestas criar uma nova series srTotalPorJogador, com o total de cestas de cada
jogador no campeonato. Exibir a nova series. 
'''
print('9.2-Total de cestas por jogador no campeonato:')



'''
10 - Exibir gráfico pizza da srTotalPorJogador, ou seja, gráfico com o  
"Total de Cestas por JOGADOR no campeonato")

'''

'''
11 - Construir 3 faixas com a series srTotalPorJogador, nomeando-as de 'pouco', 'normal', 'bom'.
Agrupar por estas faixas e mostrar a quantidade média de cestas de cada faixa, a menor e a maior
pontuação em cada faixa
'''

