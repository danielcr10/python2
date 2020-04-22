from livro import Livro

class LivroDeLivraria(Livro):
  def __init__(self, nome, assunto, autores, nPaginas, preco, qtdEstoque):
    super().__init__(nome, assunto, autores, nPaginas)
    self.preco = preco
    self.qtdEstoque = qtdEstoque
      
  def __str__(self):
    return super().__str__() + "\nPreço: {:.2f}\nQuantidade em estoque: {:d}".format(self.preco, self.qtdEstoque)

  def __repr__(self):
    return super().__repr__() + "\nPreço: {:.2f}\nQuantidade em estoque: {:d}".format(self.preco, self.qtdEstoque)

  def consultarPreco(self):
    return self.preco

  def alterarPreco(self, novoPreco):
    self.preco = novoPreco

  def venderLivro(self, qtd):
    if self.qtdEstoque >= qtd:
      return (self.preco, self.preco * qtd)
    else:
      return (0,0)

  def devolverLivro(self, qtdDevolvida):
    self.qtdEstoque += qtdDevolvida

livro1 = LivroDeLivraria("nome1", "assunto1", "autores1", 100, 15, 30)
livro2 = LivroDeLivraria("nome2", "assunto2", ("autores2", "autor7", "autor 8"), 130, 9.90, 50)
livro3 = LivroDeLivraria("nome3", "assunto3", "autores3", 150, 20, 15)
livro4 = LivroDeLivraria("nome3", "assunto3", "autores3", 300, 59.20, 4)
livro5 = LivroDeLivraria("nome4", "assunto4", "autores4", 270, 49, 30)

livros = [livro1, livro2, livro3, livro4, livro5]
print(livro4.consultarPreco())
print(livro5)
livro5.alterarPreco(29.7)
print(livro5)
print(livro1.venderLivro(5))
print(livro4.venderLivro(5))
print(livros[3])
print(livro2)
print(livro2.devolverLivro(3))
print(livro2)
print(livros)
