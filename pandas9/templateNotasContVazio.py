# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 10:11:03 2017

@author: claudia ferlin
"""

import pandas as pd
import matplotlib.pyplot as plt


#------------------------------------------------------------------------------
#   OPERANDO/TRANSFORMANDO/RESUMINDO
#------------------------------------------------------------------------------

# Calcule e inclua em dfGeral as Notas G1,G2 e G3 ==> Ti*0.2 + Pi*0.8
print("\n30 - dfGeral com G1,G2 e G3\n")

# Calcule a Média de cada aluno e inclua uma coluna com a mesma
print("\n31 - dfGeral com a media de cada aluno\n")

# Inclua uma coluna com a situação do Aluno: Ap (Media>=5 e G1,G2 e G3>=3) ou G4
print("\n32 - dfGeral com coluna Situação Final\n")

# exibir graficamente (pie) a porcentagem de alunos em G4 e AP 
print("\n33 - porcentagem de alunos em G4 e AP \n")

#------------------------------------------------------------------------------
#   FILTRANDO
#------------------------------------------------------------------------------

# Filtrando para mostrar o DF dos alunos cuja G1>G2>G3
print('\n34 - alunos com G1>G2>G3\n')

#Filtrando para mostrar o DF dos alunos com G3 >3
print('\n35 - alunos com G3>3\n')

# Mostrar qtos e DF dos alunos com algum Testei > Provai 
print('\n36 - alunos com algum Testei > Provai\n')

#Criando uma cópia sem os alunos com faltas > 3. Lembre-se que o drop necessita de valores de index ou column
print('\n37 - Df dos alunos com até 3 faltas:\n')


