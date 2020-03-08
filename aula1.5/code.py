if __name__ == "__main__":
    main()

def main():
  return

def listaMaiorElem (lista):
  maiorElem = lista[0]
  for elem in lista:
    if elem < maiorElem:
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