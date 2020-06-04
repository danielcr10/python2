# -*- coding: utf-8 -*-
"""        Exercicio de Atrasos     """
import pandas as pd
import matplotlib.pyplot as plt
'''
Considere o arquivo atrasos.xlsx com os minutos de atraso dos funcionários de 
uma empresa em um determinado mês. A Series srAtrasos já disponibilizada abaixo
'''
srAtrasos = pd.read_excel('atrasos.xlsx', index_col=0, header=0, squeeze=True)
print('1- Series srAtrasos')

'''
2 - Qual o maior atraso de um funcionário? Qual (ou quais) funcionário(s)? 
'''
print('2.a - Maior atraso')

print('2.b - Funcionarios com maior atraso')

'''
3 - Crie uma nova series com os funcionários que tiveram atrasos maiores do que
20 minutos. Exiba a nova series. 
'''
print('3- Atrasos maiores do que 20 minutos')

'''
4- Crie uma series (srFaixas) com 3 faixas de atrasos: de 0 a 15, de 15 a 25,
acima de 25. Exiba a series. 
'''
print('4- Faixas de atraso')

'''    5- Faça a tabela de frequência da srFaixas. Exiba-a.   '''
print('5- Tabela de Frequencias das Faixas de atraso')

'''   6- Para cada funcionário exiba o total de atrasos em minuto   '''
print('6- Por funcionario: total de minutos de atraso')

'''
7- Para cada funcionário exiba a sua quantidade de atrasos, seu maior atraso e
seu menor atraso (Dica: crie um agrupamento por índices)
'''
print('7- Por funcionario: quant de atrasos, atrasos max e min')

'''
Considere o arquivo sexo.xlsx com o sexo dos funcionários de uma empresa. 
A Series srSexo já disponibilizada abaixo'''
srSexo=pd.read_excel('sexo.xlsx',index_col=0,header=0,squeeze=True)
print('8- Series srSexo')

'''    9- Agrupe a series srAtrasos pela series srSexo. Exiba-a.    '''
print('9- Agrupando por srSexo')

'''   10- Exiba para cada grupo o maior, o menor e o atraso médio.  '''
print('10- Por Grupo(por sexo): maior atraso, menor atraso, atraso medio')

