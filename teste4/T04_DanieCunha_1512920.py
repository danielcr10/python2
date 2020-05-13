#Nome completo: Daniel Cunha Rios
#Matrícula PUC-Rio: 1512920
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

class Acao:
    def __init__(self, nome, cod, valUnita, qtd, tamLote):
      self.nome = nome
      self.cod = cod
      self.valUnita = valUnita
      if qtd % tamLote == 0:
        self.qtd = qtd
      else:
        self.qtd = qtd - qtd % tamLote
      self.tamLote = tamLote
        
    def __str__(self):
      s = "{} ({}) R$ {:.2f} X {} = R$ {:.2f}".format(self.nome, self.cod, self.valUnita, self.qtd, self.valUnita * self.qtd)
      return s
    
    def __add__(self, value):
      novoQtd = self.qtd + value
      novaAcao = Acao(self.nome, self.cod, self.valUnita, novoQtd, self.tamLote)
      return novaAcao



acao = Acao("Petrobras PN", "PETR4", 15.4, 1550, 100)
print("==>",acao)
acao = acao + 257
print("==>",acao)