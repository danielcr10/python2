import math
class Ponto():
  def __init__(self, x=0, y=0):
    # if(x is None)
    #   self.x = 0
    #   self.y = 0
    # else:
    self.x = x
    self.y = y

  def quadrante (self):
    if self.x > 0:
      if self.y > 0:
        return 1
      else:
        return 4
    else:
      if self.y > 0:
        return 2
      else:
        return 3

  def exibe(self):
    print(self.x, self.y)

  def distancia(self, outroPonto):
    deltaX = self.x - outroPonto.x
    deltay = self.y - outroPonto.y
    dist = math.sqrt(deltaX**2 + deltay**2)
    return dist

  def desloca (self, deltaX = 0, deltaY = 0):
    self.x += deltaX
    self.y += deltaY
    return