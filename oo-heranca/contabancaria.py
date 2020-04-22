class ContaBancaria():
  def __init__(self, nConta, senha, titular, saldo=0):
    self.nConta = nConta
    self.senha = senha
    self.titular = titular
    self.saldo = saldo

  def __str__(self):
    return "{}-{}-{:.2f}".format(self.nConta, self.titular, self.saldo)

  def __repr__(self):
    return "{}-{}-{:.2f}".format(self.nConta, self.titular, self.saldo)

  def exibeSaldo(self, senha):
    if senha == self.senha:
      print("SALDO EM CONTA: {:.2f}".format(self.saldo))
    else:
      print("SENHA INCORRETA")

  def deposito(self, valor):
    self.saldo += float(valor)

  def saque(self, valor, senha):
    if senha == self.senha:
      if valor > self.saldo:
        print("SALDO INSUFICIENTE")
        return False
      else:
        self.saldo -= valor
        return True
    else:
      print("SENHA INCORRETA")
      return False