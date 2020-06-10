# -*- coding: utf-8 -*-
"""
Avaliação 09 de INF1026 – 10/06/2020

ATENÇÃO! Leia as instruções abaixo:
1) Duração prevista: 45 minutos. Devido às condições especiais de aulas no momento, 
a coordenação oferece aos alunos um total de 6 horas entre a divulgação do teste como 
tarefa no EAD e a entrega das respostas;
2) Dê nomes adequados às variáveis;
3) Capriche na organização de seu código;
4) Nao retire nem altere os prints existentes no template 
5) A entrega da questão que compõe este teste tem de ser feita por meio de upload do arquivo
na página de INF1026 no site de EAD. Procure pela tarefa Teste 5 para G2, que se encontra na
seção TESTES/BLOCO 2;
6) Envios feitos por e-mail não serão considerados;
7) OBRIGATORIAMENTE, o nome do arquivo com sua solução tem que ter seu nome
e um sobrenome e sua matrícula conforme exemplo a seguir: T09_MARIAPATINHAS_1012983.py;
8) Preencha, OBRIGATORIAMENTE, as linhas iniciais deste arquivo com os dados pedidos.
9) A ausência da declaração de autoria inviabiliza a correção do mesmo e sua nota será ZERO:
#Nome completo: Daniel Cunha Rios
#Matrícula PUC-Rio: 1512920
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.
"""

"""
O arquivo NtBlocos contém informações sobre os alunos de uma turma organizadas em 4 planilhas, 
da seguinte forma: 
=> bloco1: notas para compor o grau G1, isto é, nota de uma prova e 3 notas de teste
=> bloco2: notas para compor o grau G2, isto é, nota de uma prova e 3 notas de teste
=> dados: sexo e idade 
=> faltas: numero de faltas
Todas as planilhas tem na primeira coluna os nomes dos alunos.
Para cada uma destas planilhas foi criada uma estrutura de dados da biblioteca Pandas.
Para as 3 primeiras planilhas os respectivos DataFrames: dfBloco1, dfBloco2 e dfDados.
Para a última planilha, a Series srFaltas.
O objetivo final é construir um DataFrame (dfFinal) contendo o grau1, grau2, grau final e a 
situação dos alunos. 
Preencha cada um dos itens solicitados.
"""

'''
ATENÇÃO: SUA SOLUÇÃO TEM QUE MANIPULAR AS ESTRUTURAS DA BIBLIOTECA PANDAS DENOMINADAS 
DATAFRAME OU SERIES E USAR OS MÉTODOS APRESENTADOS E TRABALHADOS NAS AULAS E NO MATERIAL 
DISPONIBILIZADO. NÃO É PERMITIDO TRANSFORMÁ-LAS EM OUTRAS ESTRUTURAS PARA OBTER A RESPOSTA 
PEDIDA.
'''

import pandas as pd
import matplotlib.pyplot as plt

''' Estruturas já criadas '''
dfBloco1= pd.read_excel('NtBlocos.xlsx',sheet_name='bloco1',index_col=0,header=0)
dfBloco1 = pd.DataFrame(dfBloco1)
dfBloco2= pd.read_excel('NtBlocos.xlsx',sheet_name='bloco2',index_col=0,header=0)
dfBloco2 = pd.DataFrame(dfBloco2)
dfDados= pd.read_excel('NtBlocos.xlsx',sheet_name='dados',index_col=0,header=0)
dfDados = pd.DataFrame(dfDados)
srFaltas= pd.read_excel('NtBlocos.xlsx',sheet_name='faltas',squeeze=True,index_col=0,header=0)

'''Exibir as 4 estruturas criadas '''
print('\n1 - dfBloco1')
print(dfBloco1)
print('\n2 - dfBloco2')
print(dfBloco2)
print('\n3 - dfDados')
print(dfDados)
print('\n4 - srFaltas')
print(srFaltas)
'''Renomear as colunas de dfBloco1 para que sejam P1, T1, T2 e T3'''
print('\n5 - dfBloco1 com colunas renomeadas' )
dfBloco1.columns = ['P1', 'T1', 'T2', 'T3']
print(dfBloco1)
'''Renomear as colunas de dfBloco2 para que sejam P2, T1, T2, T3'''
print('\n6 - dfBloco2 com colunas renomeadas' )
dfBloco2.columns = ['P2', 'T1', 'T2', 'T3']
print(dfBloco2)
''' Substituir no dfBloco1 e no dfBloco2 notas ausentes por 0 (zero)  '''
print('\n7 - dfBloco1 sem valores ausentes')
dfBloco1.fillna(value=0, inplace=True)
print(dfBloco1)

print('\n8 - dfBloco2 sem valores ausentes')
dfBloco2.fillna(value=0, inplace=True)
print(dfBloco2)

''' Incluir tanto em dfBloco1 como no dfBloco2 uma coluna denominada MTestes que contém a 
media aritmetica das 2 maiores notas de testes '''
print('\n9 - dfBloco1 com nova coluna MTestes ') 
dfBloco1['MTestes'] = (dfBloco1[['T1', 'T2', 'T3']].sum(axis=1) - dfBloco1[['T1', 'T2', 'T3']].min(axis=1))/2
print(dfBloco1)

print('\n10 - dfBloco2 com nova coluna MTestes ')
dfBloco2['MTestes'] = (dfBloco2[['T1', 'T2', 'T3']].sum(axis=1) - dfBloco2[['T1', 'T2', 'T3']].min(axis=1))/2
print(dfBloco2)

''' Incluir em dfBloco1 a coluna G1. Esta coluna armazena a nota da prova somada à 20% da media dos testes '''
print('\n11 - dfBloco1 com nova coluna G1 ')
dfBloco1['G1'] = dfBloco1['P1'] + dfBloco1['MTestes']*0.2
print(dfBloco1)

''' Incluir em dfBloco2 a coluna G2. Esta coluna armazena a nota da prova somada à 20% da media dos testes '''
print('\n12 - dfBloco2 com nova coluna G2 ')
dfBloco2['G2'] = dfBloco2['P2'] + dfBloco2['MTestes']*0.2
print(dfBloco2)

''' Criar dfGeral apenas com as colunas G1, G2 e FALTAS. Use o metodo concat da forma mais apropriada ''' 
print('\n13 - dfGeral ')
dfGeral = pd.DataFrame()
dfGeral['G1'] = dfBloco1['G1']
dfGeral['G2'] = dfBloco2['G2']
dfGeral['FALTAS'] = srFaltas.values
print(dfGeral)

''' Incluir em dfGeral a coluna GParcial cujos valores são a media ponderada de G1 e G2, 
sendo G1 com peso 2 e G2 com peso 3  ''' 
print('\n14 - dfGeral com coluna GParcial')
dfGeral['GParcial'] = (dfGeral['G1']*2 + dfGeral['G2']*3)/5
print(dfGeral)

''' Incluir em dfGeral a coluna SitParc com a situação de cada aluno:
    . FINAL se 0 <= grau parcial(GPARCIAL) <= 6.0
    . APV_REG se 6 < grau parcial(GPARCIAL) <= 8.0 
    . APV_MBOM se 8 < grau parcial(GPARCIAL) <= 10.0 '''
print('\n15 - dfGeral com coluna SitParc (Situacao Parcial)')
for index, row in dfGeral.iterrows():
    if 0 <= row['GParcial'] <= 6:
        dfGeral.loc[index,'SitParc'] = 'FINAL'
    if 6 < row['GParcial'] <= 8:
        dfGeral.loc[index,'SitParc'] = 'APV_REG'
    if 8 < row['GParcial'] <= 10:
        dfGeral.loc[index,'SitParc'] = 'APV_MBOM'
print(dfGeral)
'''
Exibir graficamente (barras) num único grafico apenas as notas de G1 e de G2  '''
print('\n16 - Grafico de barras de G1 e G2 ')
dfGeral.plot.bar()
plt.show()

''' Incluir em dfGeral a coluna GFinal. O grau final (GFinal) dos aluno é calculado 
acrescentando no máximo 0.5 ao grau parcial de acordo com a frequencia. Tem direito 
a este acrescimo os alunos que tiveram até 2 faltas inclusive, desde que seu grau 
final não ultrapasse a nota 10 (nota maximo). Esta coluna tem que ser criada por 
meio de uma função e o método apply '''


print('\n17 - dfGeral com coluna GFinal (Grau Final) ')


''' Exibir para cada aluno o valor do maior grau entre G1 e G2 ''' 
print('\n18 - Aluno e o valor do maior grau: G1 ou G2 ')


''' Exibir a quantidade de alunos por idade (tabela de frequencia) '''
print('\n19 - Quantidade de alunos por idade ')


'''Exibir graficamente (pizza) o percentual de meninas e de meninos '''
print('\n20 - Graficamente o percentual de meninas e de meninos')


''' Incluir em dfGeral a coluna SitFinal com a situação de cada aluno:
    . FINAL se 0 <= grau final(GFinal) <= 6.0
    . APV_REG se 6 < grau final(GFinal) <= 8.0 
    . APV_MBOM se 8 < grau final(GFinal) <= 10.0 '''
print('\n21 - dfGeral com coluna SitFinal (Situacao Final)')

''' Para observar o impacto da frequencia no grau do aluno exibir as colunas GParcial, 
SitParc, GFinal e SitFinal  do dfGeral '''
print('\n22 - Impacto da frequencia no grau do aluno')

''' Elimine as colunas GParcial e SitParc. Exiba dfGeral atualizado  '''
print('\n23 - dfGeral final')

