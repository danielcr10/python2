class Data:
    def __init__(self,d,m,a):
        self.dia = d
        self.mes = m
        self.ano = a
        
    def __str__(self):
        s = 'DATA:'+str(self.dia)+'/'+str(self.mes)+'/'+str(self.ano)
        return s
    
    def __repr__(self):
        s = str(self.dia)+'/'+str(self.mes)+'/'+str(self.ano)
        return s
    
    def __lt__(self, outra): #less than
        tot1= self.ano*10000+self.mes*100+self.dia
        tot2= outra.ano*10000+outra.mes*100+outra.dia
        return tot1<tot2 

    def __eq__(self, outra):
      tot1= self.ano*10000+self.mes*100+self.dia
      tot2= outra.ano*10000+outra.mes*100+outra.dia
      return tot1 == tot2

    def __gt__(self, outra):
      tot1= self.ano*10000+self.mes*100+self.dia
      tot2= outra.ano*10000+outra.mes*100+outra.dia
      return tot1 > tot2

    def __le__(self, outra):
      tot1= self.ano*10000+self.mes*100+self.dia
      tot2= outra.ano*10000+outra.mes*100+outra.dia
      return tot1<=tot2

    def __ge__(self, outra):
      tot1= self.ano*10000+self.mes*100+self.dia
      tot2= outra.ano*10000+outra.mes*100+outra.dia
      return tot1 >= tot2

    def __ne__(self, outra):
      return not self.__eq__(outra)

    def exibe(self): #11/12/2017 => 11 de dezembro de 2017
      meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

      print(self.dia + " de " + meses[self.mes - 1] + " de " + self.ano)