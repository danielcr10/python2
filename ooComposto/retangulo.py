import ponto

class Retangulo():
  def __init__(self, p1=ponto.Ponto(), p2=ponto.Ponto(1,1)):
    self.vie = ponto.Ponto(min(p1.x, p2.x), min(p1.y, p2.y))
    self.vsd = ponto.Ponto(max(p1.x, p2.x), max(p1.x, p2.y))
    return

  def __str__(self):
    return str(self.vie) + " " + str(self.vsd)

  def base(self):
    return self.vsd.x - self.vie.x

  def altura(self):
    return self.vsd.y - self.vie.y

  def area(self):
    return self.base() * self.altura()

  def perimetro(self):
    return 2*self.base() + 2*self.altura()
    
vie = ponto.Ponto(1,1)
vsd = ponto.Ponto(3,5)

print(str(vie))
ret = Retangulo(vie, vsd)
print(ret)
print("perimetro: ")
print(ret.perimetro())
xM = (ret.vsd.obtemX() - ret.vie.obtemX())/2
yM = (ret.vsd.obtemX() - ret.vie.obtemX())/2
pM = ponto.Ponto(xM, yM)
print(pM.exibe()) 
