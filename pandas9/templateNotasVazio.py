# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 10:11:03 2017

@author: claudia ferlin
"""

import pandas as pd
import matplotlib.pyplot as plt

lNtA=[['Lalá', 133,2,6.2, 6.9, 9.2], 
      ['Lelé',131, 4,6.5, 2.7, 3.0], 
      ['Lili',135, 9,1.3, 4.6,5.0]]
lNtO =[['Luisinho',230,1, 9.8,3.7,9.3],
       ['Zezinho',215,5,6.2,1.3,8.5],
       ['Huguinho',216,6,9.6,3.8,1.0]]

indMatrA=[133,131,135]
indMatrO=[230,215,216]

dfNtA=pd.DataFrame(lNtA,columns=['Nome','Matr','Faltas','P1','P2','P3'],index=indMatrA)
dfNtO=pd.DataFrame(lNtO,columns=['Nome','Matr','Faltas','P1','P2','P3'],index=indMatrO)

print('1 - DataFrame dfNtA:\n' )

print('\n2 - DataFrame dfNtO:\n' )

#------------------------------------------------------------------------------
#  Criar DataFrame dfTarde, a partir do excel:
#    A primeira planilha do arquivo NotasAlunoTardeOrig.xlsx contém as notas dos alunos da tarde.
#    O arquivo contém linha de cabeçalho e as linhas devem ser indexadas pela matrícula (coluna 1)
#-------------------------------------------------------------------------------
dfTarde=pd.read_excel("NotasAlunoTardeOrig.xlsx",header=0,decimal=',',index_col=1)
print('\n3 - DataFrame dfTarde:\n' )

#------------------------------------------------------------------------------
#   VISUALIZANDO
#------------------------------------------------------------------------------
# Mostrar o DataFrame dfNtA graficamente (grafico de barras)
#  Cada coluna em um gráfico (Observe quais colunas foram exibidas e se todas tem sentido)

print('\n4 - dfNtA graficamente e um por coluna:\n' )

# O Nome foi exibido?
# Tem sentido a matrícula ser exibida?

# Todas as colunas em um grafico
print('\n5 - dfNtA graficamente e juntos:\n' )

#-------------------------------------------------------------------------------
# Mostrar APENAS as notas do dfNtA graficamente. Todas juntas. Observe quem é o eixo x
print('\n6 - dfNtA (apenas as notas) graficamente e juntos:\n' )

# Mostrar APENAS as notas do dfNtA graficamente, com as Provas como eixo X. Um grafico.
#Solução 1
print('\n7 - dfNtA graficamente e juntos. Provas no eixo x - solucao 1-seleciona as colunas e transpoe:\n' )

#Solução 2
print('\n8 - dfNtA graficamente e juntos. Provas no eixo x - solucao 2-transpoe e seleciona os indices:\n' )

# Mostrar APENAS as notas da Lalá (matr: 133) e da Lili (matr: 135) graficamente. Um grafico.
print('\n9 - dfNtA graficamente. Notas da Lalá e da Lili:\n' )

# Verificar graficamente (scatter) a influência das faltas nas notas da P1, na turma da tarde
# Depois da P2 e depois da P3
print('\n10 - dfTarde graficamente analisando Faltas e P1:\n' )

print('\n11 - dfTarde graficamente analisando Faltas e P2:\n' )

print('\n12 - dfTarde graficamente analisando Faltas e P3:\n' )

#------------------------------------------------------------------------------
#   INSERINDO/SELECIONANDO/ALTERANDO/DESCARTANDO/REARRUMANDO o dfNtA
#----------------------------------------------------------------------------

#incluir no dfNtA, o número da turma: A  
print("\n13 - dfNtA com a turma\n")

#Como deixar a turma como 1ª coluna? Lembre-se que você pode selecionar as colunas em qualquer ordem
print("\n14 - dfNtA com colunas arrumadas\n")

#incluir no dfNtA, a Loló com matr 139, faltas None, P1=10, P2=9, P3=10
print("\n15 - dfNtA com Loló\n")

#incluir no dfTarde, como coluna, a matricula dos alunos e arrumar na mesma ordem da dfNtA
print("\n16 - dfTarde com colunas arrumadas e com coluna Matr\n")

## DESCARTANDO/ PREENCHENDO
'''
#Qual o resultado das instruções a seguir?
# Executes-as uma a uma
dfC=dfNtA.copy()
#Excluindo uma coluna
dfC=dfC.drop('Faltas',axis=1)
#Incluindo novas linhas
dfC.loc[996]=['A','$$$', 996,8, 9.2,None]
dfC.loc[997]=['A','???', 999,None, 9.2,0]
dfC.loc[998]=['A',None, None,None, None,None]
#incluindo nova coluna
dfC['Ex']=None
print("\n dfC\n",dfC)

print("\n\nDropna:Como todas linhas/colunas tem NaN, fica vazio\n",dfC.dropna())
print("\n\ndfC continua com valores\n",dfC)

#   dfC.dropna(axis=0)  ou dfC.dropna(axis='index')
#  Especifica o eixo ao longo do qual os elementos serão eliminados. 
#  Dropna por axis=0 (que é o mesmo que axis='index') significa que vai
#  eliminar todas as linhas que tenham NaN. Como todas linhas tem NaN, o df resultante é vazio
print("\n\nDropna por axis=0 (que é o mesmo que axis='index'). Como todas linhas tem NaN, fica vazio\n",dfC.dropna(axis='index'))
print("\n\ndfC continua com valores\n",dfC)

#   dfC.dropna(axis=1)  ou dfC.dropna(axis='columns')
#  Especifica o eixo ao longo do qual os elementos serão eliminados. 
#  Dropna por axis=1 (que é o mesmo que axis='columns') significa que vai
#  eliminar todas as colunas que tenham NaN. Como há colunas sem NaN, 
#  o df resultante não é vazio
print("\n\nDropna por axis=1((que é o mesmo que axis='columns').Como há colunas sem NaN, mostra o que sobrou\n",dfC.dropna(axis='columns'))
print("\n\ndfC continua com valores\n",dfC)

dfC.loc[998,'Turma']=None
print("Alterando a turma do 998\n",dfC)
#   Agora dfC tem:
#       a linha 998 (última) toda com NaN e 
#       a última coluna(Ex) tb toda com NaN
# 
print("\n ENTENDENDO o how='all': só elimina se TODOS no eixo são NaN\n")

print("\n\nDropna: dropna(how='all')\n",dfC.dropna(how='all'))

print("\n\nDropna: dfC.dropna(how='all',inplace=True)\n",dfC.dropna(how='all',inplace=True))
print("\n\ndfC sem  última linha\n",dfC)

print("\n\nDropna: dfC.dropna(axis=1,how='all'):\n",dfC.dropna(axis='columns',how='all',inplace=True))
print("\n\ndfC sem  última coluna\n",dfC)

print("\n ENTENDENDO o how='any': elimina se há um elemento NaN no eixo\n")

print("\n\nDropna: dfC.dropna(how='any',axis=1) sai coluna P1 e P3)\n",dfC.dropna(how='any',axis='columns'))

print("\n\nDropna: dfC.dropna(axis=0,how='any') sai linha 996,997\n",dfC.dropna(axis='index',how='any'))

#Trocar NaN por valor dependendo da coluna P1->0, P2->-1, P3->-2
print("\n - Trocando NaN por valor dependendo da coluna P1->0, P2->-1, P3->-2\n")
'''
#Criar uma cópia do dfNtA (dfAC) e incluir a coluna Media com a média ponderada (2,3,4) das Provas.
#Crie a funcao medPond e use apply.
print("\n18 - Copia de dfNtA com coluna com a média de provas ponderada\n")

#Criar uma cópia do dfTarde (dfTC) e incluir a coluna Media com a média ponderada (2,3,4) das Provas.
print("\n19 - Copia de dfTarde com coluna com a média de provas ponderada\n")

#Ordenar dfAC pela Média. Critério de desempate P3/P2/P1
print("\n20 - dfNtA ordenado por Média/P3/P2/P1\n")

# Preencher os valores ausentes em Faltas como 0 (dfNtA)
print("\n21 - dfNtA com valores ausentes preenchidos com 0\n")

#------------------------------------------------------------------------------
#   CONCATENANDO
#------------------------------------------------------------------------------

#Concatenar  dfNtA e dfNtO ==> dfManha rearrumando como Turma,Nome,Faltas,Matr,P1,P2,P3
print("\n22 - dfManha com colunas rearrumadas\n")

# Execute com ignore_index = True ==>dfManhaI
print("\n23 - dfManhaI com colunas rearrumadas e ignore_index\n")

#------------------------------------------------------------------------------
#  Criando DataFrame dfNtE, com as notas da recuperação a partir do excel:
#     A primeira planilha do arquivo NotasAlunoCursoExtra.xlsx contém as notas dos alunos 
#     que fizeram recuperação.
#     O arquivo contém linha de cabeçalho e as linhas devem ser indexadas pela matrícula (coluna 1)
#  Após criar o DF, incluir como coluna do DF a matrícula e rearrumar como Turma,Nome,Matr,P1,P2,P3
#------------------------------------------------------------------------------
dfNtE=pd.read_excel("NotasAlunoCursoExtra.xlsx", decimal=',',index_col=1)

print("\n24 - dfNtE com coluna matricula e rearrumada\n")

#------------------------------------------------------------------------------
#  A nota final de P1,P2 e P3 dos alunos que fizeram recuperação será a maior
#  nota entre a nota de Pi (dfManha ou dfTarde) e da respectiva Pi da recuperação (dfNtE)
#   Possível solução (faca separadamente para dfManha e depois dfTarde):  
#    criar um dfAux que é concatenação apenas das linhas/colunas entre dfManha ou dfTarde e dfNtE
#    encontrar a maior nota entre as repectivas Pi de dfAux                      
#    substituir em dfManha ou dfTarde os registros que constam em dfAux
#------------------------------------------------------------------------------

print("\n25 - dfManha atualizado com a nota da recuperação\n")

print("\n26 - dfTarde atualizado com a nota da recuperação\n")

#Concatenar dfManha com as Notas dos Testes do arquivo TestesAlunos planilhas 'A' e 'O'
#   Possível solução:
#       criar df com os testes dos meninos e das meninas, separadamente, a partir das planilhas
#       excluir a coluna Nome em ambos
#       criar dfT com os testes de todos os alunos da manha
#       concatenar Notas das Provas (dfManha) com Notas de Testes atualizando dfManha
dfTA=pd.read_excel("TestesAlunos.xlsx", sheetname='A', decimal=',',index_col=0)
dfTO=pd.read_excel("TestesAlunos.xlsx", sheetname='O', decimal=',',index_col=0)

print("\n27 - dfTodos da Manhã com provas e testes\n")

#  Concatenar as Turmas da Manhã (dfManha) com a turma da Tarde(dfTarde), criando
#  dfGeral e indicando o turno (Manhã e Tarde) como um nivel de índice 
print('\n28 - dfgeral: alunos dos Dois Turnos\n')

# Preencher os valores ausentes de dfGeral: Turma como O e de Teste como 0
print("\n29 - dfGeral Corrigidos\n")

#------------------------------------------------------------------------------
#   OPERANDO/TRANSFORMANDO/RESUMINDO
#------------------------------------------------------------------------------
# Calcule e inclua em dfGeral as Notas G1,G2 e G3 ==> Ti*0.2 + Pi*0.8
print("\n30 - dfGeral com G1,G2 e G3\n")

# Calcule a Média de cada aluno e inclua uma coluna com a mesma
print("\n31 - dfGeral com a media de cada aluno\n")





