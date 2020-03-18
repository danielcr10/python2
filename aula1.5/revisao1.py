def listaMaiorElem (lista):
  maiorElem = lista[0]
  for elem in lista[1:]:
    if elem > maiorElem:
      maiorElem = elem
  return maiorElem

def listaSomaElem(lista):
  soma = 0
  for elem in lista:
    soma += elem
  return soma

def listaOcorPrimElem(lista):
  ocorr = 1
  for elem in lista[1:]:
    if elem == lista[0]:
      ocorr += 1
  return ocorr

def listaMediaElem(lista):
  return listaSomaElem(lista)/len(lista)

def listaProxMedia(lista, pMedia):
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