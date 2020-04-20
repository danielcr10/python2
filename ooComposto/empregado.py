import data

class Empregado:
  def __init__(self, num, nome, sal, diaAd, mesAd, anoAd):
    self.num = num
    self.nome = nome
    self.sal = sal
    self.dtAdm = data.Data(diaAd, mesAd, anoAd)

  def __str__(self):
    s = "Num: {:d} - Nome: {:s} - Sal: {:.2f} - Data Admissao: {}".format(self.num, self.nome, self.sal, self.dtAdm)
    return s

  def admDepoisDe(self, data):
    return self.dtAdm > data



empregados = [Empregado(1, "Jefferson", 3000, 20, 1, 2011), Empregado(3, "Jorge", 9000, 3, 7, 2008), Empregado(4, "Claudio", 2000, 5, 4, 2015), Empregado(5, "Jose", 3000, 1, 1, 2000), Empregado(90, "Cleude", 8000, 30, 9, 2010)]

dia = int(input("Dia: "))
mes = int(input("mes: "))
ano = int(input("ano: "))
minhaData = data.Data(dia, mes, ano)

for emp in empregados:
  if emp.admDepoisDe(minhaData):
    print(emp)
# Para testar sua classe crie uma lista com 5 empregados.  
# Leia dia, mês e ano do teclado e crie uma data com esses dados. 
# Exiba todos os empregados que foram admitidos depois dessa data.


