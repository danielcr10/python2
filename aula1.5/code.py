

def listaMaiorElem (lista):
  maiorElem = lista[0]
  for elem in lista:
    if elem > maiorElem:
      maiorElem = elem
  return maiorElem

def listaSomaElem(lista):
  soma = 0
  for elem in lista:
    soma += elem
  return soma

def listaOcorPrimElem(lista):
  ocorr = 0
  for elem in lista:
    if elem == lista[0]:
      ocorr += 1
  return ocorr

def listaMediaElem(lista):
  return listaSomaElem(lista)/len(lista)

def listaProxMedia(lista):
  media = listaProxMedia(lista)
  dif = media - lista[0]
  result = lista[0] 
  for elem in lista:
    if media - elem < dif:
      result = elem
  return result

def listaSomaElemNeg(lista):
  soma = 0
  for elem in lista:
    if elem < 0:
      soma += elem
  return soma

def listaQtdVizIguais(lista):
  soma = 0
  for i in len(lista):
    if lista[i] == lista[i+1]:
      soma += 1
  return soma

def listaSubElem(lista): # Exiba todas as possibilidades de sublistas com 2 elementos
  
  return


# --------------------------------------------

#         Exercicio 2

# --------------------------------------------

def traduzir(lSecreta):
  lista = list(" abcdefghijklmnopqrstuvwxyz")
  msg = ""
  for num in lSecreta:
    msg = msg + lista[int(num)]
  return msg


# --------------------------------------------

#         Exercicio 3

# --------------------------------------------

def controlaFaltas(lJogos):
  faltas = {'Brasil':0, 'Italia':0, 'Espanha':0}
  for jogo in lJogos:
    faltas[jogo[0]] += jogo[2][0]
    faltas[jogo[1]] += jogo[2][1]
  total = faltas['Brasil'] + faltas['Italia'] + faltas['Espanha']
  maisFaltas = max(faltas, key=faltas.get)
  menosFaltas = min(faltas, key=faltas.get)
  print('Total de faltas: ', total)
  print('Time com menos faltas: ', menosFaltas)
  print('Time com mais faltas: ', maisFaltas)
  return

def main():
  controlaFaltas([['Brasil', 'Italia', [10, 9]], [
                 'Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7, 8]]])
  return


if __name__ == "__main__":
    main()
