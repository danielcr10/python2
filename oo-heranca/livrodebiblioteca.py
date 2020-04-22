from livro import Livro

class LivroDeBiblioteca(Livro):
  def __init__(self, nome, assunto, autores, nPaginas, exemplares):
    super().__init__(nome, assunto, autores, nPaginas)
    self.exemplares = exemplares
    # acrescentar uma lista onde cada elemento é uma lista com nº do exemplar e situação do exemplar (‘E’ ou ‘D’). 
      
  def __str__(self):
    return super().__str__() + "\nExemplares: {}".format(self.exemplares)

  def __repr__(self):
        return super().__str__() + "\nExemplares: {}".format(self.exemplares)


  def consultarLivro (self):
    return self.exemplares

  def acrescentarLivro (self, cod):
    self.exemplares.append([cod, "D"])

  def removerLivro (self, cod):
    # recebe o nº do exemplar e remove da lista de exemplares a lista contendo o nº do exemplar e sua situação
    for exemplar in self.exemplares:
      if exemplar[0] == cod:
        self.exemplares.remove(exemplar)

  def emprestarLivro (self):
    # retorna o nº do exemplar emprestado, atualizando sua situação
    for exemplar in self.exemplares:
      if exemplar[1] == "D":
        exemplar[1] = "E"
        return exemplar[0]
    return 0 

  def devolverLivro (self, cod):
    # recebe o nº do exemplar, atualizando sua situação
    for exemplar in self.exemplares:
      if exemplar[0] == cod:
        exemplar[1] = "D"


livro1 = LivroDeBiblioteca("nome1", "assunto1", "autores1", 100, [[1, "D"], [2, "E"], [3, "D"]])
livro2 = LivroDeBiblioteca("nome2", "assunto2", ("autores2", "autor7", "autor 8"), 130, [[1, "E"], [2, "E"], [3, "D"]])
livro3 = LivroDeBiblioteca("nome3", "assunto3", "autores3", 150, [[1, "E"], [2, "E"], [3, "E"]])
livro4 = LivroDeBiblioteca("nome3", "assunto3", "autores3", 300, [[1, "D"], [2, "E"], [3, "D"]])
livro5 = LivroDeBiblioteca("nome4", "assunto4", "autores4", 270, [[1, "d"], [2, "D"], [3, "D"]])

livros = [livro1, livro2, livro3, livro4, livro5]

print(livro1.consultarLivro())
livro1.acrescentarLivro(4)
print(livro1.consultarLivro())
livro1.emprestarLivro()
print(livro1.consultarLivro())
livro1.emprestarLivro()
print(livro1.consultarLivro())
livro1.removerLivro(1)
print(livro1.consultarLivro())
livro1.devolverLivro(2)
print(livro1.consultarLivro())
print()
print(livros)
