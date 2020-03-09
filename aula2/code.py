# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:22:41 2020

@author: PC48
"""
from random import randint

def maiorNumeroAcertos(apostas, resultado):
    sApostas = map(set,apostas)
    sResultado = set(resultado)
    # fazer adicionando somente a que tem resultado
    count = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for aposta in sApostas:
        count[len(aposta & sResultado)].append(list(aposta))
    
    maior = max({k: v for k, v in count.items() if v})
    
    return [maior, count[maior]]

def main():
    #apostas = [[randint(0, 61) for p in range(0, 6)] for _ in range(10)]
    #resultado = [randint(0, 61) for p in range(0, 6)]
    apostas = [ [6,3,18,49,45,57], [6,2,25,37,38,39,42,54], [51,18,37,40,44,4], [6,25,40,41,51,52,57], [1,2,6,37,49,59] ]
    resultado = [18,6,40,42,51,58]
    print(maiorNumeroAcertos(apostas, resultado))
    return
