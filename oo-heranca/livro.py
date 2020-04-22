class Livro():
  def __init__(self, nome, assunto, autores, nPaginas):
    self.nome = nome
    self.assunto = assunto
    self.autores = autores
    self.nPaginas = nPaginas
    
  def __str__(self):
    return "Nome do livro: {}\nAssunto: {}\nAutores: {}\nNumero de paginas: {:d}".format(self.nome, self.assunto, self.autores, self.nPaginas)

  def __repr__(self):
    return "Nome do livro: {}\nAssunto: {}\nAutores: {}\nNumero de paginas: {:d}".format(self.nome, self.assunto, self.autores, self.nPaginas)
