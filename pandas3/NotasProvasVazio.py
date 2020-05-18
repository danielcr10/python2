"""   Exercicio de Pandas: Series com planilha de notas   """

import pandas as pd
import matplotlib.pyplot  as plt

srNotasRasc = pd.read_excel('NotasProva1.xlsx', squeeze=True, header=None, index_col=0, decimal = '.')

print('Notas Lidas')

print('Total de Notas Lidas')

print('Notas Validas (Sem Faltas)')

print('Total de Notas Validas')


# exibir graficamente as notas validas: line, bar, barh
    
print('  TRABALHANDO COM AS SEGUINTES FAIXAS DE VALORES: 0,3,5,7,9,10 ')

print('Tabela de frequencias por faixa ')

print('Tabela de frequencias por faixa: ordenada por indice')

# exibir graficamente, por faixa, as notas validas: line, bar, barh


# criar uma copia da Series com as notas validas e exibir.
print("COPIA")

# Considere a Serie criada e exibida abaixo. A mesma contem pontos a serem acrescentados
#a nota de alguns alunos.
srOutra=pd.Series({'JUJU':2.2,'LUKA':0.5})
print('\nOUTRA SERIE: acrescimos por erro na contagem de pontos')
print(srOutra)

# criar e exibir a Serie srSoma1 que contem os acrescimos, usando +
print("\nSOMANDO com +")

# criar a Serie srSoma2 que contem os acrescimos, usando add e fill_value=0
print('\nSOMANDO com add - fill_value=0')

print("\nEXIBINDO ORDENADO POR NOTA")

print("\nEXIBINDO ORDENADO NOME DECRESCENTEMENTE")

# Considere a Serie criada abaixo. Exiba-a.
srSegCham=pd.Series({'DADA':5.6,'VIVI':7.8,'NENA':6.1})
print('\nSEGUNDA CHAMADA')

print('\nACRESCENTANDO SEG CHAMADA: append')

print('\nORDENANDO POR NOME E EXIBINDO')

# Considere a Serie criada abaixo. Exiba-a.
srRevisao=pd.Series({'BUBA':6.1, 'NENA':7.2})
print('\nREVISAO')

print('\nALTERANDO NOTAS DEPOIS DA REVISAO: update')

# usando FILTRO
print("\nUsando FILTRO: (Series booleana)aprovado?")

print("\nAPROVADOS")

print("\nREPROVADOS")

