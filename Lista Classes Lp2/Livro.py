class Livro():
    def __init__(self, nome, qtdPagina, autor):
        self.nome = nome
        self.qtdPagina = qtdPagina
        self.autor = autor

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco