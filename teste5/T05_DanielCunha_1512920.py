# -*- coding: utf-8 -*-
"""
Avaliação 05 de INF1026 – 13/05/2020

ATENÇÃO! Leia as instruções abaixo:
1) Duração prevista: 40 minutos. Devido às condições especiais de aulas no
momento, a coordenação oferece aos alunos um total de 6 horas entre a divulgação
do teste como tarefa no EAD e a entrega das respostas;
2) Dê nomes adequados às variáveis;
3) Capriche na organização de seu código;
4) A entrega da questão que compõe este teste tem de ser feita por meio de
upload do arquivo na página de INF1026 no site de EAD. Procure pela tarefa
Teste 1 para G2, que se encontra na seção TESTES/BLOCO 2;
5) Envios feitos por e-mail não serão considerados;
6) OBRIGATORIAMENTE, o nome do arquivo com sua solução tem que ter seu nome
e um sobrenome e sua matrícula conforme exemplo a seguir: T05_MARIAPATINHAS_1012983.py;
7) Preencha, OBRIGATORIAMENTE, as linhas iniciais deste arquivo com os dados
pedidos.
8) A ausência da declaração de autoria inviabiliza a correção do mesmo e sua nota será ZERO:
#Nome completo: Daniel Cunha Rios
#Matrícula PUC-Rio: 1512920
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.
"""

import pandas as pd
import matplotlib.pyplot as plt

'''  
A Series srAleCurso foi criada lendo dados do arquivo alunosecursos.xlsx. 
Cada linha tem o nome do aluno e seu curso. 
'''
srAleCurso = pd.read_excel(
    'teste5/alunosecursos.xlsx', index_col=0, header=None, squeeze=True)

print('******************************************************')
print('Exibindo a series construida')
'''  EXIBIR a series criada  '''
print(srAleCurso)
'''  EXIBIR as 4 primeiras linhas da srAleCurso  '''
print(srAleCurso.head(4))
'''  EXIBIR as 3 ultimas linhas da srAleCurso  '''
print(srAleCurso.tail(3))
print('***********************************************************')
print('Indices, Valores, Numero de Linhas')
''' EXIBIR os indices da srAleCurso:   '''
print(srAleCurso.index)
''' EXIBIR os valores da srAleCurso:   '''
print(srAleCurso.values)
''' EXIBIR tamanho (numero de linhas) da series:   '''
print(srAleCurso.size)
print('******************************************************')
''' EXIBIR o curso do aluno de nome LINO :  '''
print(srAleCurso.loc['LINO'])
''' EXIBIR o curso do aluno de nome PEPA :  '''
print(srAleCurso.loc['PEPA'])
print('***********************************************************')
print('Eliminando: ')
''' ELIMINAR de srAleCurso linhas com curso nao preenchido: '''
srAleCurso.dropna(inplace=True)
''' EXIBIR srAleCurso atualizada '''
print(srAleCurso)
''' CRIAR sCopia como sendo uma copia de srAleCurso '''
sCopia = srAleCurso.copy()
''' ELIMINAR de sCopia os alunos VAVA, LUNA, DEDE em um comando  '''
sCopia.drop(labels=['VAVA', 'LUNA', 'DEDE'], inplace=True)
''' EXIBIR a sCopia depois das eliminacoes '''
print(sCopia)
''' EXIBIR o tamanho da sCopia depois das eliminacoes '''
print(sCopia.size)
print('***********************************************************')
''' EXIBIR srAleCurso original novamente, continuaremos com ela '''
print(srAleCurso)
print('***********************************************************')
print('ORDENANDO:')
''' Exibir srAleCurso ordenada por indices  '''
print(srAleCurso.sort_index())
''' Exibir srAleCurso ordenada pelos valores  '''
print(srAleCurso.sort_values())
print('***********************************************************')
'''  
A Series srNotas foi criada lendo dados do arquivo NotasCurso.xlsx. 
Cada linha tem o nome do aluno e sua nota. 
'''
srNotas = pd.read_excel('teste5/NotasCurso.xlsx', squeeze=True,
                        header=None, index_col=0)
''' INCLUIR o aluno JOCA com nota 7.1
'''
srNotas.loc['JOCA'] = 7.1
''' EXIBIR a srNotas depois da inclusão
'''
print(srNotas)
''' EXIBIR a nota do 5o. colocado ao 10o. colocado com um unico comando. Considere como 
1o. colocado o com maior nota:  
'''
print(srNotas.sort_values(ascending=False).iloc[4:10])
''' ALTERAR a nota dos 4 melhores alunos. A nova nota eh 10
      OU
    ALTERAR a nota dos 4 primeiros colocados. A nova nota eh 10.
'''
# srNotasOrdenado = srNotas.sort_values(ascending=False)
srNotas = srNotas.sort_values(ascending=False)
# mudar = srNotasOrdenado.index[0:4]
# srNotas.loc[mudar] = 10.0
srNotas.iloc[0:4] = 10.0
''' EXIBIR a srNotas depois da alteração
'''
print(srNotas)
print('VISUALIZANDO:')
''' VISUALIZANDO como grafico de barras com o nome dos alunos em ordem alfabética
'''
srNotas.sort_index().plot.bar()
plt.show()
''' VISUALIZANDO como grafico de pizza com valores percentuais 
'''
srNotas.plot.pie(autopct="%.1f")
plt.show()
