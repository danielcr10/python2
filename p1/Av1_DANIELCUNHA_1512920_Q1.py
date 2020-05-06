#Nome completo: Daniel Cunha Rios
#Matrícula PUC-Rio:1512920
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def criaDicPaisComemoracao(comemoracao):
  dic = {}
  for comem in comemoracao:
    if comem[0] not in dic:
      dic[comem[0]] = {}
    tmp = dic[ comem[0] ].get(comem[2], [])
    tmp.append(comem[1])
    dic[comem[0]][comem[2]] = tmp
  return dic


def criaDicDataPais(comemoracoes):
  dInv = {}

  for pais, dici in comemoracoes.items():
    for data, nome in dici.items():
      if data not in dInv:
        dInv[data] = {}
      dInv[data][pais] = nome

  return dInv


def obtemComemoracoes(dic, data, pais):
  ret = dic.get(data, 'Nenhum país tem comemoração nesta data')
  if type(ret) is dict:
    ret = ret.get(pais, 'Este país não tem comemoração nesta data')
    if type(ret) is list:
      ret = len(ret)
  print(ret)

tComemoracoes = (('Brasil', 'Dia do Amigo', '18/04'), ('Argentina', 'Dia da Primavera', '21/09'), ('Brasil', 'Dia dos Pais', '09/08'),
('Brasil', 'Dia da Primavera', '22/09'), ('Argentina', 'Dia do Amigo', '20/07'), ('Brasil', 'Dia das Crianças', '12/10'),
('Argentina', 'Dia das Mães', '18/10'), ('Argentina', 'Dia dos Pais', '21/06'), ('Argentina', 'Dia das Crianças', '09/08'),
('Argentina', 'Dia dos Namorados', '14/02'), ('Chile', 'Dia Internacional dos Povos Indígenas', '09/08'),
('Argentina', 'Dia dos Professores', '11/09'), ('Chile', 'Dia dos Namorados', '14/02'), ('Chile', 'Dia das Mães', '03/05'),
('Brasil', 'Dia Internacional dos Povos Indígenas', '09/08'), ('Brasil', 'Dia das Mães', '03/05'), ('Chile', 'Dia do Trabalho', '01/05'),
('Brasil', 'Dia do Trabalho', '01/05'), ('Brasil', 'Dia das Mães', '10/05'), ('Brasil', 'Dia Mundial do Radioamador', '18/04'),
('Argentina', 'Dia Mundial do Radioamador', '18/04'), ('Chile', 'Dia Mundial do Radioamador', '18/04'),
('Argentina', 'Dia Internacional dos Povos Indígenas', '09/08'),
)

comemoracoes = criaDicPaisComemoracao(tComemoracoes)
dComemoracoes = criaDicDataPais(comemoracoes)
# obtemComemoracoes(dComemoracoes, '03/05', 'Brasil')
# obtemComemoracoes(dComemoracoes, '14/02', 'Brasil')
# obtemComemoracoes(dComemoracoes, '18/04', 'Brasil')
# obtemComemoracoes(dComemoracoes, '25/09', 'Brasil')

data1 = input("Data desejada: ")
pais1 = input("Pais desejado: ")
data2 = input("Outra data desejada: ")
pais2 = input("Outro pais desejado: ")
data3 = input("Outra data desejada: ")
pais3 = input("Outro pais desejado: ")
data4 = input("Outra data desejada: ")
pais4 = input("Outro pais desejado: ")


obtemComemoracoes(dComemoracoes, data1, pais1)
obtemComemoracoes(dComemoracoes, data2, pais2)
obtemComemoracoes(dComemoracoes, data3, pais3)
obtemComemoracoes(dComemoracoes, data4, pais4)