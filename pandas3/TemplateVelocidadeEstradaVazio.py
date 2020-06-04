# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:27:43 2018

@author: claudia ferlin
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
#
# Durante 3 dias, um radar da polícia rodoviária registrou as velocidades (em km/h) de veículos
# em uma rodovia, armazenando-as em 3 planilhas excel: dia1.xlsx, dia2.xlsx, dia3,xlsx
#
# ============================================

# ============================================
# Construindo  Series a partir de um arquivo excel
# ============================================
#
# ============================================
#       Manipulando a series do dia3
# ============================================
#   Utilizar a planilha excel dias3.xlsx para  criar a Series sDia3
#       índice: coluna 0 (hora) e valor coluna 1 (vel)- tem linha de cabeçalho
#   Mostrar 10ºs elementos
#
print("vai")
sDia3 = pd.read_excel('pandas3/dia3.xlsx', header=0, index_col=0,
                      squeeze=True, decimal=',')
print(sDia3.head(10))

#   Exibir graficamente (barras horizontal)
print('\n--------------------------------------------------\n')

sDia3.plot.barh()
plt.title('Dia 3')
plt.show()

print('\n-------------------------------------------------\n')

# ============================================
#       Responder as seguintes perguntas sobre sDia3:
# ============================================
#

# %% Outra coisada
print('\n--------------------------------------------------\n')
print("Quantos carros foram registrados?")
print(sDia3.count())
print('\n--------------------------------------------------\n')

print('\n--------------------------------------------------\n')
print("Qual a velocidade média por dia?")
print(sDia3.mean())
print('\n--------------------------------------------------\n')

print('\n--------------------------------------------------\n')
print("Qual a velocidade média por hora? Exibi-las também graficamente(barra)")
sDia3Hora = sDia3.mean(level=0)
sDia3Hora.plot.bar()
plt.title('Dia 3 - Velocidade media/hora')
plt.show()
plt.savefig('pandas3/bar3VelHora.png')  # apagar
plt.close()
print('\n--------------------------------------------------\n')
# %% Outra coisada

print('\n--------------------------------------------------\n')
print("Qual a velocidade mais frequente?")
print(sDia3.mode())
print('\n--------------------------------------------------\n')

print('\n--------------------------------------------------\n')
print("Qual a maior velocidade registrada? Em qual hora?")
velMax = sDia3.max()
print(sDia3.max())
print(sDia3.idxmax())
print('\n--------------------------------------------------\n')

print('\n--------------------------------------------------\n')
#   Qual a maior velocidade registrada por hora?
print(sDia3.max(level=0))
print('\n--------------------------------------------------\n')

print('\n--------------------------------------------------\n')
print("Em qual hora foi registrada a menor velocidade?")
print(sDia3.idxmin())
print('\n--------------------------------------------------\n')

# %% Usando o apply sobre sDia3
# ============================================
#       Usando o apply sobre sDia3
# ============================================
# Conferindo os valores, observou-se que o radar aumentava em 10% o valor medido
# quando a velocidade registrada estava superior a 105 km/h. Conserte-os.
print('\n--------------------------------------------------\n')


def ajusta105(x):
    if x > 105:
        return x * 0.9
    else:
        return x


print("Ajustando velocidades acima de 105 km/h")
print(sDia3.apply(ajusta105))
print('\n--------------------------------------------------\n')

# ============================================
# Crie as series dos dias 1 e 2
# Acrescente-as  à  Series sDia3, gerando a series sTot
# utilize o método .append
# ============================================
sDia2 = pd.read_excel('pandas3/dia2.xlsx', header=0,
                      index_col=0, squeeze=True, decimal=',')
print(sDia2.head(10))
sDia1 = pd.read_excel('pandas3/dia1.xlsx', header=0,
                      index_col=0, squeeze=True, decimal=',')
print(sDia1.head(10))

print('\n--------------------------------------------------\n')
print("sTotal")
sTot = sDia3.append(sDia1)
sTot = sTot.append(sDia2)
print(sTot)

print('\n--------------------------------------------------\n')

# ============================================
#       Usando Filtros sobre sTot
# ============================================
#  Crie uma cópia de sTot ( sCopia)
#  Substitua os valores ausentes(NaN) pela menor velocidade
sCopia = sTot.copy(deep=True)
sCopia.fillna(sCopia.min())
print(sCopia)

print('\n--------------------------------------------------\n')
print("Mostre todas as horas dos registros da menor velocidade")
print(sTot.idxmin())
print('\n--------------------------------------------------\n')

print('\n--------------------------------------------------\n')
print("Exiba por hora, a quantidade de registros abaixo de 40 km/h")
menorVel = sCopia.min()
sVerdade = sCopia < 40
sMenor = sCopia.loc[sVerdade]
print(sMenor)
print('\n--------------------------------------------------\n')

#  Exiba a velocidade média por hora em sCopia

#  Crie a Series sRapidinhos com os elementos cujos valores são
#  superiores à média de sCopia,  exiba-a graficamente

#  Mostre a porcentagem de veículos com velocidade entre 80km/h e 110km/h


# %%
