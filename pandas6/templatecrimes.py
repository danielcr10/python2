# -*- coding: utf-8 -*-
"""
Crimes
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
No arquivo crimeszs.xlsx encontram-se registrados os crimes cometidos na zona sul
na ultima sexta-feira. Cada linha tem: bairro onde foi cometido o crime e tipo do
crime cometido
'''
'''
1- A Series srCrimes foi criada a partir do arquivo crimeszs.xlsx, deixando os 
bairros como indices
'''
srCrimes=pd.read_excel('crimeszs.xlsx',header=0,index_col=0,squeeze=True)
print('\n1- Series dos crimes')


'''
2- Valores Nan devem ser preenchidos com "NAO ESPECIFICADO'. Exiba  a series 
resultante
'''
print('\n2- Com Valores NaN  preenchidos com "NAO ESPECIFICADO"')


'''
3- Exiba o numero total de crimes. Exiba  a series resultante.
'''
print('\n3-Numero total de crimes')


'''
4- Crie agora a tabela de frequencia dos crimes (srTabFreqCrimes). Exiba a tabela
'''
print('\n4- Tabela de Frequencia dos Crimes')


'''
5- Tabela de Frequencia e Tabela de Frequencia Relativa (tambem chamada Tabela de
 Frequencia Percentual): A tabela de frequencia relativa e´obtida considerando-se 
o total. Por exemplo: se o numero de homicidios for 12 e o numero e o total de 
crimes for 40, homicidios sao 30% dos crimes. Para se obter a (series) Tabela de 
Frequencia Relativa fazemos: srTabFreqRel = srTabFreq*100/srCrimes.size
'''
print('\n5-Tabela de Frequencia Relativa dos Crimes')


'''
6- Qual(is) o(s) crime(s) com maior numero de ocorrencias?
   E qual a quantidade de ocorrencias desse(s) crime(s)?
'''
print('\n6.1- Crime(s) com maior numero de ocorrencias')



print('\n6.2- E a quantidade de ocorrencias desse(s) crime(s)')



'''
7- Crie uma series srGavea so com os crimes na GAVEA
'''

'''
7.1- Exiba a series srGavea
'''
print('\n7.1 -Crimes na GAVEA')

'''
7.2- Exiba a quantidade de HOMICIDIO na Gavea
'''
print('\n7.2 Quantidade de HOMICIDIOS na GAVEA')


'''
8- Crie  a series srBOTA so com os crimes em BOTAFOGO
'''
'''
8.1 - Exiba a series srBOTA
'''
print('\n8.1- Crimes em BOTAFOGO')


'''
8.2 - Qual o crime que mais ocorreu em BOTAFOGO'
'''
print('\n8.2- Crime que mais ocorreu em BOTAFOGO')


'''
9 - Exiba a quantidade de crimes por bairro.
'''
print('\n9- Quantidade de Crimes por Bairro')

'''
10 - Qual(is) o(s) bairro(s) com a maior quantidade de crimes?
'''
print('\n10- Bairro(s) com maior quantidade de crimes')




