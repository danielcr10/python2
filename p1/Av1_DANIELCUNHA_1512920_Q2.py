#Nome completo: Daniel Cunha Rios
#Matrícula PUC-Rio:1512920
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

class Endereco():
  def __init__(self, rua, numero):
    self.rua = rua
    self.numero = numero

  def __str__(self):
    return "{}, {}".format(self.rua, self.numero)

class Pessoa():
  def __init__(self, nome, email):
    self.nome = nome
    self.email = email

  def __str__(self):
    return "{} - {}".format(self.nome, self.email)

class Contato(Pessoa):
  def __init__(self, nome, email, rua, numero):
    super().__init__(nome, email)
    self.nome = nome
    self.email = email
    self.endereco = Endereco(rua, numero)

  def __str__(self):
    return super().__str__() + " - {}".format(self.endereco)

class Agenda():
  def __init__(self):
    self.agenda = {}
  
  def inclui(self, nome, email, rua, numero):
    self.agenda[nome] = Contato(nome, email, rua, numero)

  def __str__(self):
    s = ""
    for nome, dados in self.agenda.items():
      s += dados.__str__() + "\n"
    return s



agenda = Agenda()
print(agenda)
agenda.inclui('Fulano', 'fulano@email.com', 'Sobe e Desce', 2578)
agenda.inclui('Ciclano', 'ciclano@servidor.com.br', 'Cafundó', 8752)
print(agenda)
agenda.inclui('Ciclano', 'ciclano@servidor.com.br', 'Cafundó', 25)
agenda.inclui('Gian', 'contato@revva.com.br', 'Erechim', 39)
print(agenda)