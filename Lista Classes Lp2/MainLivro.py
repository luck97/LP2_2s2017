from Livro import Livro

nome = input("Qual o nome do livro? ")
paginas = int(input("número de páginas ? "))
autor = input("nome do autor ? ")
preco = float(input("qual o preço ? "))

livro = Livro(nome, paginas, autor)
livro.setPreco(preco)

print("""
    Livro: %s
    Páginas: %d
    Autor: %s
    Preço: %.2f
""" % (livro.nome, livro.qtdPagina, livro.autor, livro.getPreco()))