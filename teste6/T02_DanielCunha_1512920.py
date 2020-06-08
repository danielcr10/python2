"""
Avaliação 06 de INF1026 – 20/05/2020

ATENÇÃO! Leia as instruções abaixo:
1) Duração prevista: 75 minutos. Devido às condições especiais de aulas no momento,
a coordenação oferece aos alunos um total de 6 horas entre a divulgação do teste como
tarefa no EAD e a entrega das respostas;
2) Dê nomes adequados às variáveis;
3) Capriche na organização de seu código;
4) A entrega da questão que compõe este teste tem de ser feita por meio de upload do arquivo
na página de INF1026 no site de EAD. Procure pela tarefa Teste 2 para G2, que se encontra na
seção TESTES/BLOCO 2;
5) Envios feitos por e-mail não serão considerados;
6) OBRIGATORIAMENTE, o nome do arquivo com sua solução tem que ter seu nome
e um sobrenome e sua matrícula conforme exemplo a seguir: T05_MARIAPATINHAS_1012983.py;
7) Preencha, OBRIGATORIAMENTE, as linhas iniciais deste arquivo com os dados pedidos.
8) A ausência da declaração de autoria inviabiliza a correção do mesmo e sua nota será ZERO:
# Nome completo: Daniel Cunha Rios
# Matrícula PUC-Rio: 1512920
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.
"""

import pandas as pd
import matplotlib.pyplot as plt
'''
A Series srDesp foi criada lendo dados do arquivo despesas.xlsx. Na planilha fds desse
arquivo são encontradas as despesas no fim de semana e a forma de pagamento das mesmas.
A primeira linha do arquivo é o cabeçalho. Cada uma das demais linhas contém a forma de
pagamento e o valor da despesa. A Series srDiaUtil foi criada lendo dados do arquivo
despesas.xlsx. Na planilha diaUtil desse arquivo são encontradas as despesas de segunda a
sexta e a forma de pagamento das mesmas. A primeira linha do arquivo é o cabeçalho.
Cada uma das demais linhas contém a forma de pagamento e o valor da despesa.
'''

srDesp = pd.read_excel('teste6/despesas.xlsx',
                       sheet_name='fds', index_col=0, header=0, squeeze=True)
srDiasUteis = pd.read_excel(
    'teste6/despesas.xlsx', sheet_name='diaUtil', index_col=0, header=0, squeeze=True)
print('******************************************************')
print('Exibindo as series construidas')
'''  EXIBIR a series srDesp  '''
print('\n srDesp')
print(srDesp)
print('\n srDiasUteis')
print(srDiasUteis)
''' EXIBIR a despesa total no final de semana  '''
print('\nTotal no FDS:')
print(srDesp.sum())
''' EXIBIR o valor da maior despesa do final de semana  '''
print('\nMaior despesa no FDS:')
print(srDesp.max())

''' EXIBIR a(s) forma(s) de pagamento da maior despesa do final de semana.
Considere a possibilidade de mais de uma.  '''
print('\nFormas de Pagamento da maior despesa no FDS:')
print(srDesp.loc[srDesp == srDesp.max()])
''' EXIBIR apenas as despesas feitas no debito no final de semana '''
print('\nDespesas no debito no FDS:')
print(srDesp.loc['debito'])
''' EXIBIR as despesas que não foram feitas no credito no final de semana '''
print('\nDespesas sem ser no credito no FDS:')
print(srDesp.loc[srDesp.index != 'credito'])
'''   Agora considerando cada forma de pagamento no final de semana  '''
print('\n------------Por Forma de Pagamento------------------')
''' EXIBIR a despesa total no final de semana por FORMA DE PAGAMENTO  '''
print('Total por Forma de Pagamento no FDS:')
print(srDesp.sum(level=0))
''' CRIAR srTabFreqFormasPg com o número de ocorrências de cada forma de pagamento, ou seja, a quantidade de vezes que cada forma de pagamento foi utilizada. EXIBA-A.   '''
print('\nTabela de Frequencia das Formas de Pagamento no FDS')
srTabFreqFormasPg = srDesp.index.value_counts()
print(srTabFreqFormasPg)
''' EXIBIR srTabFreqFormasPg graficamente com gráfico de pizza, com indicação das
porcentagens '''
srTabFreqFormasPg.plot.pie(autopct="%.1f")
# plt.show()
'''  EXIBIR a maior despesa para cada forma de pagamento no FDS'''
print('\nMaior despesa por forma de pagamento no FDS:')
print(srDesp.max(level=0))
'''  EXIBIR uma forma de pagamento em que se gastou menos no total. '''
print('\nUma forma de pagamento em que se gastou menos no total no FDS')
print(srDesp.sum(level=0).idxmin())
'''  EXIBIR a despesa total com a forma de pagamento citada acima. '''
print('\nGasto total nesta forma de pagamento no FDS')
print(srDesp.sum(level=0).min())
print('\n-----Vizualizacao da series srDesp -----------')
print('\nCom gráfico de barras:')
srDesp.sum(level=0).plot.bar()
# plt.show()
'''   Agora considerando as duas Series  '''
''' EXIBIR por forma de pagamento o total gasto '''
print('\nTotal por Forma de Pagamento:')
print(srDesp.append(srDiasUteis).sum(level=0))
print('*******************************************************')
''' Considere as 2 Series criadas abaixo. Ambas contem o nome de um produto e a quantidade
do mesmo. Exiba-as. '''
dicH = {'sabonete': 8, 'desodorante': 2, 'pasta dental': 3}
srHig = pd.Series(dicH)

dicF = {'banana': 13, 'maca': 6, 'pera': 5, 'manga': 8, 'goiaba': 3}
srFruta = pd.Series(dicF)
'''  EXIBIR a series srHig  '''
print('\nSeries srHig')
print(srHig)
'''  EXIBIR a series srFruta  '''
print('\nSeries srFruta')
print(srFruta)
''' Conferindo as quantidades das frutas observou-se alguns enganos. As quantidades pares
precisam ser acrescidas de um valor e as ímpares da metade deste mesmo valor. Acrescente
as quantidades usando uma função denominada acrescenta que recebe o valor como parametro '''
'''  ESCREVER a função acrescenta  '''


def acrescenta(x, y):
    if x % 2 == 0:
        return x + y
    else:
        return x + y/2


''' AlTERAR os valores na Series srFruta. Use 5 como valor a ser passado para a função. '''
print('\nSeries srFruta com as quantidades atualizadas. ')
srFruta = srFruta.apply(acrescenta, args=(5,))
print(srFruta)
''' CRIAR a series srCompras que contém todas as compras, isto é, produtos de higiene
e frutas. Exiba-a. '''
print('\nSeries Compras')
srCompras = srHig.append(srFruta)
print(srCompras)
''' Novas compras apareceram de ultima hora. A Series srAjuste criada abaixo contem este
ajuste.   '''
srAjuste = pd.Series({'sabonete': 6, 'banana': 24, 'cotonete': 1})

''' EXIBIR a srCompras ajustada'''
print('\nsrCompras ajustada')
print(srCompras.add(srAjuste, fill_value=0))
# print(srCompras)
''' EXIBIR apenas os nomes dos produtos cujas quantidades compradas estão entre 5 e 10
unidades inclusive. '''
print('\nNome dos produtos de srCompras entre 5 e 10 quantidades inclusive.')
print(srCompras.loc[srCompras >= 5].loc[srCompras <= 10])
''' CLASSIFICAR a lista de compras em termos das quantidades compradas como sendo:
               menos que 3 - pouca
     entre 3 inclusive e 6 - pequena
     entre 6 inclusive e 10 - muita
     entre 10 inclusive e 20 - grande
             acima de 20 - enorme
'''
s = pd.cut(srCompras, bins=[0, 3, 6, 10, 20, float('inf')], labels=[
           "pouca", "pequena", "muita", "grande", "enorme"])
''' EXIBIR a tabela de frequencia dos produtos em cada uma das classificações '''
print('\nTabela de frequencia dos produtos em cada uma das classificações.')
print(s)
