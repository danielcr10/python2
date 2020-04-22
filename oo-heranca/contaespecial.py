from contabancaria import ContaBancaria

class ContaEspecial (ContaBancaria):
  def __init__(self, nConta, senha, titular, limite, saldo):
    super().__init__(nConta, senha, titular, saldo)
    self.limite = limite

  def __str__(self):
    return super().__str__() + "-{:.2f}".format(self.limite)

  def __repr__(self):
        return super().__repr__() + "-{:.2f}".format(self.limite)
  
  def saque(self, valor, senha):
    if senha == self.senha:
      if valor > self.saldo + self.limite:
        print("SALDO INSUFICIENTE")

        return False
      else:
        self.saldo -= valor
        return True
    else:
      print("SENHA INCORRETA")
      return False




contaEsp1=ContaEspecial(111,'a2323','Maria',300,800)
contaEsp=ContaEspecial(222,'b5656','Gab',500,10000000)
contaNorm=ContaBancaria(333,'c7878','Mineiro')
contNorm2=ContaBancaria(444,'d9090','Luis',30000)
lcontas=[contaEsp1,contaEsp,contaNorm,contNorm2]
print("Contas: ", lcontas)
